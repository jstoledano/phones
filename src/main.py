#!/usr/bin/env python

import tabula
import numpy as np

file = '../data/201834mac290254telefonos.pdf'
output_format = 'csv'
output_path = '../data/test.csv'
options = (
    '--silent',
    '--pages all',
    '--area 152.433 29.004 592.532 917.505'
)

df = tabula.read_pdf(
    file,
    output_path,
    pages='all',
    guess=False,
    lattice=True,
    silent=True,
    area=(152.433, 29.004, 592.532, 917.505),
    pandas_options={
        'header': None,
        'names': ('folio_notificacion', 'clave_elector', 'folio', 'paterno', 'materno', 'nombre', 'telefono'),
        'dtype': {'folio_notificacion': np.str, 'folio': np.str, 'telefono': np.str},
    }
)
print(df)

# tabula.convert_into(
#     '../data/201834mac290254telefonos.pdf',
#     output_format='csv',
#     output_path='../data/test.csv',
#     silent=True,
#     pages='all',
#     guess=False,
#     lattice=True,
#     area=(152.433,29.004,592.532,917.505),
#     pandas_options={'header':None, 'names': ('folio_notificacion', 'clave_elector', 'folio', 'paterno', 'materno', 'nombre', 'telefono')}
# )
