from typing import List
import math

def suitableLocations(center, d):
    mid_point = sum(center) // len(center)
    l, r = -10**10, mid_point
    while l<r:
        mid = int((l+r)//2)
        if total_distance(center, mid) > d:
            l = mid + 1
        else:
            r = mid
    left_point = l
    
    l, r = mid_point, 10**10
    while l<r:
        mid = int((l+r)//2)
        if total_distance(center, mid) <= d:
            l = mid + 1
        else:
            r = mid
    right_point = l
    return int(right_point-left_point)
    
    
def total_distance(center, x):
    res = 0
    for c in center:
        res += abs(c-x) * 2
    return res

print(numberOfwarehouse([-2, 0, 1], 8))
assert numberOfwarehouse([-2, 0, 1], 8) == 3

print(numberOfwarehouse([2, 0, 3, -4], 22))
assert numberOfwarehouse([2, 0, 3, -4], 22) == 5


'''
[2133, 2654, -4807, 1869, -1113, 2547, 4054, 4498, -3265, 3630, -140, -57, 3103, 1778, -726, 1910, 3970, 3589, 4842, 2368, -573, -1080, -2999, -4313, -863, 2074, 4802, 1313, 3787, -3940, 2280, -3967, -1188, -2708, -1863, -2315, 3795, 2658, 3510, -4421, 2023, -1909, 61, -57, -3245, -1271, 456, -600, -546, 74, -3830, -4757, -2072, -754, -2152, -2258, -3358, -2096, -4986, -2269, -2577, -800, 2325, 149, 1820, 3956, 2968, -105, 2689, 2981, -3335, 3769, 3752, 2979, -2776, 4664, -4899, 1249, -4192, -1567, 3814, -889, 4525, -3776, -441, -3349, -3187, 4736, -19, -4643, 786, 3820, 4348, -4598, 2266, 4450, -1128, 3716, 4259, 3964] 525008
[4705, 1350, 518, -1779, -2855, 3096, 1207, -1506, 2673, 2160, 3864, 227, 4288, 4468, 688, -4557, -637, 54, 4985, -3525, -2714, -4610, 2226, 2275, -336, 2154, -3686, 2501, -4964, 285, -1865, -4818, -2029, -4692, 3923, 3278, 4579, 2838, -3942, 2972, -3278, 3296, 1701, -55, 2490, 4066, 703, 4312, -436, 3568, 3302, -1755, -3815, 4813, -2720, -2241, 774, -268, -1326, -4926, 132, 3231, 2821, -4015, -3977, 3896, -4534, -278, -4172, 1315, 779, -1962, -3530, 3000, 1235, -4258, 4814, 4109, 2202, 1957, 4165, -2705, 4953, 1512, 877, -1425, -1177, 3286, 4738, 3733, -410, -4885, -2181, -1534, -3803, 4230, 4179, -1057, -220] 527682
[79976023, 126770008, -160007251, -598730498, 319775962, -800684267, 542728531, 808710649, -938410977, 52010996, -326462865, 579959186, 969700187, 936749584, -108971, 915272384, 34783401, -927141859, 953897978, 482988344, 653290993, 646638058, 629376799, 38884751, 612414524, 165546569, -627535580, -287929522, 627203650, -280914167, -217183130, -251853723, -424430852, 221381870, -932762860, 7780824, 449786993, 76964037, -195555852, 443954032, 422570155, -520979585, 736073213, 163355451, -169760420, -463440863, -332352759, 111306521, -20516531, 865039040, 205937934, 998145106, -299393925, 561756583, -294641733, -34067925, -986102337, 190340657, -245771251, 126806737, 132090960, -508840190, 807599451, -500090797, -277140695, -985900294, 218804575, 600799686, -503472541, 150799918, 192736842, 395356041, 957111753, -277816987, 333110713, 814197140, 665215244, -818193104, -593969277, 270605244, -988407109, 72862801, -398146351, 364158422, -10194388, 616865190, 109798641, 649729996, 791200073, -893576139, -36378453, -792649433, 478950000, 408959600, 834480166, -717080985, -180143494, 416350346, -158069487, -526636694, -939810052, 110674980, -724940008, 991387461, 130194264, 326681207, 993627735, 723339690, 355257646, -778582543, 954289925, 17581412, -410017598, 31040236, 350712633, -796199787, 523445543, 123030098, -972880021, 82639260, 964447616, -971573722, -292164317, -186044035, 765763952, 346535165, -797802335, 699440736, 454820427, 287754074, 885292033, 178452402, 36206255, 229302362, -653382243, 851211794, -94214978, 727703689, -791584904, 274984731, 442216521, 844205798, 548978481, -940765781, 733410768, -472779261, 890663587, 706860212, 156401813, 936060727, -560746250, -660451418, -801019576, -531549, 530181457, 542438266, -781215526, 391610033, 78682866, -11960634, -613383872, 112126568, 367535237, -753538146, 710920209, 918359569, 24397675, 474280715, 920959480, -495146335, 379167909, -871313156, -285214639, 31534599, -369793271, -237184295, -803703307, -84134948, -58840836, -270297300, 676326212, -276695549, 904211882, -14900964, 138257869, -640482089, -833558515, 693563207, -462113129, 257383511, -590178254, -728798554, 399021330, -940565318, -214430760, -24436044, -546093366, -615320714, -284986888, -254759330, -776978424, 170219683, 386241649, -670777588, 419289319, 162867374, -623107892, -750424581, 924890599, 789552209, 52168588, 650864735, -440720670, -404907446, -43659259, -854680980, 701078069, -184097216, 34515537, -761078019, -654456497, 664798372, 332114501, -621192326, 299068464, -928656750, -828476163, -134632731, 895044570, 759916916, -939125675, 122286060, -467828046, -215311817, -119656273, -69611552, 688837073, -224037199, 517744667, -103740525, 862849097, -846758797, -959117659, 3244743, 959351837, -202803245, 264604540, -850850042, -811110415, -776743751, 748336789, 627138476, -757440725, -481829628, -522021034, 899712062, 958839606, 959808581, 992208324, -365828046, 62954841, -301514610, -420103211, 387457559, -572797070, 978428386, -539150274, 213760294, -445314342, 858379393, -983316807, 751626786, 492525384, 873777929, 82612008, -258955690, 214161100, 325815106, -415126517, 420032092, -747041213, -48919157, 305713145, -398790778, 610744377, -869053929, -49729758, -138030059, 405336874, -710770674, 647730305, -490101779, 711866914, -408348929, 943312004, 7744245, 659707025, 619758649, 483230967, -857659973, -641177916, 536687601, 789568277, 451643129, -883691242, -449002424, -320476440, 183064420, 697428653, 701175011, -893442137, -318108404, 99167796, -603501448, 745611637, 165233193, -980433606, -192142084, -165630709, -259335590, -690119825, -72538104, 719695018, -290645829, 790662180, 993199693, 735997981, -197098930, -421552589, -723762249, 39016459, 846821945, 665540995, -500251704, 925670936, 873407315, -30303748, -711235494, 149023470, -249328385, -97941501, 369138149, -435279444, 87688447, 763647164, 307523836, -221114493, 822347773, 440736060, -525881831, -281188258, -418360307, -982925972, 676243174, -920445065, -348322881, -845951856, 994441529, 953880675, -784230264, -686938163, 295589040, -320076549, -232033448, 642535452, 156607572, 405020904, 152257024, 393906711, -37773630, 927933053, 183779671, -11363609, 454430640, -126724489, 780815094, 459974226, -684961099, -124184924, 998613654, 662114471, 280168282, -600952591, 810293488, -711049305, -904980709, -876314536, 289285074, 465135404, -563903304, 476522436, 199004140, 156636768, 917762491, -599188675, -110780520, 739828623, 673391260, 996909792, 721266207, -915918970, 750111746, -809726713, 431547460, 620796731, 171507549, 931685570, 201303213, 233073689, -627527713, -225221756, 437421967, 501710792, 40903380, -132144942, -710843946, 646407358, -163897792, 112500855, -886491207, 19286704, 751673485, 695852425, -59350488, 190200701, 954406687, -911246538, -23423284, -293879595, 68942717, 436956413, -760053937, 426738564, -246441597, 737352487, 783428655, -88901300, 39478599, 996636512, -881489062, -716047184, 377295311, -864516278, 416588086, -688157946, 975384115, 161788053, -993324702, 486445588, -195169561, 705686891, 892399310, 151077136, 262555540, 120006054, -630817796, 643162520, 444951757, 140500908, -916105123, -636391229, 580099717, -799915174, -594420495, -629996343, -283485074, 967535112, -564475989, -162587172, 882463768, 528633937, 536858356, -70325195, -777810673, 167668053, -968478105, -308154830, -102106517, -360699837, 19892074, -165181525, 985187445, 674224983, 770173950, -110292109, -477615432, 826283086, -377572674, 481141396, -228796486, -568074676, -49305127, 149614783, -527848034, -905082647, -453001233, -571847774, 611128555, -106973903, 341755838, 502556867, -461492642, -573933892, -987672470, -273387524, 678279744, 408068897, -813079275, -295965230, -536984808, 972189707, -881896777, 887455042, 760710319, 622376972, -363564357, 345012421, 209586367, -470885998, -57175578, -709076219, -918860312, -776582445, 803632656, -167801578, -311679852, -692870309, -156320116, -575894310, 185002422, -935217943, 135640617, 989237744, -828784309, 250429653, -266587871, 862515908, 250079637, -911415129, 460513312, -632577728, 17083819, 565220976, 645562931, -912180462, -241906999, 394284741, 920146869, -228141369, -714469877, -363163086, 108718923, -522782628, 616270701, -649581179, -820980976, -107187534, 638241793, -198772016, 265537111, -269975796, 673916193, 878703560, 415191892, -624654189, 963298238, 885240589, -784847117, 425294139, 615766171, 147888100, -431850884, 359766595, 753741062, 858542138, 536103436, 146368317, -147472002, 249072855, -898387759, 801167732, 359189514, -892404353, -736289666, -170297553, -368536856, -149256494, 728276007, 821204745, 554064205, 524588536, -981929510, -248709969, -421637183, 13081293, 824415216, 907672353, -87202440, -680997564, -671794055, -822386303, -814210981, -583462929, -229704348, -300820230, 191794268, 911265064, -834765027, 889755774, 515362633, 214944715, 820004496, -673093521, -350942363, -24828614, -916985175, -456434025, -833308525, -9995356, -857130836, 32098441, 525087382, -693654222, 883989062, -437632858, -615935620, -215877641, -90454173, -14815516, -235297962, -814781408, -745523155, 322652338, -871955346, -883336508, -964620052, 598742204, -53382224, 287871240, -237900644, -134312640, 693353153, -858860857, 371425689, -461680117, -631951742, 877352570, -660006124, 715485113, 370693961, 860629211, 812495324, 466308244, -195300029, 682087098, -462094099, 100693055, -286610138, -173151301, -951676036, -351272228, -398141848, 222406817, -564113402, 317074889, 805255697, 742717213, 937535078, -944867937, -660525579, -71321061, 359482341, -147865770, -473462871, -127035971, 928798330, 548795713, -736319458, -934780411, -123955165, 685674877, 37971536, 890567386, 342891502, -677137201, -273512080, 105532418, 396465585, -19660094, -988869307, 944062403, 963653682, 526202823, 794412877, 544910736, -256132053, 515984866, 86125000, 906707556, -349032715, -901303745, 308403237, 570019502, 158193584, -229756031, -398662122, 384476491, -539262237, 680098834, -271191174, -855091412, -299515302, -34182616, -767821712, -469723955, -557092775, 423479384, -631767820, -108379092, -40534548, -368867584, 919633484, -674860300, -761665672, 866550233, 992265046, -208725983, 564992264, -573747899, -30397253, 492445205, -576273718, -430248362, -571538945, 751654223, -342927303, -873975196, -844454666, 55579257, 346244045, 740284866, -178339072, -61072381, 933056807, 629187684, -116781988, -469509646, 503041942, 569387383, 598580603, 932521111, -346664503, 909870533, 782362225, 486067735, 427545133, 838544223, -44083370, -919184415, 270047042, -614129317, 752622795, -398814293, -744057355, 820985509, -425437441, 502397040, -246872908, 820929165, -917436691, 377933024, 939584075, -511292644, 545332917, -898824531, -808227781, -563096361, 826036416, -966446145, -726680905, -90878229, -652081124, 662752360, -580185949, 38127444, 388428595, 554196892, -553854724, 915319255, 514879852, 861450223, -178309047, -949586460, -748010554, 667327324, 121040910, -400775060, 107027408, 574979644, 628232906, -955553099, 945547476, -78928306, 771968538, -338809110, 445832656, 584082995, 562908747, 514848786, 83050058, -562444229, 750721820, -74366494, -606790790, 491350436, 572054984, -324230805, 388628051, 427086818, 143522827, 138706333, -132543847, -592491861, -770479400, 886719933, 802594978, 600721238, 538547854, -767571813, -852873376, 966951545, -139116295, -189730584, -69457464, 100651360, -884700870, -514072685, -732687183, 29160206, 773584564, 276791638, -37392306, -620173702, 986790782, -925953137, 936140462, 277566363, 210245316, -767595927, -248166215, 589468440, 838040855, -145798705, -198435973, 526410519, -148245185, 38266587, -198740858, 481816095, -798878291, 612866386, -277936473, 597011212, -149021321, -212612090, 95324882, 546855610, -893338560, 387506145, -452681679, 908833723, 911982286, -466309333, -119752021, 726970504, 146830969, -908097211, -781943933, 243911688, 751358173, -867436823, 577575378, -196427717, -770037552, 117065406, 802447089, 126287418, -73895909, -39821874, -593585712, -543663222, 434691568, -344519258, 36931386, -498488541, 860596530, -450996609, 606822772, 593988385, 1077

'''