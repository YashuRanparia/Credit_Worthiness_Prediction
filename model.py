import pandas as pd


def marking(x,dict):
    for i in dict:
        if x in i:
            return dict[i]

def preprocess(data_dict):
    data = pd.DataFrame(data_dict,index=[i for i in range(20)])

    discard_features = ['Attribute9', 'Attribute13', 'Attribute11', 'Attribute20']

    data.drop(discard_features,axis=1,inplace=True)

    dict =  {
        'Attribute1': {
            ('A13','A14'): 0,    #Positive Impact
            ('A11','A12'): 1,
        },
        'Attribute4': {
            ('A40', 'A41'): 0,
            ('A42', 'A43','A44'): 1,
            ('A46','A48'): 2,
            ('A49'): 3,
            ('A47','A410','A45'): 4,
        },
        'Attribute3': {
            ('A30', 'A31'): 0,
            ('A32'): 1, 
            ('A33', 'A34'): 2
        },
        'Attribute12':{
            ('A121', 'A123'): 0,
            ('A122'): 1,
            ('A124'): 2 
        },
        'Attribute15':{
            ('A152'): 0, #positive impact
            ('A153'): 1, #neutral impact
            ('A151'): 2
        },
        'Attribute14':{
            ('A143'): 0,    #positive impact
            ('A141','A142'): 1
        },
        'Attribute10':{
            ('A101'): 0,    #Positive Impact
            ('A102','A103'): 1,
        },
        'Attribute7':{
            ('A72','A73','A74', 'A75') : 0,  #Employed
            ('A71'): 1,
        },
        'Attribute17':{
            ('A171','A172'): 0,    #Not a good job
            ('A173','A174'): 1,
        },
        'Attribute6':{
            ('A64','A63','A62'): 0,    #High Savings
            ('A61'): 1,    #Medium savings
            ('A65'): 2,
        },
        'Attribute19':{
            ('A191'): 0,    #No telephone registered
            ('A192'): 1,
        }
    }

    for key in dict:
        data[key] = data[key].apply(lambda x: marking(x,dict[key]))

    return data