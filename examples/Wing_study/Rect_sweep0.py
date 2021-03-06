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
from DLLM.DLLMGeom.wing_param import Wing_param
from DLLM.DLLMKernel.DLLMTargetCl import DLLMTargetCl
from MDOTools.OC.operating_condition import OperatingCondition
from MDOTools.ValidGrad.FDValidGrad import FDValidGrad
import numpy
import sys

OC=OperatingCondition('cond1')
OC.set_Mach(0.3)
OC.set_AoA(0.)
OC.set_altitude(3000.)
OC.set_T0_deg(15.)
OC.set_P0(101325.)
OC.set_humidity(0.)
OC.compute_atmosphere()

wing_param=Wing_param('test_param',geom_type='Broken',n_sect=20)
wing_param.build_wing()
wing_param.set_value('span',40.)
wing_param.set_value('sweep',0.)
wing_param.set_value('break_percent',33.)
wing_param.set_value('root_chord',1.0)
wing_param.set_value('break_chord',1.0)
wing_param.set_value('tip_chord',1.0)
wing_param.set_value('root_height',0.15)
wing_param.set_value('break_height',0.15)
wing_param.set_value('tip_height',0.15)
wing_param.build_linear_airfoil(OC, AoA0=0., Cm0=0.0, set_as_ref=True)
wing_param.build_airfoils_from_ref()
wing_param.update()

print wing_param

print 'AR=',wing_param.get_AR()

DLLM = DLLMTargetCl('Rectsweep0',wing_param,OC)
DLLM.set_target_Cl(0.5)
DLLM.run_direct()
DLLM.run_post()



