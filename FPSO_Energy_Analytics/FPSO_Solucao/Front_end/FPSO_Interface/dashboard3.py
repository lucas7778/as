# dependência statsmodels
import threading
import json
import sys

import dash
# import dash_html_components as html
from dash import html
# import dash_core_components as dcc
from dash import dcc
import dash_daq as daq
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objects import Layout
from plotly.validator_cache import ValidatorCache

import webbrowser
from threading import Timer

import pandas as pd
import numpy as np
import datetime as dt

from filterSelection import *


class DashThread(threading.Thread):
    def __init__(self, dataframe, objTransf=None, dataTags=None,  port=8050):
        threading.Thread.__init__(self)
        self.dataframe = dataframe
        self.dataTags = dataTags

        if (self.dataTags is None):
                print('datatags eh none no dash')
        else:
                print('datatags nao eh none no dash')

        self.objTransf=objTransf
        self.port = port
        self.daemon = True

    def getEixoName(self,tagName):
        if self.dataTags is None:
            return tagName
        else:
            unidade = self.dataTags.loc[self.dataTags['tag'] == tagName, 'engunits']
            texto = tagName + ' (' + unidade.iloc[0] + ')'
        return texto

    def format_date(self,df):
        df = df.replace('Bad', 0)

        # remove hora e formata data para padrao americano
        for i in range(df.shape[0]):

            original = str(df.loc[i, 'index']).split()
            date = original[0]
            try:
                date = date.split('/')
                date = f'{date[1]}/{date[0]}/{date[2]} {original[1]}'
            except Exception as e:
                date = str(date[0]).split('-')
                date = f'{date[1]}/{date[2]}/{date[0]} {original[1]}'

            df.loc[i, 'index'] = pd.to_datetime(date)
        df['Mês'] = pd.to_datetime(df['index']).dt.strftime('%m/%Y')
        df['Semana'] = pd.to_datetime(df['index']).dt.strftime('%W-%Y')
        return df

    def create_col_list(self, df):
        df_col = list(df.columns.values)
        df_col.remove('index')
        df_col.remove('Mês')
        df_col.remove('Semana')
        return df_col

    def open_browser(self):
        webbrowser.open_new("http://localhost:{}".format(self.port))

    def fatorIntermitencia(df, coluna, limiar):
        D = df[df[coluna] < limiar][coluna].count()
        T = df[coluna].count()
        L = T-D
        listX = ['desligado', 'ligado']
        listY = [D, L]
        fator = (T - D) / T
        return listX, listY, fator

    def run(self):
        app = dash.Dash(__name__)
        global df
        df = self.format_date(self.dataframe)
        df_col = self.create_col_list(df)

        app.layout = html.Div([

            html.Div([
                html.Div([
                    html.H1('FPSO Power Demand Analytics', className='titlename'),
                    html.Img(src=app.get_asset_url("petro2.png"), className='logo')
                ], id='title-logo'),
                html.Hr(className='hr-logo'),
                html.H2('Analisar Dados Históricos', id='menu-title'),
            ], id='menu-header'),

            html.Div([
                html.Div([
                    html.Div([
                        dcc.Graph(id='box-plot'),
                        dcc.RangeSlider(id='slider_boxplot', allowCross=False, dots=True, min=0,
                                        max=len(df['Mês'].unique()) - 1, value=[0, len(df['Mês'].unique()) - 1],
                                        className='slider-w'),
                        html.Div([
                            html.Div([
                                html.H3('Eixo X:'),
                                dcc.RadioItems(id='radio_boxplot',
                                                options=[{'value': x, 'label': x} for x in ['Mês', 'Semana']],
                                                value='Mês'),
                            ]),

                            html.Div([
                                html.H3('Eixo Y:'),
                                dcc.Dropdown(id='dropdown_boxplot',
                                            options=[{'label': i, 'value': i} for i in df_col[:]],
                                            placeholder='Selecione uma coluna',
                                            style=dict(width='100%'), value=df_col[0])
                            ])
                        ], className='box-values'),
                        html.Div([
                            html.Div([
                                html.H3('Percentil:'),
                                daq.NumericInput(min=0, max=100, value=90, id='num-percentil')
                            ]),
                            html.Div([
                                html.H3("Resultado:"),
                                html.Div(id='percentil-output')
                            ])
                        ], className='box-values')
                    ], className='divgrid'),

                    html.Div([
                        html.Div([
                            dcc.Graph(id='esp')
                        ], id='slidergraph'),
                        html.Div([
                            html.Div([
                                html.H3('Eixo X:'),
                                dcc.Dropdown(id='dropdownx_esp',
                                            options=[{'label': i, 'value': i} for i in df_col[:]],
                                            placeholder='Selecione uma coluna',
                                            style=dict(width='100%'), value=df_col[0])
                            ]),
                            html.Div([
                                html.H3('Eixo Y:'),
                                dcc.Dropdown(id='dropdowny_esp',
                                            options=[{'label': i, 'value': i} for i in df_col[:]],
                                            placeholder='Selecione uma coluna',
                                            style=dict(width='100%'), value=df_col[1]),
                            ])
                        ], className='box-values'),

                        html.Div([
                            html.H3('Desvio Padrão de Tolerância:'),
                            dcc.Slider(id='slider_dp_esp', min=1, max=4, value=4,
                                    marks={1: '1', 2: '2', 3: '3', 4: 'Inf'}),
                            dcc.Checklist(id='checkbox_esp',
                                        options=[
                                            {'label': 'Adicionar Reta de Regressão Linear', 'value': 'selected'}])
                        ], id='esp-values')

                    ], className='divgrid')
                ], className='content'),


                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Graph(id='line')
                        ]),
                        html.Div([
                            html.Div([
                                html.H3('Coluna:'),
                                dcc.Dropdown(id='dropdown_line', options=[{'label': i, 'value': i} for i in df_col[:]],
                                             placeholder='Selecione colunas',
                                             style=dict(width='100%'), value=df_col[0], multi=True)
                            ])
                        ], className='box-values')

                    ], className='divgrid'),

                    html.Div([
                        html.Div([
                            dcc.Graph(id='heatmap')
                        ]),

                        html.Div([
                            html.Div([
                                html.H3('Coluna:'),
                                dcc.Dropdown(id='dropdown_heatmap', options=[{'label': i, 'value': i} for i in df_col[:]],
                                             placeholder='Selecione uma coluna',
                                             style=dict(width='100%'), value=df_col[0])
                            ]),
                            html.Div([
                                html.H3('Mês:'),
                                dcc.Dropdown(id='dropdownm_heatmap',
                                             options=[{'label': x, 'value': x} for x in df['Mês'].unique()],
                                             placeholder='Selecione um mês',
                                             style=dict(width='100%'), value=df['Mês'].unique()[0])

                            ])
                        ], className='box-values')
                    ], className='divgrid')
                ], className='content'),

                html.Div(
                    html.H3('Análise do Fator de Intermitência:'),
                    className='h3-header'
                ),

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Graph(id='histogram')
                        ]),
                        html.Div([
                            html.Div([
                                html.H3('Colunas:'),
                                dcc.Dropdown(id='dropdown_histogram', options=[{'label': i, 'value': i} for i in df_col[:]],
                                             placeholder='Selecione colunas',
                                             style=dict(width='100%'), value=df_col[0], multi=True)
                            ]),
                            html.Div([
                                html.H3('Quantidade de Barras:'),
                                daq.NumericInput(id='numeric_histogram', min=0, max=20, value=0),

                                html.H3('Limiar de Operação:'),
                                daq.NumericInput(id='numeric_bar-fit', min=0, max=999999, value=1, size=100)
                            ])
                        ], className='box-values')

                    ], className='divgrid'),

                    html.Div([
                        html.Div([
                            dcc.Graph(id='bar-fit')
                        ]),
                        html.Div([
                            html.Div([
                                html.H3('Fator de Intermitência:'),
                                html.P(id='hist-fc')
                            ])
                        ], className='box-values')

                    ], className='divgrid')

                ], className='content'),

                html.Div(
                    html.H3('Análise do Fator de Carga:'),
                    className='h3-header'
                ),

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Graph(id='esp2')
                        ], id='slidergraph2'),

                        html.Div([
                            html.Div([
                                html.H3('Eixo X:'),
                                dcc.Dropdown(id='dropdownx_esp2',
                                            options=[{'label': i, 'value': i} for i in df_col[:]],
                                            placeholder='Selecione uma coluna',
                                            style=dict(width='100%'), value=df_col[0])
                            ]),
                            html.Div([
                                html.H3('Eixo Y:'),
                                dcc.Dropdown(id='dropdowny_esp2',
                                            options=[{'label': i, 'value': i} for i in df_col[:]],
                                            placeholder='Selecione uma coluna',
                                            style=dict(width='100%'), value=df_col[1]),
                            ])
                        ], className='box-values'),

                    ], className='divgrid'),

                    html.Div([
                        dcc.Graph(id='box-plot2'),
                        html.Div([
                            html.Div([
                                html.H3('Percentil:'),
                                daq.NumericInput(min=0, max=100, value=90, id='num-percentil2')
                            ]),
                            html.Div([
                                html.H3("Resultado:"),
                                html.Div(id='percentil-output2')
                            ])
                        ], className='box-values')
                    ], className='divgrid')
                ], className='content'),

                html.Div([
                    html.Div([
                        html.Div([
                            dcc.Graph(id='histogram2')
                        ]),
                        html.Div([
                            html.Div([
                                html.H3('Quantidade de Barras:'),
                                daq.NumericInput(id='numeric_histogram2', min=0, max=20, value=0),
                                html.H3('Potência Dimensionante:'),
                                dcc.RadioItems(options=[{'label':'Automático', 'value': 0}, {'label':'Personalizado', 'value':1}], value=0, id='radio_pd'),
                                daq.NumericInput(id='numeric_pd', min=0, max=999999, value=0, size=100)
                            ]),
                            html.Div([
                                daq.BooleanSwitch(
                                    label="Normalizar:",
                                    id='bool-fc'
                                ),
                                html.H3('Estimativa do Fator de Carga:'),
                                html.P(id='hist-fc2')
                            ]),
                        ], className='box-values'),

                    ], className='divgrid')

                ], className='content-1'),

            ], id='content-main'),

        ], id='main-window')

        @app.callback(
            [Output('box-plot', 'figure'),
             Output('slider_boxplot', 'max'),
             Output('slider_boxplot', 'marks'),
             Output('percentil-output', 'children')
             ],
            [Input('radio_boxplot', 'value'),
             Input('slider_boxplot', 'value'),
             Input('dropdown_boxplot', 'value'),
             Input('num-percentil', 'value')])
        def update_boxplot(rvalue, svalue, dpvalue, pvalue):
            bp_df = df.loc[:, [rvalue, dpvalue]]

            smax = len(bp_df[rvalue].unique()) - 1
            selected_values = bp_df[rvalue].unique()[svalue[0]:svalue[1] + 1]
            bp_df = bp_df.loc[bp_df[rvalue].isin(selected_values)]

            plabel = []
            for j in range(len(selected_values)):
                bptrab = bp_df.loc[bp_df[str(rvalue)] == selected_values[j]]

                bptrab = bptrab[dpvalue].dropna()
                bptrab = list(bptrab)
                bptrab = sorted(bptrab)

                for i in range(len(bptrab)):
                    if i == round((pvalue/100) * len(bptrab), 0):
                        plabel.append(bptrab[i])
                        break
                    elif pvalue == 100:
                        plabel.append(bptrab[-1])
                        break
            temp = ''
            for k in range(len(plabel)):
                temp += f'\n{selected_values[k]}:{plabel[k]}\n'

            eixos={rvalue:rvalue, dpvalue:self.getEixoName(dpvalue)}
            boxplot = px.box(bp_df, title='Box Plot', x=rvalue, y=dpvalue, labels=eixos)
            bp_marks = {svalue[0]: {'label': selected_values[0]},
                        svalue[1]: {'label': selected_values[len(selected_values) - 1]}}

            return boxplot, smax, bp_marks, temp


        @app.callback(
            Output('esp', 'figure'),
            [Input('esp', 'relayoutData'),
             Input('checkbox_esp', 'value'),
             Input('slider_dp_esp', 'value'),
             Input('dropdownx_esp', 'value'),
             Input('dropdowny_esp', 'value')]
        )
        def update_esp01(zoomdata, cvalue, dpvalue, xvalue, yvalue):
            esp_df = df.loc[:, [xvalue, yvalue]]

            try:
                esp_df = esp_df.loc[esp_df[xvalue] <= zoomdata['xaxis.range[1]']]
                esp_df = esp_df.loc[esp_df[xvalue] >= zoomdata['xaxis.range[0]']]

                esp_df = esp_df.loc[esp_df[yvalue] <= zoomdata['yaxis.range[1]']]
                esp_df = esp_df.loc[esp_df[yvalue] >= zoomdata['yaxis.range[0]']]
            except Exception as e:
                # print(type(e).__name__)
                pass

            if dpvalue <= 3:
                dpx = esp_df[xvalue].std()
                esp_df = esp_df.loc[esp_df[xvalue] <= esp_df[xvalue].mean() + dpvalue * dpx]
                esp_df = esp_df.loc[esp_df[xvalue] >= esp_df[xvalue].mean() - dpvalue * dpx]

                dpy = esp_df[yvalue].std()
                esp_df = esp_df.loc[esp_df[yvalue] <= esp_df[yvalue].mean() + dpvalue * dpy]
                esp_df = esp_df.loc[esp_df[yvalue] >= esp_df[yvalue].mean() - dpvalue * dpy]

            eixos = {xvalue: self.getEixoName(xvalue), yvalue: self.getEixoName(yvalue)}
            if cvalue is None or cvalue == []:
                esp = px.scatter(esp_df, title='Dispersão', x=xvalue, y=yvalue, labels=eixos)
            else:
                esp = px.scatter(esp_df, title='Dispersão', x=xvalue, y=yvalue, labels=eixos, trendline='ols',
                                 trendline_color_override="red")

            return esp

        @app.callback(
            Output('heatmap', 'figure'),
            [Input('dropdownm_heatmap', 'value'),
             Input('dropdown_heatmap', 'value')])
        def update_heatmap(mes, col):
            heat_df = df.loc[:, ['index', col, 'Mês']]
            heat_df['Hora'] = pd.to_datetime(heat_df['index']).dt.strftime('%H:%M')
            heat_df['Dia'] = pd.to_datetime(heat_df['index']).dt.strftime('%d')
            heat_df = heat_df.loc[heat_df['Mês'] == mes]
            heat_x = heat_df['Dia'].unique()
            heat_y = heat_df['Hora'].unique()
            heat_df = heat_df.loc[:, ['Dia', 'Hora', col]]
            heat_df = heat_df.pivot('Hora', 'Dia', col)

            heat = go.Figure(data=go.Heatmap(x=heat_x, y=heat_y, z=heat_df, xgap=1,ygap=1, colorscale = 'Jet'))
            '''
            This is the list of Plotly colorscales:
            [‘Blackbody’,‘Bluered’, ‘Blues’, ‘Earth’, ‘Electric’, ‘Greens’, ‘Greys’, ‘Hot’, ‘Jet’, ‘
            Picnic’, ‘Portland’, ‘Rainbow’,‘RdBu’, ‘Reds’, ‘Viridis’, ‘YlGnBu’, ‘YlOrRd’]
            The default colorscale is ‘RdBu’.
            '''
            heat.update_layout(
                title='Mapa de Calor',
                xaxis=go.layout.XAxis(title='Dia'), yaxis=go.layout.YAxis(title='Hora')
                #template='none'
            )
            # heat = px.imshow(heat_df, title='Mapa de Calor')
            return heat

        @app.callback(
            Output('histogram', 'figure'),
            [Input('dropdown_histogram', 'value'),
             Input('numeric_histogram', 'value')])
        def update_histogram(hvalue, nbar):
            hist_df = df.loc[:, hvalue]
            #eixos = {hvalue: self.getEixoName(hvalue)}
            hist = px.histogram(hist_df, x=hvalue, nbins=nbar, barmode='group',title='Histograma')#,marginal='box'
            hist.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.5,
                bgcolor='rgba(0,0,0,0)'))

            return hist

        @app.callback(
            [Output('bar-fit', 'figure'),
             Output('hist-fc', 'children')],
            [Input('dropdown_histogram', 'value'),
             Input('numeric_bar-fit', 'value')])
        def update_bar(xvalue, dim):
            if type(xvalue) is list:
                xvalue = xvalue[0]
            bar_df = df.loc[:, xvalue]
            D = bar_df[bar_df < dim].count()
            T = bar_df.count()
            L = (T - D)
            FI = L / T
            dfStatus = pd.DataFrame({'status':['Desligado','Ligado'],'ocorrências':[D,L]})
            #bar = px.bar(x=['Desligado', 'Ligado'], y=[D, L], labels={'x':'', 'y':'Ocorrências'},color=['Desligado', 'Ligado'], color_discrete_map={
        #'Desligado': 'red',
        #'Ligado': 'blue'
            bar = px.bar(dfStatus, x='status', y='ocorrências', labels={'x': '', 'y': 'Ocorrências'}, color='status', title='Operação')
                         #color=['Desligado', 'Ligado']
    #})

            return bar, FI

        @app.callback(
            [Output('box-plot2', 'figure'),
             Output('percentil-output2', 'children')
            ],
             [Input('esp2', 'selectedData'),  # this triggers the event
             Input('dropdownx_esp2', 'value'),
             Input('dropdowny_esp2', 'value'),
             Input('num-percentil2', 'value')])
        def graph_event(selected_data, xvalue, yvalue, pvalue):
            bp_df = df.copy()
            bp_df = df.loc[:, [xvalue, yvalue]]
            try:

                bp_df = bp_df.loc[bp_df[xvalue] <= selected_data['range']['x'][1]]
                bp_df = bp_df.loc[bp_df[xvalue] >= selected_data['range']['x'][0]]

                bp_df = bp_df.loc[bp_df[yvalue] <= selected_data['range']['y'][1]]
                bp_df = bp_df.loc[bp_df[yvalue] >= selected_data['range']['y'][0]]

                xmin=selected_data['range']['x'][0]
                xmax=selected_data['range']['x'][1]
                ymin=selected_data['range']['y'][0]
                ymax=selected_data['range']['y'][1]
                coord=[xmin,xmax,ymin,ymax]
                if self.objTransf != None:
                    self.objTransf.setCoord(coord, xvalue, yvalue)
                    print('dash do main')
                else:
                    print('dash do eqp')

            except Exception as e:
                # print(type(e).__name__)
                pass
            # já existe um método do pandas para calcular o percentil customizado
            # plabel=bp_df[yvalue].quantile(pvalue / 100)


            bptrab = bp_df[yvalue].dropna()
            bptrab = list(bptrab)
            bptrab = sorted(bptrab)

            plabel = ''
            for i in range(len(bptrab)):
                if i == round((pvalue / 100) * len(bptrab), 0):
                    plabel = bptrab[i]
                    break
                elif pvalue == 100:
                    plabel = (bptrab[-1])
                    break
            eixos = {yvalue: self.getEixoName(yvalue)}
            boxplot = px.box(bp_df, title='Box Plot', y=yvalue, labels=eixos)

            return boxplot, plabel

        @app.callback(
            Output('esp2', 'figure'),
            [Input('dropdownx_esp2', 'value'),
             Input('dropdowny_esp2', 'value')])
        def update_esp02(xvalue, yvalue):
            esp_df = df.copy()
            esp_df = df.loc[:, [xvalue, yvalue]]

            eixos = {xvalue: self.getEixoName(xvalue), yvalue: self.getEixoName(yvalue)}
            esp = px.scatter(esp_df, title='Dispersão', x=xvalue, y=yvalue, labels=eixos)

            return esp

        @app.callback(
            Output('line', 'figure'),
            Input('dropdown_line', 'value'))
        def update_line(yvalue):
            line_df = df.copy()
            colunas = ["index"]
            if type(yvalue) is str:
                colunas.append(yvalue)
            elif type(yvalue) is list:
                colunas.extend(yvalue)

            #colunas=['index', yvalue]
            line_df = line_df.loc[:, colunas]


            line = px.line(line_df, x='index', y=line_df.columns[1:], title='Lineplot')

            line.update_layout(legend=dict(
                yanchor="top",
                y=0.99,
                xanchor="left",
                x=0.5,
                bgcolor='rgba(0,0,0,0)'))

            return line

        @app.callback(
            [Output('histogram2', 'figure'),
             Output('hist-fc2', 'children'),
             Output('numeric_pd', 'disabled')],
            [Input('esp2', 'selectedData'),  # this triggers the event
             Input('dropdownx_esp2', 'value'),
             Input('dropdowny_esp2', 'value'),
             Input('numeric_histogram2', 'value'),
             Input('bool-fc', 'on'),
             Input('radio_pd', 'value'),
             Input('numeric_pd', 'value')])
        def graph_event(selected_data, xvalue, yvalue, nbar, norm, rvalue, npd):
            hist2_df = df.copy()
            hist2_df = df.loc[:, [xvalue, yvalue]]
            try:

                hist2_df = hist2_df.loc[hist2_df[xvalue] <= selected_data['range']['x'][1]]
                hist2_df = hist2_df.loc[hist2_df[xvalue] >= selected_data['range']['x'][0]]

                hist2_df = hist2_df.loc[hist2_df[yvalue] <= selected_data['range']['y'][1]]
                hist2_df = hist2_df.loc[hist2_df[yvalue] >= selected_data['range']['y'][0]]

            except Exception as e:
                # print(type(e).__name__)
                pass

            #### Cálculo do Fator de Carga, a partir de uma seleção
            maximo = hist2_df[yvalue].max()
            minimo = hist2_df[yvalue].min()
            if rvalue == 0:
                dvalue = True
                maximo = hist2_df[yvalue].max()

            else:
                dvalue = False
                if npd != 0:
                    maximo = npd
                if npd < minimo:
                    npd = minimo

            w = (maximo-minimo)/nbar
            media = hist2_df[yvalue].mean()
            FC = media/maximo
            hist2_df['normalizado'] = hist2_df[yvalue]/maximo
            if norm is True:
                hist2 = px.histogram(hist2_df, x='normalizado', nbins=nbar, title='Histograma', histnorm='percent',cumulative=True)#,marginal='box'
                                     #nbins=nbar,
                hist2.update_traces(xbins=dict(  # bins used for histogram
                    start=minimo/maximo,
                    end=1,
                    size=(1-minimo/maximo)/nbar
                ))

            else:
                eixos = {xvalue: self.getEixoName(yvalue)}
                hist2 = px.histogram(hist2_df, x=yvalue, nbins=nbar, title='Histograma', histnorm='percent')#, marginal='box'

                hist2.update_traces(xbins=dict(  # bins used for histogram
                    start=minimo,
                    end=maximo,
                    size=(maximo-minimo) / nbar
                ))

                #b=[x/maximo for x in hist2_df[yvalue]]
                #hist2_df[yvalue]=b
                #hist2_df[yvalue] = hist2_df[yvalue]/maximo

            
            #hist2 = px.histogram(hist2_df, x=yvalue, nbins=nbar, title='Histograma') #barmode='group',
            hist2.update_layout(legend=dict(
                yanchor="top",
                xanchor="left",
                x=0.5,
                bgcolor='rgba(0,0,0,0)'))

            
            return hist2, FC, dvalue

        Timer(1, self.open_browser).start()
        app.run_server(debug=False, port=self.port)

class Porta:
    def __init__(self):
        self.porta = 8085
    def proxima(self):
        self.porta=self.porta+1
    def getPorta(self):
        return self.porta

