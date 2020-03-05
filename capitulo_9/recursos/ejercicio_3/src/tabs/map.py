# /bin/env python3
# ==============================================================================
# Copyright (c) Moises Martinez by Fictizia. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from bokeh.plotting import figure
from bokeh.models import (CategoricalColorMapper, 
				HoverTool, 
				ColumnDataSource, 
				Panel, 
				FuncTickFormatter, 
				SingleIntervalTicker, 
				LinearAxis)
from bokeh.models.widgets import (CheckboxGroup, 
				  	Slider, 
					RangeSlider, 
					Tabs, 
					CheckboxButtonGroup, 
					TableColumn, 
					DataTable, 
					Select)

from bokeh.layouts import column, row, WidgetBox
from bokeh.palettes import Category20_16

import pandas as pd
import numpy as np

def map_tab(data, states):

	def make_plot(src, xs, ys):
		
		p = figure(plot_width = 1100, plot_height = 700, title = 'Map of 2018 Flights delays departing from NYC')
		p.xaxis.visible = False
		p.yaxis.visible = False
		p.grid.visible = False
		
		patches_glyph = p.patches(xs, 
					  ys, 
					  fill_alpha=0.2, 
					  fill_color = 'lightgray', 
					  line_color="#884444", 
					  line_width=2, 
					  line_alpha=0.8)

		lines_glyph = p.multi_line('flight_x', 
					   'flight_y', 
					   color = 'color', 
					   line_width = 1, 
					   line_alpha = 0.8, 
					   hover_line_alpha = 1.0, 
					   hover_line_color = 'color',
					   legend = 'carrier', 
					   source = src)

		squares_glyph = p.square('origin_x_loc', 
					 'origin_y_loc', 
					 color = 'color', 
					 size = 7, 
					 source = src, 
					 legend = 'avion')

		circles_glyph = p.circle('dest_x_loc', 
					 'dest_y_loc', 
					 color = 'color', 
					 size = 6, 
					 source = src, 
					 legend = 'avion')

		p.renderers.append(patches_glyph)
		p.renderers.append(lines_glyph)
		p.renderers.append(squares_glyph)
		p.renderers.append(circles_glyph)

		hover_line = HoverTool(tooltips=[('Airline', '@carrier'),
						 ('Number of Flights', '@count'),
						 ('Average Delay', '@mean_delay{0.0}'),
						 ('Max Delay', '@max_delay{0.0}'),
						 ('Min Delay', '@min_delay{0.0}')],
					line_policy = 'next',
					renderers = [lines_glyph])
		
		hover_circle = HoverTool(tooltips=[('Origin', '@origin'),
						   ('Dest', '@dest'),
						   ('Distance (miles)', '@distance')],
					 renderers = [circles_glyph])

		p.legend.location = (10, 45)
		p.add_tools(hover_line)
		p.add_tools(hover_circle)

		p = style(p) 
		
		return p
	
	def style(p):	
		p.title.align = 'center'
		p.title.text_font_size = '20pt'
		p.title.text_font = 'serif'
		p.xaxis.axis_label_text_font_size = '14pt'
		p.xaxis.axis_label_text_font_style = 'bold'
		p.yaxis.axis_label_text_font_size = '14pt'
		p.yaxis.axis_label_text_font_style = 'bold'
		p.xaxis.major_label_text_font_size = '12pt'
		p.yaxis.major_label_text_font_size = '12pt'

		return p
		
