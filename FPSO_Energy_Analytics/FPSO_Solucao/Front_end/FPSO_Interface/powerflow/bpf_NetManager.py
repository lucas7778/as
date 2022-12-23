import pandapower as pp
import math


class bpf_NetManager:
    """
        Classe gerenciadora da execução de tarefas associadas ao
        módulo Fluxo de Potência
    """

    def __init__(self):
        """
        """
        self.__bpf_net = None
        self.__bpf_sub = []
        self.__bpf_cos = []
        self.__bpf_mlcos = []
        self.__bpf_mlmodel = []
        self.__bpf_res = ""
        self.__bpf_pngen = None

    @property
    def bpf_mlmodel(self):
        return self.__bpf_mlmodel

    @bpf_mlmodel.setter
    def bpf_mlmodel(self, value):
        self.__bpf_mlmodel = value

    @property
    def bpf_cos(self):
        return self.__bpf_cos

    @bpf_cos.setter
    def bpf_cos(self, value):
        self.__bpf_cos = value

    @property
    def bpf_pngen(self):
        return self.__bpf_pngen

    @bpf_pngen.setter
    def bpf_pngen(self, value):
        self.__bpf_pngen = value

    @property
    def bpf_mlcos(self):
        return self.__bpf_mlcos

    @bpf_mlcos.setter
    def bpf_mlcos(self, value):
        self.__bpf_mlcos = value

    @property
    def bpf_sub(self):
        return self.__bpf_sub

    @bpf_sub.setter
    def bpf_sub(self, value):
        self.__bpf_sub = value

    @property
    def bpf_net(self):
        return self.__bpf_net

    @bpf_net.setter
    def bpf_net(self, value):
        self.__bpf_net = value

    @property
    def bpf_res(self):
        return self.__bpf_res

    @bpf_res.setter
    def bpf_res(self, value):
        self.__bpf_res = value

    def bpf_nunet(self, name, f_hz, sn_mva):
        """
        Método utilizado para inicializar uma rede.
        """
        # Inicializa uma rede vazia para poder salva-la
        self.bpf_net = pp.create_empty_network(name=name,
                                               f_hz=f_hz,
                                               sn_mva=sn_mva)

        # Salva a rede em formato .json
        pp.to_json(self.bpf_net, filename=name + ".json")

    def bpf_load(self, name):
        """

        """
        # Carrega uma rede salva para o atributo bpf_net
        self.bpf_net = pp.from_json(name + ".json")

    def bpf_get(self, bpf_type=None, bpf_param=None, bpf_elem=None, is_gen_bus=None, is_process_load=None):
        """

        """
        # retorna listas de atributos
        if bpf_param is None and bpf_elem is None:
            if bpf_type == 'gen_bus':
                return {
                    'name': 'Nome da barra',
                    'vn_kv': 'Tensão nominal da barra',
                    'in_service': 'Variável que indica se a barra será considerada no Fluxo de Potência',
                    'p_mw': 'Potência ativa nominal dos geradores conectados à barra de geração'
                }
            if bpf_type == 'load_bus':
                return {
                    'name': 'Nome da barra',
                    'vn_kv': 'Tensão nominal da barra',
                    'in_service': 'Variável que indica se a barra será considerada no Fluxo de Potência',
                }
            if bpf_type == 'load':
                return {
                    'name': 'Nome da carga',
                    'bus': 'Nome da barra na qual a carga se conecta',
                    'p_mw': 'Potência ativa em MW',
                    'pf': 'Fator de potência da carga',
                    'in_service': 'Variável que indica se a carga será considerada no Fluxo de Potência',
                    'sub_id': 'Número de identificação do subsistema a que pertence a carga',
                }
            if bpf_type == 'process_load':
                return {
                    'name': 'Nome da carga',
                    'bus': 'Nome da barra na qual a carga se conecta',
                    'ml_model': 'Modelo de previsão associado à carga',
                    'pf': 'Fator de potência da carga',
                    'in_service': 'Variável que indica se a carga será considerada no Fluxo de Potência',
                    'sub_id': 'Número de identificação do subsistema a que pertence a carga'
                }
            if bpf_type == 'trafo':
                return {
                    'name': 'Nome do transformador de 2 enrolamentos',
                    'sn_mva': 'Potência aparente nominal do transformador',
                    'hv_bus': 'Nome da barra do lado de alta tensão',
                    'lv_bus': 'Nome da barra do lado de baixa tensão',
                    'vn_hv_kv': 'Tensão nominal do lado de alta tensão',
                    'vn_lv_kv': 'Tensão nominal do lado de baixa tensão',
                    'in_service': 'Variável que indica se o transformador será considerado no Fluxo de Potência'
                }
            if bpf_type == 'trafo3w':
                return {
                    'name': 'Nome do transformador de 3 enrolamentos',
                    'hv_bus': 'Nome da barra do lado de alta tensão do transformador',
                    'mv_bus': 'Nome da barra do lado de média tensão do transformador',
                    'lv_bus': 'Nome da barra do lado de baixa tensão do transformador',
                    'vn_hv_kv': 'Tensão nominal no lado de alta tensão',
                    'vn_mv_kv': 'Tensão nominal no lado de média tensão',
                    'vn_lv_kv': 'Tensão nominal no lado de baixa tensão',
                    'sn_hv_mva': 'Potência aparente nominal do lado de alta tensão',
                    'sn_mv_mva': 'Potência aparente nominal do lado de média tensão',
                    'sn_lv_mva': 'Potência aparente nominal do lado de baixa tensão',
                    'in_service': 'Variável que indica se o transformador será considerado no Fluxo de Potência',
                }

        # retorna lista de valores de um atributo de determinado tipo de equipamento (só vale para bpf_param == 'name')
        if bpf_type is not None and bpf_param is not None and bpf_elem is None:
            if is_gen_bus is not None:
                if bpf_type == 'bus':
                    if not self.bpf_net.ext_grid.empty:
                        gen_bus_id = self.bpf_net.ext_grid.bus.values[0]
                        ind = self.bpf_net.bus[self.bpf_net.bus.index == gen_bus_id].index.values[0]
                        gen_bus_name = self.bpf_net.bus.at[ind, 'name']
                        if is_gen_bus:
                            return gen_bus_name
                        elif not is_gen_bus:
                            all_buses_names = list(self.bpf_net[bpf_type][bpf_param].values)
                            all_buses_names.remove(gen_bus_name)
                            return all_buses_names  # "all"
                    if self.bpf_net.ext_grid.empty:
                        if is_gen_bus:
                            return ''
                        elif not is_gen_bus:
                            return list(self.bpf_net[bpf_type][bpf_param].values)
            if is_process_load is not None:
                process_loads_names = []
                if bpf_type == 'load':
                    for process_load in self.bpf_mlcos:
                        process_loads_names.append(process_load[0])
                    if is_process_load:
                        return process_loads_names
                    elif not is_process_load:
                        return [load_name for load_name in self.bpf_net[bpf_type][bpf_param].values if load_name not in
                                process_loads_names]

            return list(self.bpf_net[bpf_type][bpf_param])

        # retorna o valor de um parametro de um determinado equipamento
        if bpf_elem is not None:
            if bpf_type == 'gen_bus':
                bpf_type = 'bus'
                if bpf_param in ['name', 'vn_kv', 'in_service']:
                    ind = self.bpf_net[bpf_type][self.bpf_net[bpf_type]['name'] == bpf_elem].index.values[0]
                    return self.bpf_net[bpf_type].at[ind, bpf_param]
                elif bpf_param == 'p_mw':
                    return self.bpf_pngen

            if bpf_type == 'load_bus':
                bpf_type = 'bus'
                ind = self.bpf_net[bpf_type][self.bpf_net[bpf_type]['name'] == bpf_elem].index.values[0]
                return self.bpf_net[bpf_type].at[ind, bpf_param]

            if bpf_type == 'trafo':
                ind = self.bpf_net[bpf_type][self.bpf_net[bpf_type]['name'] == bpf_elem].index.values[0]
                return self.bpf_net[bpf_type].at[ind, bpf_param]

            if bpf_type == 'trafo3w':
                ind = self.bpf_net[bpf_type][self.bpf_net[bpf_type]['name'] == bpf_elem].index.values[0]
                return self.bpf_net[bpf_type].at[ind, bpf_param]

            if bpf_type == 'load':
                if bpf_param in ['name', 'bus', 'in_service', 'p_mw']:
                    ind = self.bpf_net[bpf_type][self.bpf_net[bpf_type]['name'] == bpf_elem].index.values[0]
                    return self.bpf_net[bpf_type].at[ind, bpf_param]
                elif bpf_param == 'pf':
                    for load_cos in self.bpf_cos:
                        if load_cos[0] == bpf_elem:
                            return load_cos[1]
                elif bpf_param == 'sub_id':
                    for sub_id in self.bpf_sub:
                        if sub_id[0] == bpf_elem:
                            return sub_id[1]

            if bpf_type == 'process_load':
                bpf_type = 'load'
                if bpf_param in ['name', 'bus', 'in_service']:
                    ind = self.bpf_net[bpf_type][self.bpf_net[bpf_type]['name'] == bpf_elem].index.values[0]
                    return self.bpf_net[bpf_type].at[ind, bpf_param]
                elif bpf_param == 'pf':
                    for ml_load in self.bpf_mlcos:
                        if ml_load[0] == bpf_elem:
                            return ml_load[1]
                elif bpf_param == 'sub_id':
                    for sub_id in self.bpf_sub:
                        if sub_id[0] == bpf_elem:
                            return sub_id[1]
                elif bpf_param == 'ml_model':
                    for ml_model in self.bpf_mlmodel:
                        if ml_model[0] == bpf_elem:
                            return ml_model[1]

    def bpf_modfy(self, bpf_type=None, bpf_data=None):
        """
        """
        if bpf_type == 'parameter':  # Alterou parâmetro de equipamento já existente
            for i in range(len(bpf_data['bpf_equip'])):
                if bpf_data['bpf_equip'] == 'bus':
                    bpf_cond = self.bpf_net.bus.name == bpf_data['name'][i]
                    bpf_ind = self.bpf_net.bus.index[bpf_cond]
                    self.bpf_net.bus[bpf_data['bpf_param'][i]].values[bpf_ind[0]] = bpf_data['bpf_value'][i]
                if bpf_data['bpf_equip'] == 'load':
                    bpf_cond = self.bpf_net.load.name == bpf_data['name'][i]
                    bpf_ind = self.bpf_net.load.index[bpf_cond]
                    self.bpf_net.load[bpf_data['bpf_param'][i]].values[bpf_ind[0]] = bpf_data['bpf_value'][i]
                if bpf_data['bpf_equip'] == 'trafo':
                    bpf_cond = self.bpf_net.trafo.name == bpf_data['name'][i]
                    bpf_ind = self.bpf_net.trafo.index[bpf_cond]
                    self.bpf_net.trafo[bpf_data['bpf_param'][i]].values[bpf_ind[0]] = bpf_data['bpf_value'][i]
                if bpf_data['bpf_equip'] == 'trafo3w':
                    bpf_cond = self.bpf_net.trafo3w.name == bpf_data['name'][i]
                    bpf_ind = self.bpf_net.trafo3w.index[bpf_cond]
                    self.bpf_net.trafo3w[bpf_data['bpf_param'][i]].values[bpf_ind[0]] = bpf_data['bpf_value'][i]

        if bpf_type == 'equipment':  # Adicionou ou deletou equipamento

            if bpf_data['bpf_equip'] == 'gen_bus':
                if bpf_data['bpf_drop']:
                    # remove a barra slack
                    bus_ind = self.bpf_net.ext_grid.bus.values[0]
                    self.bpf_net.bus.drop(index=bus_ind, inplace=True)
                    # remove a ext_grid
                    bpf_cond = self.bpf_net.ext_grid.name == bpf_data['bpf_infos']['name']
                    bpf_ind = self.bpf_net.ext_grid.index[bpf_cond]
                    self.bpf_net.ext_grid.drop(index=bpf_ind[0], inplace=True)
                else:
                    # Cria a barra de geracao
                    pp.create_bus(
                        net=self.bpf_net,
                        name=bpf_data['bpf_infos']['name'],
                        vn_kv=bpf_data['bpf_infos']['vn_kv'],
                        in_service=bpf_data['bpf_infos']['in_service']
                    )

                    # Pendura a ext_grid - indica que a barra é de referencia
                    bpf_nbus = len(self.bpf_net.bus.name.values)
                    for j in range(bpf_nbus):
                        if bpf_data['bpf_infos']['name'] == self.bpf_net.bus.name.values[j]:
                            bpf_busid = j

                    pp.create_ext_grid(
                        net=self.bpf_net,
                        bus=bpf_busid,
                        name=bpf_data['bpf_infos']['name'],
                        vm_pu=1.0
                    )

                    # armazena a potencia ativa nominal da geraca
                    self.bpf_pngen = bpf_data['bpf_infos']['p_mw']

            if bpf_data['bpf_equip'] == 'load_bus':
                if bpf_data['bpf_drop']:
                    bpf_cond = self.bpf_net.bus.name == bpf_data['bpf_infos']['name']
                    bpf_ind = self.bpf_net.bus.index[bpf_cond]
                    self.bpf_net.bus.drop(index=bpf_ind[0], inplace=True)
                else:
                    pp.create_bus(
                        net=self.bpf_net,
                        name=bpf_data['bpf_infos']['name'],
                        vn_kv=bpf_data['bpf_infos']['vn_kv'],
                        in_service=bpf_data['bpf_infos']['in_service']
                    )

            if bpf_data['bpf_equip'] == 'trafo':
                if bpf_data['bpf_drop']:
                    bpf_cond = self.bpf_net.trafo.name == bpf_data['bpf_infos']['name']
                    bpf_ind = self.bpf_net.trafo.index[bpf_cond]
                    self.bpf_net.trafo.drop(index=bpf_ind[0], inplace=True)
                else:
                    bpf_nbus = len(self.bpf_net.bus.name.values)
                    for j in range(bpf_nbus):
                        if bpf_data['bpf_infos']['hv_bus'] == self.bpf_net.bus.name.values[j]:
                            hv_bus = j
                        if bpf_data['bpf_infos']['lv_bus'] == self.bpf_net.bus.name.values[j]:
                            lv_bus = j

                    # Preenche o DataFrame dentro do pandapower
                    pp.create_transformer_from_parameters(
                        net=self.bpf_net,
                        name=bpf_data['bpf_infos']['name'],
                        sn_mva=bpf_data['bpf_infos']['sn_mva'],
                        hv_bus=hv_bus,
                        lv_bus=lv_bus,
                        vn_hv_kv=bpf_data['bpf_infos']['vn_hv_kv'],
                        vn_lv_kv=bpf_data['bpf_infos']['vn_lv_kv'],
                        in_service=bpf_data['bpf_infos']['in_service'],
                        vk_percent=6.0,
                        vkr_percent=1.2,
                        pfe_kw=4.0,
                        i0_percent=0.22,
                        shift_degree=0,
                    )

            if bpf_data['bpf_equip'] == 'trafo3w':
                if bpf_data['bpf_drop']:
                    bpf_cond = self.bpf_net.trafo3w.name == bpf_data['bpf_infos']['name']
                    bpf_ind = self.bpf_net.trafo3w.index[bpf_cond]
                    self.bpf_net.trafo3w.drop(index=bpf_ind[0], inplace=True)
                else:
                    bpf_nbus = len(self.bpf_net.bus.name.values)
                    for j in range(bpf_nbus):
                        if bpf_data['bpf_infos']['hv_bus'] == self.bpf_net.bus.name.values[j]:
                            hv_bus = j
                        if bpf_data['bpf_infos']['mv_bus'] == self.bpf_net.bus.name.values[j]:
                            mv_bus = j
                        if bpf_data['bpf_infos']['lv_bus'] == self.bpf_net.bus.name.values[j]:
                            lv_bus = j

                    # Preenche o DataFrame no pandapower
                    pp.create_transformer3w_from_parameters(
                        net=self.bpf_net,
                        name=bpf_data['bpf_infos']['name'],
                        hv_bus=hv_bus,
                        mv_bus=mv_bus,
                        lv_bus=lv_bus,
                        vn_hv_kv=bpf_data['bpf_infos']['vn_hv_kv'],
                        vn_mv_kv=bpf_data['bpf_infos']['vn_mv_kv'],
                        vn_lv_kv=bpf_data['bpf_infos']['vn_lv_kv'],
                        sn_hv_mva=bpf_data['bpf_infos']['sn_hv_mva'],
                        sn_mv_mva=bpf_data['bpf_infos']['sn_hv_mva'],
                        sn_lv_mva=bpf_data['bpf_infos']['sn_lv_mva'],
                        in_service=bpf_data['bpf_infos']['in_service'],
                        vk_hv_percent=10.4,
                        vk_mv_percent=10.4,
                        vk_lv_percent=10.4,
                        vkr_hv_percent=0.28,
                        vkr_mv_percent=0.32,
                        vkr_lv_percent=0.35,
                        pfe_kw=20,
                        i0_percent=0.89
                    )

            if bpf_data['bpf_equip'] == 'load':
                if bpf_data['bpf_drop']:
                    bpf_cond = self.bpf_net.load.name == bpf_data['bpf_infos']['name']
                    bpf_ind = self.bpf_net.load.index[bpf_cond]
                    self.bpf_net.load.drop(index=bpf_ind[0], inplace=True)
                else:
                    bpf_nbus = len(self.bpf_net.bus.name.values)
                    for j in range(bpf_nbus):
                        if bpf_data['bpf_infos']['bus'] == self.bpf_net.bus.name.values[j]:
                            bpf_busid = j

                    cosphi = bpf_data['bpf_infos']['pf']
                    p_mw = bpf_data['bpf_infos']['p_mw']
                    q_mvar = p_mw / cosphi * math.sin(math.acos(cosphi))

                    pp.create_load(
                        net=self.bpf_net,
                        name=bpf_data['bpf_infos']['name'],
                        bus=bpf_busid,
                        p_mw=bpf_data['bpf_infos']['p_mw'],
                        q_mvar=q_mvar,
                        in_service=bpf_data['bpf_infos']['in_service']
                    )

                    # Verifica se pertence a um subsistema e preenche o subsistema
                    if bpf_data['bpf_infos']['sub_id'] != None:
                        self.bpf_sub.append([bpf_data['bpf_infos']['name'],
                                             bpf_data['bpf_infos']['sub_id']])

                    # Salva os fatores de potência das cargas de processo
                    self.bpf_cos.append([bpf_data['bpf_infos']['name'],
                                         bpf_data['bpf_infos']['pf']])

            if bpf_data['bpf_equip'] == 'process_load':
                if bpf_data['bpf_drop']:
                    bpf_cond = self.bpf_net.load.name == bpf_data['bpf_infos']['name']
                    bpf_ind = self.bpf_net.load.index[bpf_cond]
                    self.bpf_net.load.drop(index=bpf_ind[0], inplace=True)
                else:
                    bpf_nbus = len(self.bpf_net.bus.name.values)
                    for j in range(bpf_nbus):
                        if bpf_data['bpf_infos']['bus'] == self.bpf_net.bus.name.values[j]:
                            bpf_busid = j

                    pp.create_load(
                        net=self.bpf_net,
                        name=bpf_data['bpf_infos']['name'],
                        bus=bpf_busid,
                        in_service=bpf_data['bpf_infos']['in_service'],
                        p_mw=0,  # default para criar cargas de processo
                    )

                    # Verifica se pertence a um subsistema e preenche o subsistema
                    if bpf_data['bpf_infos']['sub_id'] != None:
                        self.bpf_sub.append([bpf_data['bpf_infos']['name'],
                                             bpf_data['bpf_infos']['sub_id']])

                    # Salva os fatores de potência das cargas de processo
                    self.bpf_mlcos.append([bpf_data['bpf_infos']['name'],
                                           bpf_data['bpf_infos']['pf']])

                    # Salva os fatores de potência das cargas de processo
                    self.bpf_mlmodel.append([bpf_data['bpf_infos']['name'],
                                             bpf_data['bpf_infos']['ml_model']])

    def bpf_runpf(self, ml_loads):

        for load_name_pmw in ml_loads:
            # pega o index da carga no data frame de cargas
            ind = self.bpf_net.load[self.bpf_net.load['name'] == load_name_pmw[0]].index.values[0]
            # roda a lista de listas: nome da carga de processo, fator de potencia
            for load_name_cos in self.bpf_mlcos:
                if load_name_cos[0] == load_name_pmw[0]:
                    cosphi = load_name_cos[1]
                    p_mw = load_name_pmw[1]
                    q_mvar = p_mw / cosphi * math.sin(math.acos(cosphi))
                    self.bpf_net.load.at[ind, 'p_mw'] = p_mw
                    self.bpf_net.load.at[ind, 'q_mvar'] = q_mvar

        # checa se a rede esta apta a rodar o fluxo de potencia
        diag_dict = pp.diagnostic(self.bpf_net)

        if bool(diag_dict):

            found_errors = []
            for key in diag_dict.keys():
                if key == "missing_bus_indices":
                    found_errors.append(key)
                elif key == "disconnected_elements":
                    found_errors.append(key)
                elif key == "different_voltage_levels_connected":
                    found_errors.append(key)
                elif key == "impedance_values_close_to_zero":
                    found_errors.append(key)
                elif key == "nominal_voltages_dont_match":
                    found_errors.append(key)
                elif key == "invalid_values":
                    found_errors.append(key)
                elif key == "overload":
                    found_errors.append(key)
                elif key == "wrong_switch_configuration":
                    found_errors.append(key)
                elif key == "multiple_voltage_controlling_elements_per_bus":
                    found_errors.append(key)
                elif key == "no_ext_grid":
                    found_errors.append(key)
                elif key == "wrong_reference_system":
                    found_errors.append(key)
                elif key == "deviation_from_std_type":
                    found_errors.append(key)
                elif key == "numba_comparison":
                    found_errors.append(key)
                elif key == "parallel_switches":
                    found_errors.append(key)

            error_log = 'Alguns erros foram encontrados, o que impediu a execução do Fluxo de Potência.\n\n'

            for error in found_errors:
                if error == "missing_bus_indices":
                    error_log = error_log + "Os seguintes elementos apresentam algum terminal flutuando devido à remoção das barras a eles associadas:\n"
                    i = 1
                    for equipment_type, equipments_list in diag_dict[error].items():
                        if equipment_type == 'load':
                            error_log = error_log + "\nCargas " \
                                                    "---------------------------------------------------------------\n\n "
                            for load in equipments_list:
                                load_name = self.bpf_net.load.at[load[0], 'name']
                                error_log = error_log + "    " + load_name + ": a barra a qual a carga estava " \
                                                                             "conectada foi removida. Conecte a uma " \
                                                                             "nova barra ou remova esta carga." + "\n "
                        if equipment_type == 'trafo':
                            error_log = error_log + "\nTransformadores de dois enrolamentos ---------------------------------\n\n"
                            for trafo in equipments_list:
                                trafo_name = self.bpf_net.trafo.at[trafo[0], 'name']
                                if trafo[1] == 'hv_bus':
                                    terminal = "terminal de alta tensão"
                                elif trafo[1] == 'lv_bus':
                                    terminal = "terminal de baixa tensão"
                                error_log = error_log + "    " + trafo_name + ": a barra do " + terminal + " foi " \
                                                                                                           "removida." \
                                                                                                           " Conecte " \
                                                                                                           "este " \
                                                                                                           "terminal " \
                                                                                                           "a uma " \
                                                                                                           "nova " \
                                                                                                           "barra ou " \
                                                                                                           "remova o " \
                                                                                                           "transformador." + "\n "
                        if equipment_type == 'trafo3w':
                            error_log = error_log + "\nTransformadores de três enrolamentos " \
                                                    "---------------------------------\n\n "
                            for trafo3w in equipments_list:
                                trafo3w_name = self.bpf_net.trafo3w.at[trafo3w[0], 'name']
                                if trafo3w[1] == 'hv_bus':
                                    terminal = "terminal de alta tensão"
                                elif trafo3w[1] == 'lv_bus':
                                    terminal = "terminal de baixa tensão"
                                elif trafo3w[1] == 'mv_bus':
                                    terminal = "terminal de média tensão"
                                error_log = error_log + "    " + trafo3w_name + ": a barra do " + terminal + " foi removida. Conecte este terminal a uma nova barra ou remova o transformador." + "\n"



                elif error == "disconnected_elements":
                    num_islands = len(diag_dict[error])
                    error_log = error_log + "Foi identificada a formação de " + str(
                        num_islands) + " ilha(s) desconectada(s) da rede onde está a geração:\n"
                    i = 1
                    for island in diag_dict[error]:
                        error_log = error_log + "\n" + "    Ilha " + str(i) + " formada pelos seguintes elementos:\n"
                        i = i + 1
                        for equipment_type in island.keys():
                            if equipment_type == 'loads':
                                it = 1
                                for load_idx in island['loads']:
                                    if it == 1:
                                        error_log = error_log + "    Carga: " + self.bpf_net.load.at[load_idx, 'name'] + '\n'
                                    else:
                                        error_log = error_log + "           " + self.bpf_net.load.at[load_idx, 'name'] + '\n'
                            if equipment_type == 'trafo':
                                it = 1
                                for trafo_idx in island['trafo']:
                                    if it == 1:
                                        error_log = error_log + "    Transformador: " + self.bpf_net.trafo.at[trafo_idx, 'name'] + '\n'
                                    else:
                                        error_log = error_log + "                   " + self.bpf_net.trafo.at[trafo_idx, 'name'] + '\n'
                            if equipment_type == 'trafo3w':
                                it = 1
                                for trafo3w_idx in island['trafo3w']:
                                    if it == 1:
                                        error_log = error_log + "    Transformador (3 enrol.): " + self.bpf_net.trafo3w.at[
                                            trafo3w_idx, 'name'] + '\n'
                                    else:
                                        error_log = error_log + "                              " + \
                                                    self.bpf_net.trafo3w.at[
                                                        trafo3w_idx, 'name'] + '\n'
                            if equipment_type == 'buses':
                                it = 1
                                for bus_idx in island['buses']:
                                    if it == 1:
                                        error_log = error_log + "    Barra: " + self.bpf_net.bus.at[bus_idx, 'name'] + '\n'
                                    else:
                                        error_log = error_log + "           " + self.bpf_net.bus.at[
                                            bus_idx, 'name'] + '\n'

                else:
                    error_log = error_log + '\n\nAVISO: verificações ainda não implementadas. Reportar ao desenvolvedor.\n\n'

            return error_log

        if not bool(diag_dict):
            # se nao houver nenhum aviso/erro, roda o fluxo
            try:
                pp.runpp(self.bpf_net)

                powerflow_log = 'RESULTADOS DO FLUXO DE POTÊNCIA ******************************\n\n'
                buses_log_header1 = 'RESULTADOS NAS BARRAS:\n\n'
                buses_log_header2 = f'{"NOME DA BARRA":>20}  ' \
                                    f'{"TENSÃO (p.u.)":>10}  ' \
                                    f'{"POTÊNCIA ATIVA (MW)":>20}  ' \
                                    f'{"POTÊNCIA REATIVA (MVAr)":>20}\n\n'

                buses_log_result = ''
                for index, row in self.bpf_net.res_bus.iterrows():
                    vm_pu = f'{row["vm_pu"]:.4f}'
                    p_mw = f'{row["p_mw"]:.4f}'
                    q_mvar = f'{row["q_mvar"]:.4f}'
                    buses_log_result = buses_log_result + f'{self.bpf_net.bus.at[index, "name"]:>20}  ' \
                                                          f'{vm_pu:>10}  ' \
                                                          f'{p_mw:>20}  ' \
                                                          f'{q_mvar:>20}  ' \
                                                          f'\n'

                powerflow_log = powerflow_log + buses_log_header1 \
                                + buses_log_header2 \
                                + buses_log_result

                return powerflow_log

            except:
                return "Um erro incomum ocorreu. Comunique ao desenvolvedor."
