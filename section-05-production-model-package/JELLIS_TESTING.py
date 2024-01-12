from pydantic import BaseModel

class WhatEver(BaseModel):
    name: str
    size: int

print(WhatEver(name='tryout',size = 5, argument_not_in_class=True).name)
#print(WhatEver(name='tryout',size = 5, argument_not_in_class=True).argument_not_in_class) --> ERROR
print(WhatEver(name='tryout',size = 5).size)

#used int instead of str for name --> error expected (but no error given)
print(WhatEver(name=9,size = 5).name) 

obj_ = WhatEver(name='hallo',size=30)
print(obj_.name)

from typing import Optional, List

class HouseDataInputSchema(BaseModel):
    Alley: Optional[str]
    BedroomAbvGr: Optional[int]
    BldgType: Optional[str]

class MultipleHouseDataInputs(BaseModel):
    inputs: List[HouseDataInputSchema]

obj_1 = HouseDataInputSchema(Alley='ja', BedroomAbvGr=3, BldgType='whatever')
print(obj_1.BldgType)

data_obj_2 = {'Alley':'nee','BedroomAbvGr':4,'BldgType':'random'}
obj_2 = HouseDataInputSchema(**data_obj_2) #the ** is necessary to unpack dictionary
print(obj_2.BldgType)

import pandas as pd
df = pd.DataFrame(data={'Alley':['ja','nee'],'BedroomAbvGr':[3,4],'BldgType':['whatever','random']})
print(df.to_dict(orient='records'))
obj_3 = MultipleHouseDataInputs(inputs=df.to_dict(orient='records'))
print(obj_3.inputs[0].BldgType)