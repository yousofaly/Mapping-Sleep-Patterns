{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "        <script type=\"text/javascript\">\n",
       "        window.PlotlyConfig = {MathJaxConfig: 'local'};\n",
       "        if (window.MathJax) {MathJax.Hub.Config({SVG: {font: \"STIX-Web\"}});}\n",
       "        if (typeof require !== 'undefined') {\n",
       "        require.undef(\"plotly\");\n",
       "        requirejs.config({\n",
       "            paths: {\n",
       "                'plotly': ['https://cdn.plot.ly/plotly-latest.min']\n",
       "            }\n",
       "        });\n",
       "        require(['plotly'], function(Plotly) {\n",
       "            window._Plotly = Plotly;\n",
       "        });\n",
       "        }\n",
       "        </script>\n",
       "        "
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib as mpl\n",
    "import matplotlib.pyplot as plt\n",
    "plt.style.use('ggplot')\n",
    "\n",
    "#!pip install plotly\n",
    "#!pip install chart_studio\n",
    "#!pip install cufflinks\n",
    "import chart_studio.plotly as py\n",
    "import plotly.graph_objs as go\n",
    "from plotly.offline import iplot, init_notebook_mode\n",
    "import cufflinks\n",
    "cufflinks.go_offline(connected = True)\n",
    "init_notebook_mode(connected = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "files = ('0418.csv','0518.csv','0618.csv','0718.csv','0818.csv','0918.csv','1018.csv','1118.csv','1218.csv','0119.csv','0219.csv','0319.csv','0419.csv','0519.csv','0619.csv','0719.csv','0819.csv','0919.csv','1019.csv','1119.csv','1219.csv','0120.csv')\n",
    "df = pd.DataFrame()\n",
    "for file in files:\n",
    "    df_month = pd.read_csv(file)\n",
    "    df = pd.concat([df,df_month])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['timestamp', 'Activity', 'Duration (min)', 'Quantity', 'Caregiver']\n",
      "(5802, 4)\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Activity</th>\n",
       "      <th>minutes</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Room</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>timestamp</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2018-04-04 09:00:00</th>\n",
       "      <td>Sign In</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 09:05:00</th>\n",
       "      <td>Diaper</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 09:20:00</th>\n",
       "      <td>Bottle</td>\n",
       "      <td>NaN</td>\n",
       "      <td>4.0</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 09:38:00</th>\n",
       "      <td>Photo</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 09:39:00</th>\n",
       "      <td>Sleep</td>\n",
       "      <td>22.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Activity  minutes  Quantity      Room\n",
       "timestamp                                                \n",
       "2018-04-04 09:00:00  Sign In      NaN       NaN  Infant E\n",
       "2018-04-04 09:05:00   Diaper      NaN       NaN  Infant E\n",
       "2018-04-04 09:20:00   Bottle      NaN       4.0  Infant E\n",
       "2018-04-04 09:38:00    Photo      NaN       NaN  Infant E\n",
       "2018-04-04 09:39:00    Sleep     22.0       NaN  Infant E"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = df[['Start Time','Activity','Duration (min)','Quantity','Caregiver']]\n",
    "df['timestamp'] = pd.to_datetime(df['Start Time'])\n",
    "cols = df.columns.tolist()\n",
    "cols = cols[-1:] + cols [1:5]\n",
    "print(cols)\n",
    "df = df[cols]\n",
    "df.rename(columns = {'Duration (min)' : 'minutes', 'Caregiver' : 'Room'}, inplace = True)\n",
    "df.set_index('timestamp', inplace = True)\n",
    "df.sort_index(inplace = True)\n",
    "print (df.shape)\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_sleep = df[df['Activity'] == 'Sleep']\n",
    "df_sleep = df_sleep[df_sleep['minutes'] < 200]\n",
    "#df_sleep.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "//anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:5: FutureWarning:\n",
      "\n",
      "how in .resample() is deprecated\n",
      "the new syntax is .resample(...)..apply(<func>)\n",
      "\n"
     ]
    },
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "Month=%{x}<br>minutes=%{y}",
         "legendgroup": "",
         "marker": {
          "color": "#636efa"
         },
         "name": "",
         "notched": false,
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": false,
         "type": "box",
         "x": [
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-04",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-05",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-06",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-07",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-08",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-09",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-10",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-11",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2018-12",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-01",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-02",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-03",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-04",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-05",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-06",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-07",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-08",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-09",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-10",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-11",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2019-12",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01",
          "2020-01"
         ],
         "x0": " ",
         "xaxis": "x",
         "y": [
          127,
          190,
          96,
          126,
          57,
          138,
          178,
          130,
          119,
          92,
          82,
          130,
          108,
          103,
          79,
          126,
          65,
          132,
          62,
          59,
          80,
          134,
          84,
          41,
          148,
          106,
          164,
          70,
          115,
          119,
          121,
          57,
          136,
          125,
          83,
          105,
          124,
          79,
          95,
          70,
          65,
          119,
          149,
          123,
          50,
          162,
          82,
          132,
          110,
          170,
          104,
          85,
          174,
          151,
          130,
          126,
          112,
          61,
          72,
          64,
          105,
          67,
          114,
          121,
          100,
          84,
          92,
          87,
          79,
          55,
          65,
          72,
          126,
          95,
          100,
          88,
          73,
          81,
          20,
          129,
          100,
          74,
          91,
          56,
          47,
          91,
          66,
          79,
          63,
          38,
          75,
          74,
          33,
          29,
          62,
          87,
          32,
          23,
          32,
          63,
          45,
          62,
          59,
          41,
          61,
          34,
          29,
          52,
          6,
          47,
          112,
          43,
          44,
          28,
          92,
          33,
          34,
          44,
          41,
          60,
          36,
          25,
          46,
          49,
          110,
          41,
          29,
          30,
          24,
          35,
          34,
          24,
          50,
          29,
          39,
          29,
          9,
          30,
          34,
          25,
          41,
          25,
          48,
          29,
          56,
          72,
          35,
          96,
          104,
          87,
          47,
          117,
          72,
          46,
          93,
          65,
          26,
          89,
          78,
          99,
          90,
          59,
          54,
          33,
          63,
          88,
          108,
          99,
          32,
          69,
          40,
          92,
          86,
          85,
          84,
          113,
          58,
          95,
          81,
          69,
          51,
          45,
          79,
          74,
          116,
          95,
          77,
          89,
          83,
          84,
          66,
          65,
          70,
          56,
          71,
          92,
          74,
          58,
          85,
          64,
          92,
          132,
          83,
          64,
          115,
          103,
          70,
          104,
          107,
          101,
          89,
          74,
          78,
          92,
          76,
          111,
          87,
          63,
          99,
          68,
          91,
          75,
          131,
          96,
          109,
          106,
          77,
          123,
          80,
          110,
          92,
          108,
          107,
          67,
          63,
          116,
          113,
          81,
          111,
          113,
          119,
          98,
          112,
          122,
          64,
          123,
          117,
          104,
          87,
          107,
          76,
          116,
          113,
          77,
          101,
          105,
          88,
          97,
          110,
          107,
          116,
          100,
          101,
          102,
          92,
          103,
          97,
          134,
          101,
          102,
          103,
          90,
          100,
          96,
          107,
          81,
          113,
          97,
          98,
          90,
          99,
          87,
          99,
          85,
          88,
          104,
          104,
          81,
          102,
          92,
          94,
          114,
          119,
          75,
          99,
          105,
          98,
          89,
          83,
          104,
          90,
          81,
          74,
          114,
          129,
          98,
          105,
          82,
          87,
          116,
          106,
          110,
          128,
          84,
          113,
          96,
          129,
          109,
          94,
          116,
          78,
          92,
          89,
          102,
          124,
          100,
          131,
          107,
          151,
          133,
          95,
          118,
          102,
          111,
          128,
          106,
          122,
          111,
          86,
          112,
          99,
          115,
          88,
          96,
          137,
          117,
          118,
          83,
          107,
          109,
          106,
          112,
          125,
          102,
          119,
          94,
          117,
          76,
          111,
          99,
          94,
          115,
          103,
          94
         ],
         "y0": " ",
         "yaxis": "y"
        }
       ],
       "layout": {
        "boxmode": "group",
        "height": 750,
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Monthly Nap Trends"
        },
        "width": 1000,
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Month"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "minutes"
         }
        }
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"e3e3174a-cfe1-46d0-9ff6-67d2738a91ec\" class=\"plotly-graph-div\" style=\"height:750px; width:1000px;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    \n",
       "                if (document.getElementById(\"e3e3174a-cfe1-46d0-9ff6-67d2738a91ec\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        'e3e3174a-cfe1-46d0-9ff6-67d2738a91ec',\n",
       "                        [{\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"Month=%{x}<br>minutes=%{y}\", \"legendgroup\": \"\", \"marker\": {\"color\": \"#636efa\"}, \"name\": \"\", \"notched\": false, \"offsetgroup\": \"\", \"orientation\": \"v\", \"showlegend\": false, \"type\": \"box\", \"x\": [\"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-04\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-05\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-06\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-07\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-08\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-09\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-10\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-11\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2018-12\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-01\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-02\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-03\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-04\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-05\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-06\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-07\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-08\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-09\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-10\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-11\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2019-12\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\", \"2020-01\"], \"x0\": \" \", \"xaxis\": \"x\", \"y\": [127.0, 190.0, 96.0, 126.0, 57.0, 138.0, 178.0, 130.0, 119.0, 92.0, 82.0, 130.0, 108.0, 103.0, 79.0, 126.0, 65.0, 132.0, 62.0, 59.0, 80.0, 134.0, 84.0, 41.0, 148.0, 106.0, 164.0, 70.0, 115.0, 119.0, 121.0, 57.0, 136.0, 125.0, 83.0, 105.0, 124.0, 79.0, 95.0, 70.0, 65.0, 119.0, 149.0, 123.0, 50.0, 162.0, 82.0, 132.0, 110.0, 170.0, 104.0, 85.0, 174.0, 151.0, 130.0, 126.0, 112.0, 61.0, 72.0, 64.0, 105.0, 67.0, 114.0, 121.0, 100.0, 84.0, 92.0, 87.0, 79.0, 55.0, 65.0, 72.0, 126.0, 95.0, 100.0, 88.0, 73.0, 81.0, 20.0, 129.0, 100.0, 74.0, 91.0, 56.0, 47.0, 91.0, 66.0, 79.0, 63.0, 38.0, 75.0, 74.0, 33.0, 29.0, 62.0, 87.0, 32.0, 23.0, 32.0, 63.0, 45.0, 62.0, 59.0, 41.0, 61.0, 34.0, 29.0, 52.0, 6.0, 47.0, 112.0, 43.0, 44.0, 28.0, 92.0, 33.0, 34.0, 44.0, 41.0, 60.0, 36.0, 25.0, 46.0, 49.0, 110.0, 41.0, 29.0, 30.0, 24.0, 35.0, 34.0, 24.0, 50.0, 29.0, 39.0, 29.0, 9.0, 30.0, 34.0, 25.0, 41.0, 25.0, 48.0, 29.0, 56.0, 72.0, 35.0, 96.0, 104.0, 87.0, 47.0, 117.0, 72.0, 46.0, 93.0, 65.0, 26.0, 89.0, 78.0, 99.0, 90.0, 59.0, 54.0, 33.0, 63.0, 88.0, 108.0, 99.0, 32.0, 69.0, 40.0, 92.0, 86.0, 85.0, 84.0, 113.0, 58.0, 95.0, 81.0, 69.0, 51.0, 45.0, 79.0, 74.0, 116.0, 95.0, 77.0, 89.0, 83.0, 84.0, 66.0, 65.0, 70.0, 56.0, 71.0, 92.0, 74.0, 58.0, 85.0, 64.0, 92.0, 132.0, 83.0, 64.0, 115.0, 103.0, 70.0, 104.0, 107.0, 101.0, 89.0, 74.0, 78.0, 92.0, 76.0, 111.0, 87.0, 63.0, 99.0, 68.0, 91.0, 75.0, 131.0, 96.0, 109.0, 106.0, 77.0, 123.0, 80.0, 110.0, 92.0, 108.0, 107.0, 67.0, 63.0, 116.0, 113.0, 81.0, 111.0, 113.0, 119.0, 98.0, 112.0, 122.0, 64.0, 123.0, 117.0, 104.0, 87.0, 107.0, 76.0, 116.0, 113.0, 77.0, 101.0, 105.0, 88.0, 97.0, 110.0, 107.0, 116.0, 100.0, 101.0, 102.0, 92.0, 103.0, 97.0, 134.0, 101.0, 102.0, 103.0, 90.0, 100.0, 96.0, 107.0, 81.0, 113.0, 97.0, 98.0, 90.0, 99.0, 87.0, 99.0, 85.0, 88.0, 104.0, 104.0, 81.0, 102.0, 92.0, 94.0, 114.0, 119.0, 75.0, 99.0, 105.0, 98.0, 89.0, 83.0, 104.0, 90.0, 81.0, 74.0, 114.0, 129.0, 98.0, 105.0, 82.0, 87.0, 116.0, 106.0, 110.0, 128.0, 84.0, 113.0, 96.0, 129.0, 109.0, 94.0, 116.0, 78.0, 92.0, 89.0, 102.0, 124.0, 100.0, 131.0, 107.0, 151.0, 133.0, 95.0, 118.0, 102.0, 111.0, 128.0, 106.0, 122.0, 111.0, 86.0, 112.0, 99.0, 115.0, 88.0, 96.0, 137.0, 117.0, 118.0, 83.0, 107.0, 109.0, 106.0, 112.0, 125.0, 102.0, 119.0, 94.0, 117.0, 76.0, 111.0, 99.0, 94.0, 115.0, 103.0, 94.0], \"y0\": \" \", \"yaxis\": \"y\"}],\n",
       "                        {\"boxmode\": \"group\", \"height\": 750, \"legend\": {\"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"Monthly Nap Trends\"}, \"width\": 1000, \"xaxis\": {\"anchor\": \"y\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"Month\"}}, \"yaxis\": {\"anchor\": \"x\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"minutes\"}}},\n",
       "                        {\"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('e3e3174a-cfe1-46d0-9ff6-67d2738a91ec');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#import plotly express \n",
    "import plotly.express as px\n",
    "\n",
    "#daily total and remove incorrect entries and days with no sleep (no school)\n",
    "df_sleep_daily = df_sleep.resample('d', how = np.sum)\n",
    "df_sleep_daily = df_sleep_daily[(df_sleep_daily['minutes'] > 0)]\n",
    "#assign each row month of the year\n",
    "df_sleep_daily['Month'] = df_sleep_daily.index.to_period ('M')\n",
    "df_sleep_daily['Month'] = df_sleep_daily['Month'].astype(str)\n",
    "fig = px.box(df_sleep_daily, x=\"Month\", y=\"minutes\", width = 1000, height =750)\n",
    "fig.update_layout(title = 'Monthly Nap Trends')\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How do daily sleep patterns look? A stacked bar chart showing total naps for each day will allow for visualization of both total nap time and pattern."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Activity</th>\n",
       "      <th>minutes</th>\n",
       "      <th>Quantity</th>\n",
       "      <th>Room</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>timestamp</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2018-04-04 09:39:00</th>\n",
       "      <td>Sleep1</td>\n",
       "      <td>22.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 10:13:00</th>\n",
       "      <td>Sleep2</td>\n",
       "      <td>19.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 11:07:00</th>\n",
       "      <td>Sleep3</td>\n",
       "      <td>13.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 12:38:00</th>\n",
       "      <td>Sleep4</td>\n",
       "      <td>22.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018-04-04 14:46:00</th>\n",
       "      <td>Sleep5</td>\n",
       "      <td>51.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Infant E</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                    Activity  minutes  Quantity      Room\n",
       "timestamp                                                \n",
       "2018-04-04 09:39:00   Sleep1     22.0       NaN  Infant E\n",
       "2018-04-04 10:13:00   Sleep2     19.0       NaN  Infant E\n",
       "2018-04-04 11:07:00   Sleep3     13.0       NaN  Infant E\n",
       "2018-04-04 12:38:00   Sleep4     22.0       NaN  Infant E\n",
       "2018-04-04 14:46:00   Sleep5     51.0       NaN  Infant E"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#cumulative count of naps per day\n",
    "c = df_sleep.groupby([\"Activity\",df_sleep.index.date]).cumcount() + 1\n",
    "c = c.replace(0, '').astype(str)\n",
    "c.head(10)\n",
    "df_sleep[\"Activity\"] += c\n",
    "df_sleep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "Activity=Sleep1<br>x=%{x}<br>minutes=%{y}",
         "legendgroup": "Activity=Sleep1",
         "marker": {
          "color": "#636efa"
         },
         "name": "Activity=Sleep1",
         "offsetgroup": "Activity=Sleep1",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "2018-04-04",
          "2018-04-05",
          "2018-04-06",
          "2018-04-17",
          "2018-04-18",
          "2018-04-19",
          "2018-04-20",
          "2018-04-23",
          "2018-04-24",
          "2018-04-25",
          "2018-04-26",
          "2018-04-30",
          "2018-05-01",
          "2018-05-02",
          "2018-05-04",
          "2018-05-07",
          "2018-05-08",
          "2018-05-09",
          "2018-05-10",
          "2018-05-15",
          "2018-05-16",
          "2018-05-17",
          "2018-05-18",
          "2018-05-21",
          "2018-05-22",
          "2018-05-23",
          "2018-05-24",
          "2018-05-25",
          "2018-05-29",
          "2018-05-30",
          "2018-05-31",
          "2018-06-01",
          "2018-06-04",
          "2018-06-05",
          "2018-06-06",
          "2018-06-07",
          "2018-06-08",
          "2018-06-11",
          "2018-06-12",
          "2018-06-13",
          "2018-06-14",
          "2018-06-18",
          "2018-06-19",
          "2018-06-26",
          "2018-06-27",
          "2018-06-28",
          "2018-06-29",
          "2018-07-09",
          "2018-07-10",
          "2018-07-11",
          "2018-07-12",
          "2018-07-13",
          "2018-07-24",
          "2018-07-25",
          "2018-07-26",
          "2018-07-27",
          "2018-07-30",
          "2018-07-31",
          "2018-08-01",
          "2018-08-02",
          "2018-08-03",
          "2018-08-06",
          "2018-08-07",
          "2018-08-08",
          "2018-08-09",
          "2018-08-10",
          "2018-08-13",
          "2018-08-14",
          "2018-08-15",
          "2018-08-16",
          "2018-08-17",
          "2018-08-20",
          "2018-08-22",
          "2018-08-23",
          "2018-08-24",
          "2018-08-27",
          "2018-08-28",
          "2018-08-29",
          "2018-08-30",
          "2018-09-04",
          "2018-09-05",
          "2018-09-06",
          "2018-09-07",
          "2018-09-10",
          "2018-09-11",
          "2018-09-12",
          "2018-09-13",
          "2018-09-14",
          "2018-09-17",
          "2018-09-18",
          "2018-09-19",
          "2018-09-20",
          "2018-09-21",
          "2018-09-24",
          "2018-09-25",
          "2018-09-26",
          "2018-09-27",
          "2018-09-28",
          "2018-10-01",
          "2018-10-02",
          "2018-10-04",
          "2018-10-05",
          "2018-10-15",
          "2018-10-16",
          "2018-10-17",
          "2018-10-18",
          "2018-10-19",
          "2018-10-22",
          "2018-10-23",
          "2018-10-24",
          "2018-10-29",
          "2018-10-30",
          "2018-10-31",
          "2018-11-01",
          "2018-11-02",
          "2018-11-05",
          "2018-11-06",
          "2018-11-07",
          "2018-11-08",
          "2018-11-09",
          "2018-11-12",
          "2018-11-13",
          "2018-11-14",
          "2018-11-15",
          "2018-11-16",
          "2018-11-19",
          "2018-11-20",
          "2018-11-21",
          "2018-11-27",
          "2018-11-28",
          "2018-11-29",
          "2018-11-30",
          "2018-12-03",
          "2018-12-04",
          "2018-12-05",
          "2018-12-06",
          "2018-12-10",
          "2018-12-11",
          "2018-12-12",
          "2018-12-13",
          "2018-12-17",
          "2018-12-18",
          "2018-12-19",
          "2018-12-20",
          "2018-12-21",
          "2019-01-02",
          "2019-01-03",
          "2019-01-04",
          "2019-01-08",
          "2019-01-09",
          "2019-01-10",
          "2019-01-11",
          "2019-01-14",
          "2019-01-15",
          "2019-01-16",
          "2019-01-17",
          "2019-01-18",
          "2019-01-21",
          "2019-01-22",
          "2019-01-23",
          "2019-01-24",
          "2019-01-25",
          "2019-01-28",
          "2019-01-29",
          "2019-01-30",
          "2019-02-01",
          "2019-02-04",
          "2019-02-05",
          "2019-02-06",
          "2019-02-07",
          "2019-02-08",
          "2019-02-11",
          "2019-02-12",
          "2019-02-13",
          "2019-02-14",
          "2019-02-15",
          "2019-02-25",
          "2019-02-26",
          "2019-02-27",
          "2019-02-28",
          "2019-03-01",
          "2019-03-11",
          "2019-03-12",
          "2019-03-13",
          "2019-03-15",
          "2019-03-18",
          "2019-03-20",
          "2019-03-25",
          "2019-03-26",
          "2019-03-27",
          "2019-03-28",
          "2019-03-29",
          "2019-04-01",
          "2019-04-02",
          "2019-04-03",
          "2019-04-04",
          "2019-04-05",
          "2019-04-08",
          "2019-04-09",
          "2019-04-10",
          "2019-04-11",
          "2019-04-12",
          "2019-04-15",
          "2019-04-16",
          "2019-04-17",
          "2019-04-18",
          "2019-04-19",
          "2019-04-22",
          "2019-04-23",
          "2019-04-24",
          "2019-04-25",
          "2019-04-26",
          "2019-04-29",
          "2019-04-30",
          "2019-05-01",
          "2019-05-02",
          "2019-05-03",
          "2019-05-06",
          "2019-05-07",
          "2019-05-08",
          "2019-05-13",
          "2019-05-14",
          "2019-05-20",
          "2019-05-21",
          "2019-05-22",
          "2019-05-23",
          "2019-05-24",
          "2019-05-28",
          "2019-05-29",
          "2019-05-30",
          "2019-05-31",
          "2019-06-03",
          "2019-06-05",
          "2019-06-06",
          "2019-06-07",
          "2019-06-10",
          "2019-06-11",
          "2019-06-25",
          "2019-06-26",
          "2019-06-27",
          "2019-06-28",
          "2019-07-01",
          "2019-07-02",
          "2019-07-03",
          "2019-07-05",
          "2019-07-08",
          "2019-07-09",
          "2019-07-10",
          "2019-07-11",
          "2019-07-12",
          "2019-07-15",
          "2019-07-16",
          "2019-07-17",
          "2019-07-18",
          "2019-07-22",
          "2019-07-24",
          "2019-07-29",
          "2019-07-30",
          "2019-07-31",
          "2019-08-01",
          "2019-08-02",
          "2019-08-05",
          "2019-08-06",
          "2019-08-07",
          "2019-08-08",
          "2019-08-09",
          "2019-08-12",
          "2019-08-13",
          "2019-08-14",
          "2019-08-15",
          "2019-08-16",
          "2019-08-20",
          "2019-08-21",
          "2019-08-22",
          "2019-08-23",
          "2019-08-26",
          "2019-08-27",
          "2019-08-28",
          "2019-08-29",
          "2019-09-03",
          "2019-09-04",
          "2019-09-05",
          "2019-09-06",
          "2019-09-09",
          "2019-09-10",
          "2019-09-11",
          "2019-09-12",
          "2019-09-13",
          "2019-09-16",
          "2019-09-17",
          "2019-09-18",
          "2019-09-19",
          "2019-09-20",
          "2019-09-23",
          "2019-09-24",
          "2019-09-25",
          "2019-09-26",
          "2019-09-27",
          "2019-10-07",
          "2019-10-08",
          "2019-10-09",
          "2019-10-10",
          "2019-10-11",
          "2019-10-15",
          "2019-10-16",
          "2019-10-17",
          "2019-10-18",
          "2019-10-21",
          "2019-10-22",
          "2019-10-23",
          "2019-10-24",
          "2019-10-25",
          "2019-10-28",
          "2019-10-29",
          "2019-10-30",
          "2019-10-31",
          "2019-11-01",
          "2019-11-04",
          "2019-11-05",
          "2019-11-06",
          "2019-11-07",
          "2019-11-08",
          "2019-11-11",
          "2019-11-12",
          "2019-11-13",
          "2019-11-14",
          "2019-11-15",
          "2019-11-18",
          "2019-11-19",
          "2019-11-20",
          "2019-11-21",
          "2019-11-22",
          "2019-11-25",
          "2019-11-27",
          "2019-12-02",
          "2019-12-03",
          "2019-12-04",
          "2019-12-05",
          "2019-12-06",
          "2019-12-09",
          "2019-12-10",
          "2019-12-11",
          "2019-12-12",
          "2019-12-13",
          "2019-12-16",
          "2019-12-17",
          "2019-12-18",
          "2019-12-19",
          "2020-01-06",
          "2020-01-07",
          "2020-01-08",
          "2020-01-09",
          "2020-01-10",
          "2020-01-13",
          "2020-01-14",
          "2020-01-15",
          "2020-01-16",
          "2020-01-17",
          "2020-01-20",
          "2020-01-21",
          "2020-01-22",
          "2020-01-23",
          "2020-01-30",
          "2020-01-31"
         ],
         "xaxis": "x",
         "y": [
          22,
          51,
          30,
          21,
          39,
          41,
          47,
          58,
          25,
          32,
          41,
          31,
          39,
          43,
          35,
          41,
          22,
          44,
          62,
          33,
          35,
          26,
          39,
          32,
          20,
          17,
          55,
          41,
          48,
          91,
          49,
          26,
          19,
          47,
          34,
          38,
          78,
          56,
          27,
          64,
          25,
          54,
          37,
          54,
          25,
          14,
          11,
          28,
          31,
          35,
          58,
          58,
          41,
          86,
          43,
          96,
          35,
          18,
          26,
          18,
          39,
          36,
          26,
          102,
          31,
          37,
          20,
          42,
          32,
          25,
          21,
          21,
          126,
          45,
          76,
          23,
          38,
          33,
          20,
          55,
          40,
          39,
          35,
          56,
          47,
          30,
          26,
          29,
          47,
          38,
          33,
          38,
          33,
          25,
          28,
          27,
          32,
          23,
          32,
          43,
          11,
          36,
          20,
          41,
          8,
          34,
          29,
          22,
          6,
          47,
          85,
          7,
          44,
          28,
          65,
          33,
          34,
          44,
          41,
          60,
          36,
          25,
          46,
          30,
          65,
          41,
          29,
          30,
          24,
          19,
          34,
          24,
          50,
          29,
          39,
          29,
          9,
          30,
          34,
          8,
          41,
          25,
          35,
          29,
          56,
          72,
          35,
          20,
          104,
          87,
          47,
          117,
          72,
          46,
          93,
          65,
          26,
          89,
          78,
          99,
          90,
          59,
          54,
          33,
          63,
          88,
          108,
          99,
          32,
          69,
          40,
          92,
          86,
          85,
          84,
          113,
          58,
          95,
          81,
          69,
          51,
          45,
          79,
          74,
          116,
          95,
          77,
          89,
          83,
          84,
          66,
          65,
          70,
          56,
          71,
          92,
          74,
          58,
          85,
          64,
          92,
          132,
          83,
          64,
          115,
          103,
          70,
          104,
          107,
          101,
          89,
          74,
          78,
          92,
          76,
          111,
          87,
          63,
          99,
          68,
          91,
          75,
          131,
          96,
          109,
          106,
          77,
          123,
          80,
          110,
          92,
          108,
          107,
          67,
          63,
          116,
          113,
          81,
          111,
          113,
          119,
          98,
          112,
          122,
          64,
          123,
          117,
          104,
          87,
          107,
          76,
          116,
          113,
          77,
          101,
          105,
          88,
          97,
          110,
          107,
          116,
          100,
          101,
          102,
          92,
          103,
          97,
          134,
          101,
          102,
          103,
          90,
          100,
          96,
          107,
          81,
          113,
          97,
          98,
          90,
          99,
          87,
          99,
          85,
          88,
          104,
          104,
          81,
          102,
          92,
          94,
          114,
          119,
          75,
          99,
          105,
          98,
          89,
          83,
          104,
          90,
          81,
          74,
          114,
          129,
          98,
          105,
          82,
          87,
          116,
          106,
          110,
          128,
          84,
          113,
          96,
          129,
          109,
          94,
          116,
          78,
          92,
          89,
          102,
          124,
          100,
          131,
          107,
          151,
          133,
          95,
          118,
          102,
          111,
          128,
          106,
          122,
          111,
          86,
          112,
          99,
          115,
          88,
          96,
          137,
          117,
          118,
          83,
          107,
          109,
          106,
          112,
          125,
          102,
          119,
          94,
          117,
          76,
          87,
          99,
          94,
          115,
          103,
          94
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "Activity=Sleep2<br>x=%{x}<br>minutes=%{y}",
         "legendgroup": "Activity=Sleep2",
         "marker": {
          "color": "#EF553B"
         },
         "name": "Activity=Sleep2",
         "offsetgroup": "Activity=Sleep2",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "2018-04-04",
          "2018-04-05",
          "2018-04-06",
          "2018-04-17",
          "2018-04-18",
          "2018-04-19",
          "2018-04-20",
          "2018-04-23",
          "2018-04-24",
          "2018-04-25",
          "2018-04-26",
          "2018-04-30",
          "2018-05-01",
          "2018-05-02",
          "2018-05-04",
          "2018-05-07",
          "2018-05-08",
          "2018-05-09",
          "2018-05-15",
          "2018-05-16",
          "2018-05-17",
          "2018-05-18",
          "2018-05-21",
          "2018-05-22",
          "2018-05-23",
          "2018-05-24",
          "2018-05-25",
          "2018-05-29",
          "2018-05-30",
          "2018-05-31",
          "2018-06-01",
          "2018-06-04",
          "2018-06-05",
          "2018-06-06",
          "2018-06-07",
          "2018-06-08",
          "2018-06-11",
          "2018-06-12",
          "2018-06-13",
          "2018-06-14",
          "2018-06-18",
          "2018-06-19",
          "2018-06-26",
          "2018-06-27",
          "2018-06-28",
          "2018-06-29",
          "2018-07-09",
          "2018-07-10",
          "2018-07-11",
          "2018-07-12",
          "2018-07-13",
          "2018-07-24",
          "2018-07-25",
          "2018-07-26",
          "2018-07-27",
          "2018-07-30",
          "2018-07-31",
          "2018-08-01",
          "2018-08-02",
          "2018-08-03",
          "2018-08-06",
          "2018-08-07",
          "2018-08-08",
          "2018-08-09",
          "2018-08-10",
          "2018-08-13",
          "2018-08-14",
          "2018-08-15",
          "2018-08-16",
          "2018-08-17",
          "2018-08-20",
          "2018-08-23",
          "2018-08-24",
          "2018-08-27",
          "2018-08-28",
          "2018-08-29",
          "2018-09-04",
          "2018-09-05",
          "2018-09-06",
          "2018-09-07",
          "2018-09-12",
          "2018-09-13",
          "2018-09-14",
          "2018-09-17",
          "2018-09-19",
          "2018-09-20",
          "2018-09-24",
          "2018-09-25",
          "2018-09-26",
          "2018-10-02",
          "2018-10-04",
          "2018-10-05",
          "2018-10-15",
          "2018-10-17",
          "2018-10-22",
          "2018-10-29",
          "2018-10-30",
          "2018-11-02",
          "2018-11-15",
          "2018-11-16",
          "2018-11-28",
          "2018-12-13",
          "2018-12-19",
          "2019-01-04",
          "2020-01-20"
         ],
         "xaxis": "x",
         "y": [
          19,
          29,
          66,
          27,
          18,
          27,
          17,
          29,
          28,
          20,
          41,
          32,
          33,
          33,
          13,
          63,
          43,
          19,
          26,
          14,
          15,
          45,
          9,
          45,
          27,
          38,
          29,
          38,
          28,
          24,
          20,
          80,
          17,
          49,
          8,
          46,
          23,
          40,
          6,
          40,
          27,
          65,
          24,
          25,
          27,
          35,
          27,
          39,
          99,
          46,
          27,
          133,
          41,
          48,
          30,
          33,
          43,
          46,
          21,
          66,
          31,
          88,
          19,
          38,
          26,
          72,
          45,
          47,
          30,
          44,
          22,
          50,
          24,
          65,
          35,
          48,
          38,
          60,
          35,
          45,
          61,
          40,
          50,
          16,
          42,
          36,
          4,
          34,
          60,
          20,
          34,
          26,
          18,
          53,
          30,
          27,
          36,
          27,
          19,
          45,
          16,
          17,
          13,
          76,
          24
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "Activity=Sleep3<br>x=%{x}<br>minutes=%{y}",
         "legendgroup": "Activity=Sleep3",
         "marker": {
          "color": "#00cc96"
         },
         "name": "Activity=Sleep3",
         "offsetgroup": "Activity=Sleep3",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "2018-04-04",
          "2018-04-05",
          "2018-04-17",
          "2018-04-19",
          "2018-04-20",
          "2018-04-23",
          "2018-04-24",
          "2018-04-25",
          "2018-04-30",
          "2018-05-01",
          "2018-05-02",
          "2018-05-04",
          "2018-05-07",
          "2018-05-09",
          "2018-05-16",
          "2018-05-17",
          "2018-05-22",
          "2018-05-23",
          "2018-05-24",
          "2018-05-29",
          "2018-05-31",
          "2018-06-01",
          "2018-06-04",
          "2018-06-05",
          "2018-06-07",
          "2018-06-12",
          "2018-06-18",
          "2018-06-19",
          "2018-06-26",
          "2018-06-28",
          "2018-06-29",
          "2018-07-09",
          "2018-07-10",
          "2018-07-11",
          "2018-07-25",
          "2018-07-26",
          "2018-07-30",
          "2018-08-02",
          "2018-08-09",
          "2018-08-10",
          "2018-08-20",
          "2018-09-04",
          "2018-09-07",
          "2018-10-15"
         ],
         "xaxis": "x",
         "y": [
          13,
          110,
          30,
          53,
          54,
          43,
          34,
          40,
          34,
          24,
          27,
          31,
          22,
          34,
          31,
          67,
          33,
          62,
          37,
          29,
          48,
          11,
          37,
          20,
          28,
          28,
          38,
          47,
          45,
          121,
          36,
          77,
          40,
          36,
          24,
          39,
          22,
          25,
          31,
          21,
          29,
          36,
          11,
          21
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "Activity=Sleep4<br>x=%{x}<br>minutes=%{y}",
         "legendgroup": "Activity=Sleep4",
         "marker": {
          "color": "#ab63fa"
         },
         "name": "Activity=Sleep4",
         "offsetgroup": "Activity=Sleep4",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "2018-04-04",
          "2018-04-17",
          "2018-04-19",
          "2018-04-20",
          "2018-04-24",
          "2018-04-30",
          "2018-05-01",
          "2018-05-09",
          "2018-05-17",
          "2018-05-22",
          "2018-05-24",
          "2018-06-05",
          "2018-06-07",
          "2018-07-30"
         ],
         "xaxis": "x",
         "y": [
          22,
          48,
          17,
          60,
          32,
          33,
          12,
          35,
          26,
          50,
          26,
          41,
          31,
          22
         ],
         "yaxis": "y"
        },
        {
         "alignmentgroup": "True",
         "hoverlabel": {
          "namelength": 0
         },
         "hovertemplate": "Activity=Sleep5<br>x=%{x}<br>minutes=%{y}",
         "legendgroup": "Activity=Sleep5",
         "marker": {
          "color": "#FFA15A"
         },
         "name": "Activity=Sleep5",
         "offsetgroup": "Activity=Sleep5",
         "orientation": "v",
         "showlegend": true,
         "textposition": "auto",
         "type": "bar",
         "x": [
          "2018-04-04",
          "2018-05-24"
         ],
         "xaxis": "x",
         "y": [
          51,
          8
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "margin": {
         "t": 60
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "Daily Nap Pattern"
        },
        "xaxis": {
         "anchor": "y",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "Date"
         }
        },
        "yaxis": {
         "anchor": "x",
         "domain": [
          0,
          1
         ],
         "title": {
          "text": "minutes"
         }
        }
       }
      },
      "text/html": [
       "<div>\n",
       "        \n",
       "        \n",
       "            <div id=\"58f6d887-87c3-40b4-9176-7908503647ef\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>\n",
       "            <script type=\"text/javascript\">\n",
       "                require([\"plotly\"], function(Plotly) {\n",
       "                    window.PLOTLYENV=window.PLOTLYENV || {};\n",
       "                    \n",
       "                if (document.getElementById(\"58f6d887-87c3-40b4-9176-7908503647ef\")) {\n",
       "                    Plotly.newPlot(\n",
       "                        '58f6d887-87c3-40b4-9176-7908503647ef',\n",
       "                        [{\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"Activity=Sleep1<br>x=%{x}<br>minutes=%{y}\", \"legendgroup\": \"Activity=Sleep1\", \"marker\": {\"color\": \"#636efa\"}, \"name\": \"Activity=Sleep1\", \"offsetgroup\": \"Activity=Sleep1\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [\"2018-04-04\", \"2018-04-05\", \"2018-04-06\", \"2018-04-17\", \"2018-04-18\", \"2018-04-19\", \"2018-04-20\", \"2018-04-23\", \"2018-04-24\", \"2018-04-25\", \"2018-04-26\", \"2018-04-30\", \"2018-05-01\", \"2018-05-02\", \"2018-05-04\", \"2018-05-07\", \"2018-05-08\", \"2018-05-09\", \"2018-05-10\", \"2018-05-15\", \"2018-05-16\", \"2018-05-17\", \"2018-05-18\", \"2018-05-21\", \"2018-05-22\", \"2018-05-23\", \"2018-05-24\", \"2018-05-25\", \"2018-05-29\", \"2018-05-30\", \"2018-05-31\", \"2018-06-01\", \"2018-06-04\", \"2018-06-05\", \"2018-06-06\", \"2018-06-07\", \"2018-06-08\", \"2018-06-11\", \"2018-06-12\", \"2018-06-13\", \"2018-06-14\", \"2018-06-18\", \"2018-06-19\", \"2018-06-26\", \"2018-06-27\", \"2018-06-28\", \"2018-06-29\", \"2018-07-09\", \"2018-07-10\", \"2018-07-11\", \"2018-07-12\", \"2018-07-13\", \"2018-07-24\", \"2018-07-25\", \"2018-07-26\", \"2018-07-27\", \"2018-07-30\", \"2018-07-31\", \"2018-08-01\", \"2018-08-02\", \"2018-08-03\", \"2018-08-06\", \"2018-08-07\", \"2018-08-08\", \"2018-08-09\", \"2018-08-10\", \"2018-08-13\", \"2018-08-14\", \"2018-08-15\", \"2018-08-16\", \"2018-08-17\", \"2018-08-20\", \"2018-08-22\", \"2018-08-23\", \"2018-08-24\", \"2018-08-27\", \"2018-08-28\", \"2018-08-29\", \"2018-08-30\", \"2018-09-04\", \"2018-09-05\", \"2018-09-06\", \"2018-09-07\", \"2018-09-10\", \"2018-09-11\", \"2018-09-12\", \"2018-09-13\", \"2018-09-14\", \"2018-09-17\", \"2018-09-18\", \"2018-09-19\", \"2018-09-20\", \"2018-09-21\", \"2018-09-24\", \"2018-09-25\", \"2018-09-26\", \"2018-09-27\", \"2018-09-28\", \"2018-10-01\", \"2018-10-02\", \"2018-10-04\", \"2018-10-05\", \"2018-10-15\", \"2018-10-16\", \"2018-10-17\", \"2018-10-18\", \"2018-10-19\", \"2018-10-22\", \"2018-10-23\", \"2018-10-24\", \"2018-10-29\", \"2018-10-30\", \"2018-10-31\", \"2018-11-01\", \"2018-11-02\", \"2018-11-05\", \"2018-11-06\", \"2018-11-07\", \"2018-11-08\", \"2018-11-09\", \"2018-11-12\", \"2018-11-13\", \"2018-11-14\", \"2018-11-15\", \"2018-11-16\", \"2018-11-19\", \"2018-11-20\", \"2018-11-21\", \"2018-11-27\", \"2018-11-28\", \"2018-11-29\", \"2018-11-30\", \"2018-12-03\", \"2018-12-04\", \"2018-12-05\", \"2018-12-06\", \"2018-12-10\", \"2018-12-11\", \"2018-12-12\", \"2018-12-13\", \"2018-12-17\", \"2018-12-18\", \"2018-12-19\", \"2018-12-20\", \"2018-12-21\", \"2019-01-02\", \"2019-01-03\", \"2019-01-04\", \"2019-01-08\", \"2019-01-09\", \"2019-01-10\", \"2019-01-11\", \"2019-01-14\", \"2019-01-15\", \"2019-01-16\", \"2019-01-17\", \"2019-01-18\", \"2019-01-21\", \"2019-01-22\", \"2019-01-23\", \"2019-01-24\", \"2019-01-25\", \"2019-01-28\", \"2019-01-29\", \"2019-01-30\", \"2019-02-01\", \"2019-02-04\", \"2019-02-05\", \"2019-02-06\", \"2019-02-07\", \"2019-02-08\", \"2019-02-11\", \"2019-02-12\", \"2019-02-13\", \"2019-02-14\", \"2019-02-15\", \"2019-02-25\", \"2019-02-26\", \"2019-02-27\", \"2019-02-28\", \"2019-03-01\", \"2019-03-11\", \"2019-03-12\", \"2019-03-13\", \"2019-03-15\", \"2019-03-18\", \"2019-03-20\", \"2019-03-25\", \"2019-03-26\", \"2019-03-27\", \"2019-03-28\", \"2019-03-29\", \"2019-04-01\", \"2019-04-02\", \"2019-04-03\", \"2019-04-04\", \"2019-04-05\", \"2019-04-08\", \"2019-04-09\", \"2019-04-10\", \"2019-04-11\", \"2019-04-12\", \"2019-04-15\", \"2019-04-16\", \"2019-04-17\", \"2019-04-18\", \"2019-04-19\", \"2019-04-22\", \"2019-04-23\", \"2019-04-24\", \"2019-04-25\", \"2019-04-26\", \"2019-04-29\", \"2019-04-30\", \"2019-05-01\", \"2019-05-02\", \"2019-05-03\", \"2019-05-06\", \"2019-05-07\", \"2019-05-08\", \"2019-05-13\", \"2019-05-14\", \"2019-05-20\", \"2019-05-21\", \"2019-05-22\", \"2019-05-23\", \"2019-05-24\", \"2019-05-28\", \"2019-05-29\", \"2019-05-30\", \"2019-05-31\", \"2019-06-03\", \"2019-06-05\", \"2019-06-06\", \"2019-06-07\", \"2019-06-10\", \"2019-06-11\", \"2019-06-25\", \"2019-06-26\", \"2019-06-27\", \"2019-06-28\", \"2019-07-01\", \"2019-07-02\", \"2019-07-03\", \"2019-07-05\", \"2019-07-08\", \"2019-07-09\", \"2019-07-10\", \"2019-07-11\", \"2019-07-12\", \"2019-07-15\", \"2019-07-16\", \"2019-07-17\", \"2019-07-18\", \"2019-07-22\", \"2019-07-24\", \"2019-07-29\", \"2019-07-30\", \"2019-07-31\", \"2019-08-01\", \"2019-08-02\", \"2019-08-05\", \"2019-08-06\", \"2019-08-07\", \"2019-08-08\", \"2019-08-09\", \"2019-08-12\", \"2019-08-13\", \"2019-08-14\", \"2019-08-15\", \"2019-08-16\", \"2019-08-20\", \"2019-08-21\", \"2019-08-22\", \"2019-08-23\", \"2019-08-26\", \"2019-08-27\", \"2019-08-28\", \"2019-08-29\", \"2019-09-03\", \"2019-09-04\", \"2019-09-05\", \"2019-09-06\", \"2019-09-09\", \"2019-09-10\", \"2019-09-11\", \"2019-09-12\", \"2019-09-13\", \"2019-09-16\", \"2019-09-17\", \"2019-09-18\", \"2019-09-19\", \"2019-09-20\", \"2019-09-23\", \"2019-09-24\", \"2019-09-25\", \"2019-09-26\", \"2019-09-27\", \"2019-10-07\", \"2019-10-08\", \"2019-10-09\", \"2019-10-10\", \"2019-10-11\", \"2019-10-15\", \"2019-10-16\", \"2019-10-17\", \"2019-10-18\", \"2019-10-21\", \"2019-10-22\", \"2019-10-23\", \"2019-10-24\", \"2019-10-25\", \"2019-10-28\", \"2019-10-29\", \"2019-10-30\", \"2019-10-31\", \"2019-11-01\", \"2019-11-04\", \"2019-11-05\", \"2019-11-06\", \"2019-11-07\", \"2019-11-08\", \"2019-11-11\", \"2019-11-12\", \"2019-11-13\", \"2019-11-14\", \"2019-11-15\", \"2019-11-18\", \"2019-11-19\", \"2019-11-20\", \"2019-11-21\", \"2019-11-22\", \"2019-11-25\", \"2019-11-27\", \"2019-12-02\", \"2019-12-03\", \"2019-12-04\", \"2019-12-05\", \"2019-12-06\", \"2019-12-09\", \"2019-12-10\", \"2019-12-11\", \"2019-12-12\", \"2019-12-13\", \"2019-12-16\", \"2019-12-17\", \"2019-12-18\", \"2019-12-19\", \"2020-01-06\", \"2020-01-07\", \"2020-01-08\", \"2020-01-09\", \"2020-01-10\", \"2020-01-13\", \"2020-01-14\", \"2020-01-15\", \"2020-01-16\", \"2020-01-17\", \"2020-01-20\", \"2020-01-21\", \"2020-01-22\", \"2020-01-23\", \"2020-01-30\", \"2020-01-31\"], \"xaxis\": \"x\", \"y\": [22.0, 51.0, 30.0, 21.0, 39.0, 41.0, 47.0, 58.0, 25.0, 32.0, 41.0, 31.0, 39.0, 43.0, 35.0, 41.0, 22.0, 44.0, 62.0, 33.0, 35.0, 26.0, 39.0, 32.0, 20.0, 17.0, 55.0, 41.0, 48.0, 91.0, 49.0, 26.0, 19.0, 47.0, 34.0, 38.0, 78.0, 56.0, 27.0, 64.0, 25.0, 54.0, 37.0, 54.0, 25.0, 14.0, 11.0, 28.0, 31.0, 35.0, 58.0, 58.0, 41.0, 86.0, 43.0, 96.0, 35.0, 18.0, 26.0, 18.0, 39.0, 36.0, 26.0, 102.0, 31.0, 37.0, 20.0, 42.0, 32.0, 25.0, 21.0, 21.0, 126.0, 45.0, 76.0, 23.0, 38.0, 33.0, 20.0, 55.0, 40.0, 39.0, 35.0, 56.0, 47.0, 30.0, 26.0, 29.0, 47.0, 38.0, 33.0, 38.0, 33.0, 25.0, 28.0, 27.0, 32.0, 23.0, 32.0, 43.0, 11.0, 36.0, 20.0, 41.0, 8.0, 34.0, 29.0, 22.0, 6.0, 47.0, 85.0, 7.0, 44.0, 28.0, 65.0, 33.0, 34.0, 44.0, 41.0, 60.0, 36.0, 25.0, 46.0, 30.0, 65.0, 41.0, 29.0, 30.0, 24.0, 19.0, 34.0, 24.0, 50.0, 29.0, 39.0, 29.0, 9.0, 30.0, 34.0, 8.0, 41.0, 25.0, 35.0, 29.0, 56.0, 72.0, 35.0, 20.0, 104.0, 87.0, 47.0, 117.0, 72.0, 46.0, 93.0, 65.0, 26.0, 89.0, 78.0, 99.0, 90.0, 59.0, 54.0, 33.0, 63.0, 88.0, 108.0, 99.0, 32.0, 69.0, 40.0, 92.0, 86.0, 85.0, 84.0, 113.0, 58.0, 95.0, 81.0, 69.0, 51.0, 45.0, 79.0, 74.0, 116.0, 95.0, 77.0, 89.0, 83.0, 84.0, 66.0, 65.0, 70.0, 56.0, 71.0, 92.0, 74.0, 58.0, 85.0, 64.0, 92.0, 132.0, 83.0, 64.0, 115.0, 103.0, 70.0, 104.0, 107.0, 101.0, 89.0, 74.0, 78.0, 92.0, 76.0, 111.0, 87.0, 63.0, 99.0, 68.0, 91.0, 75.0, 131.0, 96.0, 109.0, 106.0, 77.0, 123.0, 80.0, 110.0, 92.0, 108.0, 107.0, 67.0, 63.0, 116.0, 113.0, 81.0, 111.0, 113.0, 119.0, 98.0, 112.0, 122.0, 64.0, 123.0, 117.0, 104.0, 87.0, 107.0, 76.0, 116.0, 113.0, 77.0, 101.0, 105.0, 88.0, 97.0, 110.0, 107.0, 116.0, 100.0, 101.0, 102.0, 92.0, 103.0, 97.0, 134.0, 101.0, 102.0, 103.0, 90.0, 100.0, 96.0, 107.0, 81.0, 113.0, 97.0, 98.0, 90.0, 99.0, 87.0, 99.0, 85.0, 88.0, 104.0, 104.0, 81.0, 102.0, 92.0, 94.0, 114.0, 119.0, 75.0, 99.0, 105.0, 98.0, 89.0, 83.0, 104.0, 90.0, 81.0, 74.0, 114.0, 129.0, 98.0, 105.0, 82.0, 87.0, 116.0, 106.0, 110.0, 128.0, 84.0, 113.0, 96.0, 129.0, 109.0, 94.0, 116.0, 78.0, 92.0, 89.0, 102.0, 124.0, 100.0, 131.0, 107.0, 151.0, 133.0, 95.0, 118.0, 102.0, 111.0, 128.0, 106.0, 122.0, 111.0, 86.0, 112.0, 99.0, 115.0, 88.0, 96.0, 137.0, 117.0, 118.0, 83.0, 107.0, 109.0, 106.0, 112.0, 125.0, 102.0, 119.0, 94.0, 117.0, 76.0, 87.0, 99.0, 94.0, 115.0, 103.0, 94.0], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"Activity=Sleep2<br>x=%{x}<br>minutes=%{y}\", \"legendgroup\": \"Activity=Sleep2\", \"marker\": {\"color\": \"#EF553B\"}, \"name\": \"Activity=Sleep2\", \"offsetgroup\": \"Activity=Sleep2\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [\"2018-04-04\", \"2018-04-05\", \"2018-04-06\", \"2018-04-17\", \"2018-04-18\", \"2018-04-19\", \"2018-04-20\", \"2018-04-23\", \"2018-04-24\", \"2018-04-25\", \"2018-04-26\", \"2018-04-30\", \"2018-05-01\", \"2018-05-02\", \"2018-05-04\", \"2018-05-07\", \"2018-05-08\", \"2018-05-09\", \"2018-05-15\", \"2018-05-16\", \"2018-05-17\", \"2018-05-18\", \"2018-05-21\", \"2018-05-22\", \"2018-05-23\", \"2018-05-24\", \"2018-05-25\", \"2018-05-29\", \"2018-05-30\", \"2018-05-31\", \"2018-06-01\", \"2018-06-04\", \"2018-06-05\", \"2018-06-06\", \"2018-06-07\", \"2018-06-08\", \"2018-06-11\", \"2018-06-12\", \"2018-06-13\", \"2018-06-14\", \"2018-06-18\", \"2018-06-19\", \"2018-06-26\", \"2018-06-27\", \"2018-06-28\", \"2018-06-29\", \"2018-07-09\", \"2018-07-10\", \"2018-07-11\", \"2018-07-12\", \"2018-07-13\", \"2018-07-24\", \"2018-07-25\", \"2018-07-26\", \"2018-07-27\", \"2018-07-30\", \"2018-07-31\", \"2018-08-01\", \"2018-08-02\", \"2018-08-03\", \"2018-08-06\", \"2018-08-07\", \"2018-08-08\", \"2018-08-09\", \"2018-08-10\", \"2018-08-13\", \"2018-08-14\", \"2018-08-15\", \"2018-08-16\", \"2018-08-17\", \"2018-08-20\", \"2018-08-23\", \"2018-08-24\", \"2018-08-27\", \"2018-08-28\", \"2018-08-29\", \"2018-09-04\", \"2018-09-05\", \"2018-09-06\", \"2018-09-07\", \"2018-09-12\", \"2018-09-13\", \"2018-09-14\", \"2018-09-17\", \"2018-09-19\", \"2018-09-20\", \"2018-09-24\", \"2018-09-25\", \"2018-09-26\", \"2018-10-02\", \"2018-10-04\", \"2018-10-05\", \"2018-10-15\", \"2018-10-17\", \"2018-10-22\", \"2018-10-29\", \"2018-10-30\", \"2018-11-02\", \"2018-11-15\", \"2018-11-16\", \"2018-11-28\", \"2018-12-13\", \"2018-12-19\", \"2019-01-04\", \"2020-01-20\"], \"xaxis\": \"x\", \"y\": [19.0, 29.0, 66.0, 27.0, 18.0, 27.0, 17.0, 29.0, 28.0, 20.0, 41.0, 32.0, 33.0, 33.0, 13.0, 63.0, 43.0, 19.0, 26.0, 14.0, 15.0, 45.0, 9.0, 45.0, 27.0, 38.0, 29.0, 38.0, 28.0, 24.0, 20.0, 80.0, 17.0, 49.0, 8.0, 46.0, 23.0, 40.0, 6.0, 40.0, 27.0, 65.0, 24.0, 25.0, 27.0, 35.0, 27.0, 39.0, 99.0, 46.0, 27.0, 133.0, 41.0, 48.0, 30.0, 33.0, 43.0, 46.0, 21.0, 66.0, 31.0, 88.0, 19.0, 38.0, 26.0, 72.0, 45.0, 47.0, 30.0, 44.0, 22.0, 50.0, 24.0, 65.0, 35.0, 48.0, 38.0, 60.0, 35.0, 45.0, 61.0, 40.0, 50.0, 16.0, 42.0, 36.0, 4.0, 34.0, 60.0, 20.0, 34.0, 26.0, 18.0, 53.0, 30.0, 27.0, 36.0, 27.0, 19.0, 45.0, 16.0, 17.0, 13.0, 76.0, 24.0], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"Activity=Sleep3<br>x=%{x}<br>minutes=%{y}\", \"legendgroup\": \"Activity=Sleep3\", \"marker\": {\"color\": \"#00cc96\"}, \"name\": \"Activity=Sleep3\", \"offsetgroup\": \"Activity=Sleep3\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [\"2018-04-04\", \"2018-04-05\", \"2018-04-17\", \"2018-04-19\", \"2018-04-20\", \"2018-04-23\", \"2018-04-24\", \"2018-04-25\", \"2018-04-30\", \"2018-05-01\", \"2018-05-02\", \"2018-05-04\", \"2018-05-07\", \"2018-05-09\", \"2018-05-16\", \"2018-05-17\", \"2018-05-22\", \"2018-05-23\", \"2018-05-24\", \"2018-05-29\", \"2018-05-31\", \"2018-06-01\", \"2018-06-04\", \"2018-06-05\", \"2018-06-07\", \"2018-06-12\", \"2018-06-18\", \"2018-06-19\", \"2018-06-26\", \"2018-06-28\", \"2018-06-29\", \"2018-07-09\", \"2018-07-10\", \"2018-07-11\", \"2018-07-25\", \"2018-07-26\", \"2018-07-30\", \"2018-08-02\", \"2018-08-09\", \"2018-08-10\", \"2018-08-20\", \"2018-09-04\", \"2018-09-07\", \"2018-10-15\"], \"xaxis\": \"x\", \"y\": [13.0, 110.0, 30.0, 53.0, 54.0, 43.0, 34.0, 40.0, 34.0, 24.0, 27.0, 31.0, 22.0, 34.0, 31.0, 67.0, 33.0, 62.0, 37.0, 29.0, 48.0, 11.0, 37.0, 20.0, 28.0, 28.0, 38.0, 47.0, 45.0, 121.0, 36.0, 77.0, 40.0, 36.0, 24.0, 39.0, 22.0, 25.0, 31.0, 21.0, 29.0, 36.0, 11.0, 21.0], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"Activity=Sleep4<br>x=%{x}<br>minutes=%{y}\", \"legendgroup\": \"Activity=Sleep4\", \"marker\": {\"color\": \"#ab63fa\"}, \"name\": \"Activity=Sleep4\", \"offsetgroup\": \"Activity=Sleep4\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [\"2018-04-04\", \"2018-04-17\", \"2018-04-19\", \"2018-04-20\", \"2018-04-24\", \"2018-04-30\", \"2018-05-01\", \"2018-05-09\", \"2018-05-17\", \"2018-05-22\", \"2018-05-24\", \"2018-06-05\", \"2018-06-07\", \"2018-07-30\"], \"xaxis\": \"x\", \"y\": [22.0, 48.0, 17.0, 60.0, 32.0, 33.0, 12.0, 35.0, 26.0, 50.0, 26.0, 41.0, 31.0, 22.0], \"yaxis\": \"y\"}, {\"alignmentgroup\": \"True\", \"hoverlabel\": {\"namelength\": 0}, \"hovertemplate\": \"Activity=Sleep5<br>x=%{x}<br>minutes=%{y}\", \"legendgroup\": \"Activity=Sleep5\", \"marker\": {\"color\": \"#FFA15A\"}, \"name\": \"Activity=Sleep5\", \"offsetgroup\": \"Activity=Sleep5\", \"orientation\": \"v\", \"showlegend\": true, \"textposition\": \"auto\", \"type\": \"bar\", \"x\": [\"2018-04-04\", \"2018-05-24\"], \"xaxis\": \"x\", \"y\": [51.0, 8.0], \"yaxis\": \"y\"}],\n",
       "                        {\"barmode\": \"relative\", \"legend\": {\"tracegroupgap\": 0}, \"margin\": {\"t\": 60}, \"template\": {\"data\": {\"bar\": [{\"error_x\": {\"color\": \"#2a3f5f\"}, \"error_y\": {\"color\": \"#2a3f5f\"}, \"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"bar\"}], \"barpolar\": [{\"marker\": {\"line\": {\"color\": \"#E5ECF6\", \"width\": 0.5}}, \"type\": \"barpolar\"}], \"carpet\": [{\"aaxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"baxis\": {\"endlinecolor\": \"#2a3f5f\", \"gridcolor\": \"white\", \"linecolor\": \"white\", \"minorgridcolor\": \"white\", \"startlinecolor\": \"#2a3f5f\"}, \"type\": \"carpet\"}], \"choropleth\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"choropleth\"}], \"contour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"contour\"}], \"contourcarpet\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"contourcarpet\"}], \"heatmap\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmap\"}], \"heatmapgl\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"heatmapgl\"}], \"histogram\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"histogram\"}], \"histogram2d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2d\"}], \"histogram2dcontour\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"histogram2dcontour\"}], \"mesh3d\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"type\": \"mesh3d\"}], \"parcoords\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"parcoords\"}], \"pie\": [{\"automargin\": true, \"type\": \"pie\"}], \"scatter\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter\"}], \"scatter3d\": [{\"line\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatter3d\"}], \"scattercarpet\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattercarpet\"}], \"scattergeo\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergeo\"}], \"scattergl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattergl\"}], \"scattermapbox\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scattermapbox\"}], \"scatterpolar\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolar\"}], \"scatterpolargl\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterpolargl\"}], \"scatterternary\": [{\"marker\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"type\": \"scatterternary\"}], \"surface\": [{\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}, \"colorscale\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"type\": \"surface\"}], \"table\": [{\"cells\": {\"fill\": {\"color\": \"#EBF0F8\"}, \"line\": {\"color\": \"white\"}}, \"header\": {\"fill\": {\"color\": \"#C8D4E3\"}, \"line\": {\"color\": \"white\"}}, \"type\": \"table\"}]}, \"layout\": {\"annotationdefaults\": {\"arrowcolor\": \"#2a3f5f\", \"arrowhead\": 0, \"arrowwidth\": 1}, \"coloraxis\": {\"colorbar\": {\"outlinewidth\": 0, \"ticks\": \"\"}}, \"colorscale\": {\"diverging\": [[0, \"#8e0152\"], [0.1, \"#c51b7d\"], [0.2, \"#de77ae\"], [0.3, \"#f1b6da\"], [0.4, \"#fde0ef\"], [0.5, \"#f7f7f7\"], [0.6, \"#e6f5d0\"], [0.7, \"#b8e186\"], [0.8, \"#7fbc41\"], [0.9, \"#4d9221\"], [1, \"#276419\"]], \"sequential\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]], \"sequentialminus\": [[0.0, \"#0d0887\"], [0.1111111111111111, \"#46039f\"], [0.2222222222222222, \"#7201a8\"], [0.3333333333333333, \"#9c179e\"], [0.4444444444444444, \"#bd3786\"], [0.5555555555555556, \"#d8576b\"], [0.6666666666666666, \"#ed7953\"], [0.7777777777777778, \"#fb9f3a\"], [0.8888888888888888, \"#fdca26\"], [1.0, \"#f0f921\"]]}, \"colorway\": [\"#636efa\", \"#EF553B\", \"#00cc96\", \"#ab63fa\", \"#FFA15A\", \"#19d3f3\", \"#FF6692\", \"#B6E880\", \"#FF97FF\", \"#FECB52\"], \"font\": {\"color\": \"#2a3f5f\"}, \"geo\": {\"bgcolor\": \"white\", \"lakecolor\": \"white\", \"landcolor\": \"#E5ECF6\", \"showlakes\": true, \"showland\": true, \"subunitcolor\": \"white\"}, \"hoverlabel\": {\"align\": \"left\"}, \"hovermode\": \"closest\", \"mapbox\": {\"style\": \"light\"}, \"paper_bgcolor\": \"white\", \"plot_bgcolor\": \"#E5ECF6\", \"polar\": {\"angularaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"radialaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"scene\": {\"xaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"yaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}, \"zaxis\": {\"backgroundcolor\": \"#E5ECF6\", \"gridcolor\": \"white\", \"gridwidth\": 2, \"linecolor\": \"white\", \"showbackground\": true, \"ticks\": \"\", \"zerolinecolor\": \"white\"}}, \"shapedefaults\": {\"line\": {\"color\": \"#2a3f5f\"}}, \"ternary\": {\"aaxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"baxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}, \"bgcolor\": \"#E5ECF6\", \"caxis\": {\"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\"}}, \"title\": {\"x\": 0.05}, \"xaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}, \"yaxis\": {\"automargin\": true, \"gridcolor\": \"white\", \"linecolor\": \"white\", \"ticks\": \"\", \"title\": {\"standoff\": 15}, \"zerolinecolor\": \"white\", \"zerolinewidth\": 2}}}, \"title\": {\"text\": \"Daily Nap Pattern\"}, \"xaxis\": {\"anchor\": \"y\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"Date\"}}, \"yaxis\": {\"anchor\": \"x\", \"domain\": [0.0, 1.0], \"title\": {\"text\": \"minutes\"}}},\n",
       "                        {\"responsive\": true}\n",
       "                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('58f6d887-87c3-40b4-9176-7908503647ef');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })\n",
       "                };\n",
       "                });\n",
       "            </script>\n",
       "        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = px.bar(df_sleep, x=df_sleep.index.date, y=\"minutes\", color='Activity')\n",
    "fig.update_layout(title=\"Daily Nap Pattern\", xaxis_title=\"Date\")\n",
    "fig.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If we add start and end time, that will allow for sleep schedule visualization, along with previously visualized time and pattern. A 3D bar chart (x = date, y = duration, z = start time) will facilitate this. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#set date and time as spearate columns \n",
    "df_sleep['Date'] = df_sleep.index.date\n",
    "df_sleep['Start'] = df_sleep.index.time\n",
    "#df_sleep.reset_index(inplace = True)\n",
    "#df_sleep.drop(['timestamp'], axis = 1, inplace = True)\n",
    "df_sleep = df_sleep[['Date','Start','minutes','Activity']]\n",
    "df_sleep.head()\n",
    "\n",
    "#save index to insert later \n",
    "index = df_sleep.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "#number unique dates to set position as x-axis \n",
    "unique_dates = pd.DataFrame(df_sleep['Date'].unique())\n",
    "unique_dates.reset_index(inplace = True)\n",
    "unique_dates.rename(columns = {'index': 'x position', 0: 'Date'}, inplace = True)\n",
    "\n",
    "df_sleep = pd.merge(df_sleep, unique_dates, on = 'Date')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Start</th>\n",
       "      <th>minutes</th>\n",
       "      <th>Activity</th>\n",
       "      <th>x position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>09:39:00</td>\n",
       "      <td>22.0</td>\n",
       "      <td>Sleep1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>10:13:00</td>\n",
       "      <td>19.0</td>\n",
       "      <td>Sleep2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>11:07:00</td>\n",
       "      <td>13.0</td>\n",
       "      <td>Sleep3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>12:38:00</td>\n",
       "      <td>22.0</td>\n",
       "      <td>Sleep4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>14:46:00</td>\n",
       "      <td>51.0</td>\n",
       "      <td>Sleep5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Date     Start  minutes Activity  x position\n",
       "0  2018-04-04  09:39:00     22.0   Sleep1           0\n",
       "1  2018-04-04  10:13:00     19.0   Sleep2           0\n",
       "2  2018-04-04  11:07:00     13.0   Sleep3           0\n",
       "3  2018-04-04  12:38:00     22.0   Sleep4           0\n",
       "4  2018-04-04  14:46:00     51.0   Sleep5           0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_sleep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "unique_times = pd.DataFrame(df_sleep['Start'].unique())\n",
    "unique_times.sort_values(by = 0, inplace = True)\n",
    "unique_times.reset_index(drop = True, inplace = True)\n",
    "unique_times.reset_index(inplace = True)\n",
    "unique_times.rename(columns = {'index': 'y position', 0: 'Start'}, inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Start</th>\n",
       "      <th>minutes</th>\n",
       "      <th>Activity</th>\n",
       "      <th>x position</th>\n",
       "      <th>y position</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>09:39:00</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>54</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>10:13:00</td>\n",
       "      <td>19.0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>104</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>11:07:00</td>\n",
       "      <td>13.0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>73</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>373</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>12:38:00</td>\n",
       "      <td>22.0</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>134</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>489</th>\n",
       "      <td>2018-04-04</td>\n",
       "      <td>14:46:00</td>\n",
       "      <td>51.0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>206</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Date     Start  minutes  Activity  x position  y position\n",
       "27   2018-04-04  09:39:00     22.0         1           0          23\n",
       "54   2018-04-04  10:13:00     19.0         2           0          40\n",
       "104  2018-04-04  11:07:00     13.0         3           0          73\n",
       "373  2018-04-04  12:38:00     22.0         4           0         134\n",
       "489  2018-04-04  14:46:00     51.0         5           0         206"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_sleep.sort_values(by = \"Start\", inplace = True)\n",
    "df_sleep = pd.merge(df_sleep, unique_times, on = 'Start')\n",
    "\n",
    "df_sleep.sort_values(['x position', 'y position'], inplace = True)\n",
    "#df_sleep.set_index(index, inplace = True)\n",
    "\n",
    "#remove sleep form activity column for multiple colored bars\n",
    "df_sleep['Activity'] = df_sleep['Activity'].str.replace('Sleep', '')\n",
    "df_sleep['Activity'] = df_sleep['Activity'].astype(int)\n",
    "df_sleep.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Date           object\n",
       "Start          object\n",
       "minutes       float64\n",
       "Activity        int64\n",
       "x position      int64\n",
       "y position      int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Here, I am setting the date and time columns as a string so they can be switched out with position \n",
    "#later on in the 3D \n",
    "df_sleep['Date'] = df_sleep['Date'].astype(str)\n",
    "df_sleep['Start'] = df_sleep['Start'].astype(str)\n",
    "df_sleep.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#define colors\n",
    "colors = ['k','royalblue','orangered','mediumspringgreen','blueviolet','orange']\n",
    "\n",
    "#store colors\n",
    "clrs = []\n",
    "for n in df_sleep['Activity']:\n",
    "    c = colors[n]\n",
    "    clrs.append(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "No handles with labels found to put in legend.\n"
     ]
    }
   ],
   "source": [
    "#import 3D plotting, this step is still in development \n",
    "from mpl_toolkits.mplot3d import Axes3D \n",
    "\n",
    "#interactive plot\n",
    "%matplotlib qt\n",
    "\n",
    "#set bar positions \n",
    "x = df_sleep ['x position']\n",
    "y = df_sleep ['y position']\n",
    "z = np.zeros (529)\n",
    "\n",
    "#set bar depths \n",
    "dx = 2*(np.ones (529))\n",
    "dy = np.ones (529)\n",
    "dz = df_sleep['minutes']\n",
    "\n",
    "#initiate figure \n",
    "fig = plt.figure(figsize = (12,8))\n",
    "ax1 = fig.add_subplot(111, projection='3d')\n",
    "ax1.bar3d(x,y,z,dx,dy,dz,alpha = 0.25, color = clrs)\n",
    "\n",
    "ax1.set_xticklabels(['','April 18','July 18','October 18',' January 19','April 19','July 19','October 19','January 20'])\n",
    "ax1.set_xlabel('')\n",
    "\n",
    "ax1.set_yticklabels(['6 AM','8 AM','10 AM','12 PM','2 PM','4 PM'])\n",
    "ax1.set_ylabel('Start Time')\n",
    "\n",
    "ax1.set_zlabel('Duaration (minutes)')\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
