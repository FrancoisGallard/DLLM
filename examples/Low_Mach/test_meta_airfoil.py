# -*-mode: python; py-indent-offset: 4; tab-width: 8; coding: iso-8859-1 -*-
#  DLLM (non-linear Differentiated Lifting Line Model, open source software)
# 
#  Copyright (C) 2013-2015 Airbus Group SAS
# 
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# 
#  http://github.com/TBD
#
# Imports
from DLLM.DLLMGeom.wing_param import Wing_param
from DLLM.DLLMKernel.DLLMSolver import DLLMSolver
from MDOTools.OC.operating_condition import OperatingCondition

OC=OperatingCondition('cond1')
OC.set_Mach(0.4)
OC.set_AoA(3.5)
OC.set_altitude(5000.)
OC.set_T0_deg(15.)
OC.set_P0(101325.)
OC.set_humidity(0.)
OC.compute_atmosphere()

wing_param=Wing_param('test_param',geom_type='Broken',n_sect=20)
wing_param.build_wing()
wing_param.set_value('test_param.span',34.1)  #34.1
wing_param.set_value('test_param.sweep',34.)
wing_param.set_value('test_param.break_percent',23.) #33.
wing_param.set_value('test_param.root_chord',5.4)  #6.1
wing_param.set_value('test_param.break_chord',4.6)
wing_param.set_value('test_param.tip_chord',1.2) #1.5
wing_param.set_value('test_param.root_height',.98)
wing_param.set_value('test_param.break_height',0.70)
wing_param.set_value('test_param.tip_height',0.18)
wing_param.convert_to_design_variable('test_param.span',(10.,50.))
wing_param.convert_to_design_variable('test_param.sweep',(0.,40.))
wing_param.convert_to_design_variable('test_param.break_percent',(20.,40.))
wing_param.convert_to_design_variable('test_param.root_chord',(5.,7.))
wing_param.convert_to_design_variable('test_param.break_chord',(3.,5.))
wing_param.convert_to_design_variable('test_param.tip_chord',(1.,2.))
wing_param.convert_to_design_variable('test_param.root_height',(0.7,1.))
wing_param.convert_to_design_variable('test_param.break_height',(0.45,0.8))
wing_param.convert_to_design_variable('test_param.tip_height',(0.10,0.26))
#wing_param.build_linear_airfoil(OC, AoA0=-2., Cm0=-0.1, set_as_ref=True)
wing_param.build_meta_airfoil(OC, '../MetaModelCleaning.xml', relative_thickness=.12, camber=0., Sref=1., Lref=1., sweep=.0, set_as_ref=True)
wing_param.build_airfoils_from_ref()
wing_param.update()

print wing_param

DLLM = DLLMSolver('Meta',wing_param,OC)
DLLM.run_direct()
DLLM.run_post()
