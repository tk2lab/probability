# Copyright 2020 The TensorFlow Probability Authors.
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
# ============================================================================
r"""Ground truth values for `stochastic_volatility_sp500_small`.

Automatically generated using the command:

```
python -m inference_gym.tools.get_ground_truth \
  --target=stochastic_volatility_sp500_small \
  --stan_samples=50000
```
"""

import numpy as np

IDENTITY_LOG_VOLATILITY_MEAN = np.array([
    7.268318506680001,
    7.27417840744,
    7.1116079495,
    6.8696819618800005,
    6.7323853933799995,
    6.65894468784,
    6.538234677939999,
    6.53539518584,
    6.479754442700001,
    6.55145445668,
    6.7298578361,
    7.021190713179999,
    7.3784074785,
    7.86294684888,
    8.40349200868,
    8.64635938498,
    8.769558158079999,
    9.05124648522,
    9.12045725832,
    9.33178709892,
    9.419831466039998,
    9.562586552279999,
    9.66725479772,
    9.8033779766,
    10.07690994298,
    10.16471696412,
    10.296270683740001,
    10.48549934508,
    10.53477146486,
    10.5251245675,
    10.23995255734,
    9.998921997459998,
    9.77446440066,
    9.70656588258,
    9.683466460720002,
    9.77000136682,
    9.582437142359998,
    9.5434488821,
    9.368101353380002,
    9.235279800559999,
    9.120391528499999,
    9.120847941920001,
    9.036260814860002,
    9.02901455668,
    9.1486979821,
    8.889127503419997,
    8.78581792182,
    8.589770134999998,
    8.48855806712,
    8.510055749600001,
    8.421823116919999,
    8.33217838004,
    8.37406069954,
    8.328821377859999,
    8.321852967039998,
    8.17430930682,
    7.972022052019999,
    7.912096150980001,
    7.8846462019,
    7.867605554160001,
    7.98582004072,
    7.89518818926,
    7.909658122960001,
    7.6648119137599995,
    7.548112350159999,
    7.4914445933,
    7.541082895120001,
    7.609364533520001,
    7.594502555040002,
    7.726845533320001,
    7.7412756713199995,
    7.7203026549,
    7.75103247788,
    7.908859476719999,
    7.7120555333,
    7.598135329020001,
    7.396952955900001,
    7.2818660994,
    7.299483698799999,
    7.277920734299999,
    7.118052870599999,
    7.0947267838800006,
    7.155533976800001,
    7.3242855584800015,
    7.533204826939999,
    7.69317180198,
    7.9896795117599995,
    8.03430577808,
    8.1355731562,
    8.35048964312,
    8.706083262560002,
    8.342342208580002,
    8.06073154312,
    7.88080883782,
    7.58514920442,
    7.424740313840002,
    7.39994899814,
    7.47627194912,
    7.6327331669000005,
    7.910298574339999,
]).reshape((100,))

IDENTITY_LOG_VOLATILITY_MEAN_STANDARD_ERROR = np.array([
    0.0014843739532068077,
    0.001213566791322832,
    0.001167470943822889,
    0.0012940812882840142,
    0.0013474593438529997,
    0.0013762074379247385,
    0.0015471238061060381,
    0.001543414880194724,
    0.0017299607695414599,
    0.0019051908658357665,
    0.0017963599223401476,
    0.0017814335508758467,
    0.0016681092219795774,
    0.001260571555812206,
    0.0009685464601909508,
    0.0009691535402796822,
    0.0010541570881505587,
    0.0009755268484195636,
    0.001102370464706595,
    0.0010370057996211945,
    0.0010845863765513968,
    0.001084004988871308,
    0.0010893965870925541,
    0.0011138399183207876,
    0.0009516838736037057,
    0.001043559498609259,
    0.0010737472535262225,
    0.0010293463719660968,
    0.0010408216735101085,
    0.001036985924346608,
    0.0010247065144565414,
    0.0010778937057483139,
    0.0011849096998599877,
    0.0013093451824662317,
    0.0011637587386644271,
    0.0010581515593120932,
    0.0011858589534966735,
    0.0010751409522737204,
    0.0011443300483087843,
    0.001122137149472769,
    0.0011594239729226278,
    0.0010901015868403894,
    0.0011088075376478404,
    0.0011022912621923289,
    0.0009324408741143268,
    0.0010660600498054707,
    0.0010119349065086708,
    0.0011072635171144453,
    0.001101923181021366,
    0.0010173565457686565,
    0.001054931613201859,
    0.001105206871914297,
    0.00099580546094967,
    0.0010151316063963898,
    0.0009613094252478865,
    0.0010166832822794895,
    0.001203494502283573,
    0.0012158660678869,
    0.0012931609158126191,
    0.0012013999230537338,
    0.0010090569983751782,
    0.0011710444263245492,
    0.0010349330622893527,
    0.001215917941171991,
    0.0011707911048146774,
    0.0011850521768138735,
    0.0011832644058038717,
    0.001055189175885253,
    0.0011290398534274542,
    0.0010503998094035115,
    0.0010986165085608483,
    0.0010937666061155628,
    0.0010511088160184531,
    0.0009740321443016172,
    0.0010505544445495044,
    0.0010710292137329734,
    0.001238955003073266,
    0.0011733640172356533,
    0.0011138483067888937,
    0.0010246706670914189,
    0.0013290949700449296,
    0.0014705925818115065,
    0.0014346683135254192,
    0.0012357454891855062,
    0.0010997953309407032,
    0.001070287630443859,
    0.000919280368701601,
    0.0010387699592895347,
    0.0011304882134801153,
    0.0011615191298017288,
    0.0009142237675891191,
    0.0009814420825274355,
    0.0011256156288677298,
    0.0011068839896653227,
    0.0014340136571971782,
    0.001557169280794054,
    0.0015673939695160569,
    0.0014236963312661396,
    0.0014099648648951758,
    0.0011682727107551242,
]).reshape((100,))

