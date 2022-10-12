import pandas as pd
import numpy as np

from datetime import datetime


dates = pd.date_range(datetime.now().date(), periods=8)
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])  # index=dates
df['Dates'] = dates

mountain_head = pd.Series(
    [2061, 2035.8, 2028.5, 2022.5, 2016.4],
    index=['Goverla', 'Brebenskyl', 'Pip_Ivan', 'Petros', 'Gutin_Tomnatik'],
    name='Height, m',
    dtype=float
)

contacts = pd.DataFrame(
    {
        'name': [
            'Allen Raymond',
            'Chaim Lewis',
            'Kennedy Lane',
            'Wylie Pope',
            'Cyrus Jackson'
        ],
        'email': [
            'allen@mail.com',
            'chaim@mail.com',
            'kennedy@mail.comn',
            'wylie@mail.com',
            'cyrus@mail.com'
        ],
        'phone': [
            '(992) 914-1234',
            '(345) 234-4567',
            '(233) 123-9900',
            '(678) 233-0988',
            '(653) 111-5690'
        ],
        'favorite': [
            False,
            False,
            True,
            False,
            True
        ]
    },
    index=[1, 2, 3, 4, 5]
)

# print(mountain_head.sort_values(ascending=False))
# contacts['phone'][2] = '(555) 666-8899'
# contacts.__getitem__('phone').__setitem__([2], '(555) 666-7788')
# print(contacts['phone'])

tmp = pd.read_html(io='https://www.statisticstimes.com/tech/top-computer-languages.php',
                   attrs={'id': 'table_id1'},
                   index_col='Jun 2022')
# tmp[0]['Change'][1] = '100'
tmp[0]['nums'] = [i for i in range(1, len(tmp[0]) + 1)]

# tmp[0].append(pd.Series(['Jun 2022', 'Change', 'Programming language', 'Share', 'Trends'],
#                         [29, 'Yes', 'Python2', '30%', '+2.5%']),
#               ignore_index=True)
# tmp[0] = pd.concat([tmp[0], pd.DataFrame.from_records([{'Change': 'Yes',
#                                                         'Programming language': 'Python',
#                                                         'Share': '30%',
#                                                         'Trends': '+2.5%'
#                                                         }])])
#
# tmp[0].drop(['Change'], axis=1, inplace=True)
# print(tmp[0].dropna())
# print(tmp[0].fillna(0.0))
# print(tmp[0].replace('↑↑↑', 1.0))
# print(tmp[0].drop_duplicates('Change'))

date = pd.date_range(start=datetime.now().date(), periods=7)
date_view = pd.Series(
    [i for i in range(len(date))],
    index=pd.date_range(start=datetime.now().date(), periods=7).sort_values(ascending=False)
)
print(tmp[0])