IDENTITY_LOG_VOLATILITY_STANDARD_DEVIATION = np.array([
    0.7576311029876834,
    0.6503435573294609,
    0.6437570525424625,
    0.6990271629079455,
    0.7151950332919078,
    0.7082620282919925,
    0.7670010183291927,
    0.764764583636051,
    0.8527258429416792,
    0.8804063157853272,
    0.8631386778572396,
    0.8056913759851234,
    0.7499802076742361,
    0.6435339418645626,
    0.5397339194709945,
    0.5586655511756126,
    0.608782051044351,
    0.5664613872471436,
    0.6155790422761571,
    0.5787574361385796,
    0.6037498393077316,
    0.5968701557432168,
    0.6168138266369828,
    0.6316773836957574,
    0.570687873807296,
    0.5959691633895021,
    0.5964992255280532,
    0.567240806834999,
    0.5620648974775386,
    0.5441675567793528,
    0.590945381110419,
    0.6260091407281563,
    0.675106405250143,
    0.6484386100278745,
    0.6306570666828369,
    0.5618727436956519,
    0.6148717873540692,
    0.5770986134351702,
    0.6088945760362819,
    0.625458149669234,
    0.6441793266726965,
    0.6019982358356673,
    0.6266970881375143,
    0.6200772264764589,
    0.5416094190086154,
    0.6163111335185365,
    0.6032140866587097,
    0.6446305159431512,
    0.6524051151333244,
    0.5962463858254642,
    0.6141715868478311,
    0.6437911931219004,
    0.5944414230511051,
    0.5991456422385047,
    0.5703532763340586,
    0.5975864815576204,
    0.660555932065523,
    0.6467448931493844,
    0.6424417993614762,
    0.6437804884490834,
    0.5755730788123878,
    0.6096640889555606,
    0.5744293910395747,
    0.6557684706507138,
    0.6730281928801949,
    0.6804513450885931,
    0.6443897878174455,
    0.6154687855093963,
    0.6443691454965048,
    0.591472431453577,
    0.60288968206588,
    0.621685961931572,
    0.620669193175896,
    0.5476396583465942,
    0.6021821943310208,
    0.602067010540881,
    0.6608428845928,
    0.6818066195550629,
    0.6341719028596127,
    0.6227235341811255,
    0.7154274868304944,
    0.7377852202140333,
    0.7334033315701352,
    0.6811390653939914,
    0.6331855178001794,
    0.6405178912233124,
    0.566745974179017,
    0.6146630962671626,
    0.6399717963252165,
    0.6062531046812708,
    0.5041849443781607,
    0.5863857900832506,
    0.6371710125172493,
    0.6371879454249123,
    0.7552466655337227,
    0.8127032584631456,
    0.805565624664427,
    0.774376095923107,
    0.7432065918773698,
    0.6764411946172574,
]).reshape((100,))

IDENTITY_MEAN_LOG_VOLATILITY_MEAN = np.array([
    7.91516637742,
]).reshape(())

IDENTITY_MEAN_LOG_VOLATILITY_MEAN_STANDARD_ERROR = np.array([
    0.004522720834862319,
]).reshape(())

IDENTITY_MEAN_LOG_VOLATILITY_STANDARD_DEVIATION = np.array([
    1.0478904838684748,
]).reshape(())

IDENTITY_PERSISTENCE_OF_VOLATILITY_MEAN = np.array([
    0.9249792145839999,
]).reshape(())

IDENTITY_PERSISTENCE_OF_VOLATILITY_MEAN_STANDARD_ERROR = np.array([
    0.00014421067997856288,
]).reshape(())

IDENTITY_PERSISTENCE_OF_VOLATILITY_STANDARD_DEVIATION = np.array([
    0.04760110487933296,
]).reshape(())

IDENTITY_WHITE_NOISE_SHOCK_SCALE_MEAN = np.array([
    0.500450060468,
]).reshape(())

IDENTITY_WHITE_NOISE_SHOCK_SCALE_MEAN_STANDARD_ERROR = np.array([
    0.00038906346615080745,
]).reshape(())

IDENTITY_WHITE_NOISE_SHOCK_SCALE_STANDARD_DEVIATION = np.array([
    0.13947841751592666,
]).reshape(())
