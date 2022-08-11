# -*- coding: utf-8 -*-

"""
To change the version of entire package, just edit this one location.
"""

__title__ = "news_scraper"
__author__ = "Ivan Sedelkin, Suad Huseynli, Mohammed Shakir"
__copyright__ = "Copyright 2022, EIOP"

version_info = (0, 4, 5)
__version__ = ".".join(map(str, version_info))

# Scrape and Lick
"""
..........................................................................................................................................................................................................................................................................................................  
',,,,,,,,,,'''''''''''''''''''''''''''''',,,''''''''''',,'',,,,,,,,,,,,;;;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,;;;;;,,,,,,,'''''''''''.''''''''''''''''''''''',,,,,,',,,'',,,',,,,,,,,,,,,,'''''''''''''',,,,,,,,,,,'''''''',,,'''''',,,,''. 
''',,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''',,,,''''''''',,,',,,,,,',,,,,,,,,,,,,,,,,,,,,,''''........                       .......''''''''''''''''',''''''''''''',,,,,,,'''''''''''''''',,,,,,,,,'''''''''''''''''''',;::.
,'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,;;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''',,'''''''''',,',,'',,,'',,,,,,,,,,,,,,''......              .......'.........          ....''''''''''''''''''''''''''''',,'''''''''''''''''''',,,,,,,,,''''''''''''''''',',;col.
,,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,;,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''',,''',,,,,,'',,,,,'''.....             ..',;:codxkkOO00KKKK0000OOkdoc;'..       ...'',,,''''''''''''''''''''''''''''''''''''''''''''',,,,,,''',,,'''''''''''',,,,;c:.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''',,'',,,,,,,'......          ..,,;clodkO00KKXXXXKKKKKKKKKKKKKKKKKKXXXK0Oxdl;'.      ...'''''''''''''''''''''''''''''''''''''''''''''''',''''',,,,'''''''''',,,,,'',,.
'',,'',,,''''''''''''''''''',''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''''',,,,,,,,,''''''''''''''''',,,,,'....        ...',:ldxO0KKKKXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0koc,.      ...''''''''''''''''''''''''''''''''''''''''''''''''''',,''''''',,''',,,,,,,,.
',,,,,,,,,,''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''',,''',,'''''''',''''''''''''''...       ..';coxO0KKKXXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKOdc'.     ......'''...''''''''''''''''''''''''''''''''''''''',,''''''',,;;;;;,,,,,,.
',,''',,''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'''''','''''''''''''''',''''''''...      ..,coxOO0KXXXKKKKKKKKKKKK00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK000KKKKKKKKKKKKKKK0ko;.     ....'''...'''''''''''''''''''''''''''''''''''''',,,','',,;cooolc;,,,,,.
,'''''''''''''''''''',''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'',,,,,,'''''''''''''''',,''''''..    .'cok0KXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK00000KKKKKKKKKKKKKKKKKKKKKKKKKKKKOo;.     ......''''''''''''''''''''''''''''''''''''''''',,'''';cokkkxo:,,',,.
''''''''''''''''''''''','''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'',,,,'''''''''''''''''''''''''..   'oOKXXXXXKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK0OxdolllllloddxkO00KKKKKKKKKKKKKKKKKKKKKKKOo;.     ...''''''''''''''''''''''''''''''''''''''''',,'''',;ldxdoc;,'','.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''','',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''''''''''''''''''''''''.   ,kXXXKKKKKKKKKKKKK0Okxxk0KKKKKKKKKKKKKKKKKKK0Oxolcccccclllcccccccllodk0KKKKKKKKKKKKKKKKKKKKXKkl,     ....''''''''''''''''''''''''''''''''''''''',,,,'',;:::;;,''',,.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,'',,,,,,,,,,,,,,,,,;,,,,,,,,,,,,,,,,,,',,'''''''''''''''''''''''''''.   'xXXKKKKKKKKKKKK0kolccccclok0KKKKKKKKKKKKKKOxl::clllllloolllllooollcc:cldOKKKKKKKKKKKKKKKKKKKKKX0d:.     ...'''''''''''''''''''''''''''''''''''''''''''''''''''',,,,.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,;;;,,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''','.   .dKXKKKKKKKKKKKOxoccclllolc::lkKKKKKKKKKKKOdc::cllllllolllloolllolllllllc:cok0KKKKKKKKKKKKKKKKKKKKXKOo,.     ..'''''''''''''''''''''''''''''''.'''''''''''''''''',,,,.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,;,,,,,,,,,,,,,,,,,,,'''''''''''''''''''''''','..  .c0XKKKKKKKKKK0xc::clooloolllc:cd0XKKKKKK0dl:clllllllllllllloollloooooollllccclx0KKKKKKKKKKKKKKKKKKKKKK0d;.     ..',::;,'''''''''''''''''''''''''''''''''''''''''''','.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,;:ccc:;,,,,,,,,,,,,,,,,,,,,,,,,,''''''''''''''',,,,,'''''.   'kXXKKKKKKKKKOoccclllllllllllolc:o0KKKK0klcclollllllllllllllllllllllooolllloolc:okKKKKKKKKKKKKKKKKKKKKKKXKkl'     .,cc:,''''''''''''''''''''''''''''''''''''''''''''''.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,;;cldddoc:,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''.   .oKXKKKKKKKKKOl:clollllllllllooolc:d0XX0dccllllllllllllllllllllllllllllllllllllll:cd0KKKKKKKKKKKKKKKKKKKKKKXKOo,.   ..,,''''''...''''''''''''..''''''''''''''''''''''''.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,,;coxxxdl:,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''''''''''.   ;OXKKKKKKKKKOl:cllllllllllllloooolccxK0dcclllllllllllllllllllllllllllllllllllllool::oOKKKKKKKKKKKKKKKKKKKKKKKKK0d;.    .''........'''''''''''.....'''''''''''''''''''''.
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''',,,,;:coool:;,,,,,,,,,,,,,,,,,,,,,,,''''''''''''''''''''''''.   .oXXKKKKKKKXOo:cllllllllllllllllloolclxdccllloooolllllllllllllllllllllllllllllllllllc;lOKKKKKKKKKKKKKKKKKKKKKKKKKX0d,.   .........'''''''''''''....'''''''''''''''''''''.
''''''''''''''''''''''''''''''''''''''''''',,'''''''''''''''''''''',,,,,,;;;;;,,,,,,,,,,,,,,,,,,,,,,,,,'''''''''''''''''''','''.   ;0XXKKKKKKX0d:cllllollllllllllllloollc::clllllloolllllllooollllllllllllllllllllllllolc:lOKKKKKKKKKKKKKKKKKKKKKKKKKKK0o'   .....'''''''''''''''''''''''''''''''''''''''''.
'''''''''''''''''''''''''''''''''''''''''''','''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'',,,,'''''''''''''''''''''''.   .dXXKKXKKKK0xccllllllllllllllllllloollc::lolllllllllllllllooollllllllllllllllllllllllllc:oOKKKKKKKKKKKKKKKKKKKKKKKK0KKKk:.  ..'''''''''''''''''''''''''''''''''''''''''''.
''''''''''''''''''''''''''''''''''''''''''''',,''','''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,',,''''''''''''''''''''''''''''''.   ;OXXKKKKKKKkc:llolllloolloooollolloolllclllllllloolooolollllllllllllllllllllllllllllllll::o0XKKKKKKKKKKKKKKKKKKKKKK00KKXk'   ...'''''''''''''''''''''''''''''''''''''''''.
''''''''''''''''''''''''''''''''',,,''',,',,''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,',,'''''''''''''''''''''''''''''.   .oKXKKKKKXXOl:cllllooloollllloooollolllllllllollloolooolllooolllllllllllllllllllllllllllll:ckKKKKKKKKKKKKKKKKKKKKKKKKKKKX0:   ..'''''''''''''''''''''''''''''''''''''''','.
''''''''''''''''''''''''''',,,''',,',,,,,',,''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,'',',,''''''''''''''''''''''''''.   'kXKKKKKKX0dcclllllolllllllooooooolollllllllllllllolooolllooollllllllllllllllllllooollloooc;l0KKKKKKKKKKKKKKKKKKKKKKKKKKXKl.  ..'''''''''''''''''''''''''''''''''''',,,,,,.
''''''''''',,,',,''',,,,;,,,''',,,''''',,,',''''''''''''''''''''''',,,,,,,,,,,,,,,,,,;;;;,,,,'',,,,''''''''''''''''''''''''''.  .c0XKKKKKKXkccllllloollllooooooooooloolloollllllllooolooolllloollllllllllllllllllloollllloll:cxKKKKKKKKKKKKKKKKKKKKKKKKKKXKo.   ...'''''''''''''''''''''''''''''',,,,,,,,,,.
,,''''''''',,,,,,,,,,,:cl:;,,'',,,''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,;:clc;,,,,'',,,''''''''''''''''''''''',,'.  .oKXKKKKKX0d:cllllloolllllllllllllllllllllllllolloooolloooooloollllllllllllllllllllollllllllc:o0KKKKKKKKKKKKKKKKKKKKKKKKKKKx'   ..''''''''''''''''''''''''''''',,,,;;;;;;;,.
..'''''''''',,,,,,,,,;:clc;,,,'',,''''''''',''''''''''''''''''''''',,,,,,,,,,,,,,,,,,;:::;,,'',,,,'''''''''''''''''''''''',;'.  'kXKKKKKKXOl:colllloolllloollooolollllloooolllllllooolllooooollllllllllllllllllllllllllllllll:l0KKKKKKKKKKKKKKKKKKKKKKKKKKXk,   .''''''''''''''''''''''''''',,,,,;;:::c:::;.
  ...',,,,,,,,,,,,,,,,,;;,,,'''',,'''''',''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,'',,'''''''''''''''''''''''''',,.   ;0NKKKKKKKxcclllllloollloolllooooollllooooooolc:llooolooooooollllllllllllllllllllllllllllllol:ckKKKKKKKKKKKKKKKKKKKKKKKKKKXO,   .''''''''''''''''''''''''''',,,;;:cclooool:.
     ..'',,,,,,,,,,,,,,,,,,,,,,''''''''',,'''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,,,''''''''''''''''''''''''''''.  .lKXKKKKKK0dclllllllloooolllllllllllcclollloolc;:lllllloolllllolllllllllllllllllllllllooolllol::xKKKKKKKKKKKKKKKKKKKKKKKKKKXO;   .',''''''''''''''''''''''''',,;;:clodxkkkxo.
        ..',,,,,,,,,,,,,,,,,,,,,''''''',,,,''''''''''''''''''''''''''',,,,,,,,,,,,,,,;:::;,,,,,,'''''''''''''''''''''''''''.   .oKXKKKKKKOlclolllllllloooollllllllc:clollllll:;clllllllollloooollllllllllooolllllllloolllolll::dKKKKKKKKKKKKKKKKKKKKKKKKKKXO;   .',''',,,,,,'''''''''''''''',,;::cloxkOOOOd'
          ..'',,,,,,,,,,,,,,,,,''',,'''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,;:c:;,,,,,,'''''''''''''''''''''''''''.   .xXXKKKKKKxccllllllllllllolllllllolc:clollllll::lllcccccclloollllllollllllllolllllllooolllllllc:dKKKKKKKKKKKKKKKKKKKKKKKKKKXO,   .'''''',;::;,''''''''''''''',,,;:clodxkkkko.
             ..',,,,,,,,'''''''''''''''''',,,''''''''''''''''''''''''',,,,,,,,,,,,,,,,;;;,,,,,,,,''''''''''''''''''''''''''.   .kXXKKKKK0dclllllllolllllllcccccccc;;:ccc:ccc:;;::ccccclllllllllllllolllllllllllllllooolloooolc:o0KKKKKKKKKKKKKKKKKKKKKKKKKXO;   .'''''',,:::,'''''''''','''',,,;;:ccloooooc.
               ..',,,,,,'''''''''''''''''''','''''''''''''''''''''''''',,,,,,,,,,,,,,,,,,,,,,,,,,''''''''''''''''''''''''''.   'OXXKKKKX0oclllllllllllloollccccc::;;;cccccc:;:clllllooooolllllllllllllllloooollllllllllloooolc:oKXKKKKKKKKKKKKKKKKKKKKKKKXXO;   .''''''',,,,''''''''''''''''',,,;:::cc::::;.
                 ..'',,,'''''''''''''''''''''''''''''''','''''''''''''''',,,,,,,,,,,,,,,,,,,,,,''''''''''''''''''''''''''''.   ;0XKKKKXXOlcloooollloooooooolllolloc::lollllc;coooooolllooooollloollllllllloooolllllllllllllllc;dKXKKKKKKKKKKKKKKKKKKKKKKKXXO,   ..'''''''''''''''''',''''''''',,,;;;;;;;;;,.
                    ..'''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,,,''''''''''''''''''''''''''''''''''.   :0NKKKKXXkccloollloooollloooolllllll::llllol::clooolllllllllllllllllllllllollooloollllllllllllc:dKKKKKKKKKKKKKKKKKKKKKKKKKKXO,   ..'''''''''''''''''',''''''''''',,,,,,,,,,'.
                      ..''''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,,,,'''''''''''''''''''''''''''''''''''.   :0XKKKKXKxccloollllllllllllllllllllc::lolllc;:lolllllllccccllllllllllllllloooooloollllllllllll:ckKKKKKKKKKKKKKKKKKKKKKKKKKKKk,   ..'''''''''''..''''''''''''''''''''',,,'','.
                        ..''''''''''''''''''''''''''''''''''''''''''''''',,,,,,,,'',,'',''''''''''''''''''''''''''''''''''..   ;0XKKKKXKdcclolllllllloollcccc::::::;;:cccc;;:cccc::::cccccllolloolllloollloolllllllllllllllol:lOKKKKKKKKKKKKKKKKKKKKKKKKKKKx'   ......''.'''.....'''''''''''''''''''''''','.
                          ..'''''''''''''''''''''''''''''''''''''''''''''',,,',,,,,,,,'''''''''''''''''''''''''''''''''''''.   ;0XKKKKXKdcclllllllllllllllllllcllcc:;;:cc:;;:cccccclllllllloooooollllolllloollllllllllllllllc:o0KKKKKKKKKKKKKKKKKKKK00KKKKKo.   ...........'......'''''''''''''''''''''''''.
                            ...''''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,,'''''''''''''''''''''''''''''''''''''.   'kXXKKKXKxccloolllllooooolloolollolll::lool:clllooooloooolooooooollllllllllolloollllllloollolc:xKKKKKKKKKKKKKKKKKKKKKKKKKKXKc.   .......................''''''''''''''''''''.
                              ...''''''''''''''''''''''''''''''''''''''''',,,,,,,,,,,''''''''''''''''''''''''''''''''''''''.   .dKXKKKXKxcclooolc,;:lllloooollllollllcloollllooooooloooolloollllloolllllllllllollooloooooool:lOKKKKKKKKKKKKKKKKKKKKKKKKKKX0;    ......................'''''''''''''''''''''.
                                ...''''''''''''''''''''''''''''''''''''''',,,,,,,,,''''''''''''''''''''''''''''''''''''''''.    :0XKKKXXkccloool,  ...',:lloooolollllllooloolloooooooooollc;,..,looollooollllllllllloooolol::xKKKKKKKKKKKKKKKKKKKKKKKKKKKKO,    ..............................'''''''''''''.
                                  ...''''''''''''''''''''''''''''''''''''',,,,,,'''''''''''''''''''''''''''''''''''''''''''..   .dXXKKXXkccloool'        ..,;clllolllcllccloooooolllc:;,...    .;ooooooollllloooolllooooolc:o0KKKKKKKKKKKKKKKKKKKKKKKKKKKKx.   ..............................''''''''''''''.
                                    ....'''''''''''''''''''''''''''''''''',,,',,''''''''''''''''''''''''''''''''''''''''''''..   ,xXXKXXklcllool,            ...,;::,,cc,,clcc:;,'...           ,lolllllllllloooollloooooc:lOKKKKKKKKKKKKKKKKKKKKKKKKKKKXKo.   ..............................''''''''''''''.
                                       ..''''''''''''''''''''''''''''''''''''','',,''''''''''''''''''''''''''''''''''''''''''..   ,xKXXXOlclooooc,..               ..,l:......               ..'coolooollooollolllllllllc:lkKKKKKKKKKKKKKKKKKKKKKKKKKKKKX0:   ...............'....''''......'''''''''''''''.
                                        ...''''''''''''''''''''''''''''''''''''',,''''''''''''''''''''''''''''''''''''''''''''..   .o0XXOlclooooool:,. .....         'l:.            ...,:'.,clooooooooooooolllllllloolc:lkKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXk'   ..''...............''''.......'''''''''''''''.
                                          ...''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..   .:kX0lcloooooooc,;lx000kdl:;,'.  .cc'   ....';coxO0KXNO:;ldooooooooolllooollllllolc:lkKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXKd.   .,;;''...........''''..........''''''''''''''.
                                            ...''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.    .cxlcllccllll;'dXNMMMMN0xooxkl',ldl'.ckd;':dKWWMMMMMXo,cooolloollllllllolllllllc:lkKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXO;   .'clc;'...........'.............''''''''''''''.
                                              .......'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..    .';llccccll,'xNWMMMWKl...lKO:,col,;OXo...,kNMMWMMMXl,coolcccccccccccllllloolccoOKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXKd.   .';:;,'''........''...'..........'''''''''''''.
                                                ......''''''''''''''''..'''''''''''''''''''''''''''''''''''''''''''''''''''''.....       .,lolccclo:'lOXWMMMNkc;:dOd;,:c:,,oOxc::o0WWWWMMWO:;loolc:::::::ccclloollcclx0KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKXk,   ...''''''....''...''..............'''''''''''''.
                                                  ....''.''''''''''....'''''''''''''''''''''''''''''''''''''''''''''''''''''..     ..',;;:clolllllol;',lONWMMWXOxocccllllcccllld0XWMMWWWXk:,coolc:ccccccccllolllc:;cdk00KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKO:    ...''......''''..................''''''''''''''.
                                                    ........''''''''..''''''''''',''''''''''''''''''''''''''''''''''''''''..    .';clooooooooooooooll:;,;lx0KKOocccloooooollllccok0K0Okdc;;cloolcclllllloollllllcccclllodkKKKKKKKKKKKKKKKKKKKKKKKKKK0d,    .'''''.....'''''......''..........''''''''''''''.
                                                      .....''''.''.'...'''''''',;;;,'''''''''''''''''''''''''''''''''''''..   .,coooooooolooloooooollool:;,,,,;clooooooolllllollc;;;;;;;:clollollloololllllllollollllllcccd0KKKKKKKKKKKKKKKKKKKK0kdc,.   ..'''''.............................''''''''''''''.
                                                       ....''''''.......'''''',;:::,'''''''''''''''''''''''''''''''''''''.    .loooooooooooolooolllccccclooo:,;loollcloollcclloolc;;coollcccclllooooollollllllllllllloool:cOKKKKKKKKKKKKKKKOkdl:,..   ..'',,'''....................''.'''''''''''''''''''''.
                                                         ....'''........''''''',;;,,'''''''''''''''''''''''''''''''''''''..   .;llooooollloolllccclloxkkO0K0o:clllc;;loolc;:ccllllc:o0K0Okxolc:cllooollollloooolooolllllccd0KKKKKKK00Okkxxo;.      .,cooc;,,'''....................''''''''''''''''''''''''.
                                                           ......''.....''''''''''''''''''''''''''''''''''''''''''''''''''..    .,:cllooooollccldk00KKKKKKXKxcccclol:clll:cdxolcccccxKXKKKKK0OdocccllloollloollllllccccldkKK0kxxxdoolllccll;.    .':oxxo:;,,,''''.......'..........''''''''''''''''''..''''.
                                                             ...''.....'''''''''''''''',,,,,,''''''''''''''''''''''''''''''...     ...',,,,;cdk0KKXKKKKKKKKK0OkkkOKOdcccclkKXKOkxxkO0KKKKKKKKKK0OxlcclllolcccllllllodxkO0KX0d::cccccccccclol,   .,;::cc:;;,,,'''''''''..''...'.'...'''''''''''''''''..'''''.
                                                               ........'''''''''''''''',,,,,'''''''''''''''''''''''''''''''''.....        .;xKXXKKKKKKKKKKKKKKKKKKKK0Okkk0KKKKKKKKKKKKKKKKKKKKKKKK0dc:clol::oOOOO000KKKKKKK0d:cllcc::::ccloo;.  .,;;;;;;;;,,,'''''''''''''''''''....'''''''''''''''''''''''.
                                                                .......''''''''''''''''',,'''''''''''''''''''''''''''''''''''''''....     ;OXXKKKKKKKKKKKKKKKKKKKKKKKKK00K000000KKKKKKKKKKKKKKKKKKKKko:cllc:dKXKKKKKKKKKKKKKd:colc;;:ccclloo;.  .,,;,,,,,,,,,,''''''''''''''''''..'''''''''''''''''''''''''.
                                                                  ....''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..   .xXXKKKKKKKKKKKKK000OOkkkkxxxoloddxddooxkkxxkO00KKKKKKKKKKXKOo:cll:o0KKKKKKKKKKKKKKd:clllccc::;cloc.   .,,,,,,,,,,,''''''''''''''''''''''''''''''.''''''''''''''''.
                                                                    ..''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''.    :0XKKKKKKKK0OkkxdxkxoclkOOO0kllk000OxclOOxccdxxdk0KKKKKKKKKKKOl:cl:lOKKKKKKKKKKKKKKd::cccc::::cllc'   ..'',,,,,,,''''''''''''''''''''''''''''''...''''''''''''''''.
                                                                      ..'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''..   .oXXKKKKKKKKOxxoco0XKdoOXNNNWXxdKNNNN0oxNXkokXXkld0KKKKKKKKKKKKxc:l:ckKKKKKKKKKKKKXKx:;cccccclllc,.   ..''''''',,'''''''''''''''''''''''''''''''.''''''''''''''''''.
                                                                       ..''''''''''''''''''''''''''''',,,,'''''''''''''''''''''''''..   .oXXKKKKKKKKKKX0doONOlok0O0000dlx0000kldXKocxkkdoOXKKKKKKKKKKKXOl:cc:xKKKKKKKKKKKKKKkc:clllcc:,..    ..''''''''''''''''''''''''.'''''''''''''''..''''''''''''''''''.
                                       ..                                ..'''''''''''',,;,,'''''''''';::;,'''''''''''''''''''''''''.   .oXXKKKKKKKKKKKKOld0x'.......'....'''..;OO:.....lKXKKKKKKKKKKKX0o:cc:dKKKKKKKKKKKKKKOc'......       ...............'''''''''''''''''''''''''''..'''''''''''''''''''.
                                       ...                                ..'''''',''',;ccc;'''''''''',;:;,'''''..''''''''''''''''''.    cKXKKKKKKKKKKKXKd:lc.                 .;l'    .lKXKKKKKKKKKKKX0o:cc:dKXKKKKKKKKKKKKOl,.         ..............................'''''''''''''...''''''',''''''''.'''.
                                                         .                  ..''''''''';:::,''''''''''',,,''......''''''''''''''''''..   'kXXKKKKKKKKKKK0l...                    ..    .c0XXKKKKKKKKKKKOo:ll:o0XKKKKKKKKKKKKOl:c;.   ......'...........................'''''''''''.......''',;;,'''''....''.
                                                                              .'''''''''',,'''''''''''''..........''''''''''''''''''..    :0XXKKKKKKKKX0x:'.                            ,xKXKKKKKKKKKKKOl:ll;l0KKKKKKKKKKKKK0l:loc;,'',,,;;;;;,,;;;,,'''''................'',,,'''''''.''''',;;,''.....''''.
                                                                               ..'''''''''''''''''''....     .. .....''''''''''''''''..   .l0XXKKKKKK0Odcc;.                            .:OXKKKKKKKKKKKxcclc;o0KKKKKKKKKKKKKOl:llool:;,,,;;;;;;;;;;;;;;;;;;;,,,''..........';c:;,'''''''''',,,,''''''''''''.
                                                                                 ..''''''''''''''''..  ..',,;;;,'..  ...'''''''''''''...   .:kKXXXXXOl,''cc.                             .:kKXKKKKKKKKkl:clc:dKKKKKKKKKKKKKK0l:lllollc:;,,,;;;;;;;;;;;;;;;;;;;;;;;,,''.......,,,,,,,,''''',,'''',''''''''''.
                                                                                  ...'''''''''''...  .,lxkkxkkkxxdl:,..  ...'''''''''''...   .:oxkxo,.  .cc.                              .,oOKKXKKK0xl:cllc:xKKKKKKKKK0KKKK0o:clllllllc:;,,;;;;;;;;;;;;;;;;;;;;;;;;;;;,''........''','',,,',,,;;;,,''''','.
                                                                                    ..'''.''''''..  .:xOOOkkkkkkkOOkxdl;... .....''''''''..     ...     .::.   ....'''.................     .,coddocccclool:ckKKKKKKKKKKKKKK0o:clllooooolc:;,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;,,'........''''''',,;::;,,''''','.
                      ...                           .                                ..'''''''''.   ,dkOkkkkkkkkkkkkkkkxxoc'.   ....'''''.....          .,;'';coddoollclllllllooodxddollc,'..      .'cooool:l0XKKKKKKK00Okxdo:;cllloooooollc;,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'........'','',,,,,,,,,''','.
                      ...                           .                 .                ..'''''''.   :kOOOkkkkkkkkkkkkkkkkkkxoc,..  ......'''......    ..,:ldxkkOkkdodxkkkkkkkkkkkkkkkkkOkxxxo:,.    .coollc;oO00Okkxxdolccccc;;clllolllllloolc;,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'.......'''''''''',,'''''.
                                 ...                  ..              .                 ..''''''..  ,xOOOOkkkkkkkkkkkkkkkkkkkkxdl:,....   ...      ..;:cloxkkkkkkkkkOOOkkkkxxkOkxoloxkkOkkkkkkxdc,. .cooooc:collcccccccclllll:;clllllolccclooll:,',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'......''''''''''''''''.
                                ..'.              .                       .               ...''''.. .:xOkkkkkkkkkkkkkkkkkkkkkkkOkkxxdoc;,.......',;:loooodxkkkOOOkxxdolc;;;;:oxddol:;::cldxkkkxkkxc.'collllllllllllllllllooll::clllllolc::clllol;'',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'.......''''''''''','.
                                 ...                                                        ..''''.. .:xkkkkkkkdoodkkkkkkkkkkkkkkkkkkkkkxxdooddxxkkkkkkkkkkkkxddolol::looooddxxlo0O:';:::clolloodo;.,llccllllllllllllllllooll::cloollollc:::cloo;'',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'.......'''''''''''.
                                                           ..                                ....''.. .'cdkOkOOkdc:cokOOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdolc:lddxkOooOXXXNNNN0dkXXxokXXKKKdcx0K0d,'col::llllllllllllllllolll::cloollooollc::cll;',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'.......'''''''''.
                                                                 .                             ...'.... ..:oxkkkkkoc:cdxkkkkkkkkkkkkkkkkkkkkkkkkkxxdoc::,'''..;cccc:;,clloodddl:oO0Ooo0XNNNkoOXOo;,:ooc:cllollllloollllloolll::cllllllllllllc::,'',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'......''''''''.
                                                                 .                              .........  ..,:ldkkkdocclodxxxkOOOOOkkOOOOkxxxol:;;:;...',;;;:::ccccccc:::::::;,;;::;',clll:,:c;';cooc::llooollllllllllllllll:;cllccccllllllll:'.';;;;;;;;;;;;;;;;;;;;;;;,,;;;;;;;;;;;;;;;;;;,'......''''''.
                                                                .                                 ..........  ...',:clc:;,'..,:cccloooooolc;'.. .,colccclllllooooooooooooooooolllllcc::;;;;;::cclllc:;:cllloooloollllllllllll::clllc:::ccloool;'',;;;;;;;;;;;;;;;;;,,,,''''''''''',',,,,,,,;;;,'.......''''.
                                                               ..                                  ............... .......    ..   .......       .,:ccccc::cllccllllllllllllllllllooolllccccccccc::::cclllllllllooollllllllll::cllllllcc:::cc:'.,,;;;;;;;;;;;;;;;;;;;;;,,'''''....''''''''',,,,,'........''.
                                                                                                    ...........................................    .;ccclllll::loolllllllccc::clllolloollcccccccccllllllloolllollllllllllllll:;cllllllllllc:,..',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'''''.'.'''''''''''........'.
                                                                                                      ..........................................   .:oolllloc:o0KK000OOOOkkkdc:llllllooooollllllllloooooooollllllllolllllccc:;:llcclllloool:''';;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,,,'''''''''''''..........
                                                                                                       .........................................   .cooollll:ckKXKKKKKKKKKKKKxc:lolllllllllllllllllllllllloolllllllllcc:::;;;:cllcc:::cccc;'',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,''''.''''''........
                                                                                           .            ........................................   .coooooll:o0KKKKKKKKKKKKKKOl:loollllllllllllllllollllllllllccc:;,;:ccc:::;;;::lllllcc;'.',;;;;;;;;;;;;;;;,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;,,,''''..''...... 
                                                                                ...        ..             ......................................   .cdoooolccxKKKKKKKKKKKKKKKKxccloolloolllllllllllolllccc:;;;,,,,,'';cc:cdOx:;;;:loool:,',;;;;;;;;;;;,,,,''',,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,''........ 
                                                                               .....          .            .....................................   .:oooool:lOXXXXKKXXXKKXXXXX0o:cllllllllllllcc::::;;;,,,,,,,,,;;;;,,,';dKXKd;;;;cll:,',,;;;;;,,;,,,'''''',,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,,''..... 
                               ...                                   ..           ...          ..           ...'................................    .''',,'.,loooooooooooooollc,..''''',;:;;;;;,,,,,;,,,',,,;;;;;;;;;;,'cOXXXx:;:;,,,'.',,,,,,''''''..''',;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,'... 
                               ...                                   .....  ...   ....          .            ....................................                                      ..,,,,;;;;;;;;;,,''''''',,,,,,'''lKXXKkc:c;'.....''''''.''''',,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,.
                                                                      ....  .....      ......   ..             ........................................                                .',;;;;;;;;;;;;;;,,''''''''''''..lKXXXx::c;''',''''''',,,;;;;;;;;;;;;;;,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
                                                                     .   ...  ..... .. .....     .              ........................................................................,;;;;;;;;;;;;;;;;;;;;,,,,,,;,,,'cOXXKd:::;''',,;;,;;,,;;;;,;;,,,,,,,,,'',,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
                                                                          ..  ..        .....       .            .......................................................................,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,';dKXKo;::,....'''''''''''......''...',,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
                                                                                    .  ....       ...              .....................................................................',,,,,,,,,,;;;,,,,,,,;,,,,,,''...:dOxc,,'.....'''.......     ..'',,',,,,,,,,,;;;,,,,,,,;;;;;;;;;;;;;;;;;;;;;;;;;;;;.
                                                                                  ..     .                          ....               ........              ....  .      .            ..............',,,''''.......... ..',...............           ..','.....................,;;;;;;;;;;;;;;;;;;;;;;;;;;.
                            .':ldxxxxdc;'.      .':odxxxxl:,.    'oxxxxxxxxxxo:,.      .lxxxxxxxxl.    ,oxxxxxxxxxdl:.   ,oxxxxxxxxxxc. ....... .;dxxxxxxxxx:. . .:xxxxx:   ;dxxxd;  .cxxxxxxxxxxoc:,...,,,,'. .;dxxxxd:. .,..:xxxxxd;     .;cdxxxxoc;'.....'oxxxxxc.  .lxxxxc. .,;;;;;;;;;;;;;;;;;;;;;;;:;.
                           'dKNWMMMMMWWNKx'   .:kXNWMMMMMWNXOc.  ;KWMMMMMMMMMWNXk,    .cKMMMMMMWMK:.  .cXMMMMMMMMMWWN0c. :KMMMMMMMMMMk. ......  .xNMMMMMMMMWk'   .xWMMMW0; .oNMMMNo. 'OWMMMMMMMMWWWNKd'..,;;;. .oNMMMMNd..;c..xWMMMWNo   'dKNWWMMMMWWNKd,.  ;0WMMMMO' .oNMMWXl..';;;;;;;;;;;;;;;;;;;;;;;;;;.
                          .xWMMMWXOONMMMMWd. .lXMMMMWKk0WMMMMXd. ;KWMMMMN0OXWMMMNk'   .dWMMMMWWMMXo.   cXMMMMMNOONMMMWK:.:XMMMMMMWWWWk. ......  ,0WMMMMMMMMWK:   .xWMMMMWd..oNMMMNo. 'OWMMMMN0OXMMMMMNd...,;;' .oNMMMMNd..oo..xWMMMMNo  ;OWMMMWXkOXWMMMWO,  ;KWMMMMO'.lXMMMNo...,;;;;;,,,,,'''''.........''.
                          ,0MMMMNx',kWMMMMk. ,OMMMMMXc.:KMMMMM0' ;KWMMMM0:'dWMMMMK;   .OMMMWNXNMMWO'   cXMMMMWO,.xWMMMWl.cXMMMMMKl;;;.  ......  :XMMMWNXXWMMNo   .xWMMMMMK:.oNMMMNd. 'OWMMMMKc.lXMMMMWO,..,;;' .oNMMMMNx.'dd..xWMMMMNo .dNMMMMNd.'kWMMMMXc. ;KWMMMMO;:0MMMNx' .,,,,'....................... 
                          ,0MMMMW0:';clccc,. ;0MMMMWK; ;KMMMMMK; ;KWMMMM0;.dNMMMMX;   ;0MMMNkxXMMMK:   cXMMMMWO' dWMMMWl.cXMMMMWO.      .....  .oNMMWKOkONMMMk.  .xWMMMMMWO:dNMMMNd. 'OWMMMMK:.:KMMMMWO,..,;;' .oNMMMMNd.'dd..xWMMMMNo .kMMMMMNo..xNMMMMNo. ;KWMMMM0d0WMMWO,  ............................. 
                          .kWMMMMWXOl'.      :0MMMMWK; ,0WWWWW0, ;KWMMMMXxdKWMMMWO'  .lXMMMKol0MMMNo.  cXMMMMWO,.kWMMMWl.cXMMMMMKo::;.  .....  'kWMMWOlcdNMMM0;  .xWMMMMMMXOONMMMNd. 'OWMMMMKc.:0WMMMWO,..,,,. .oNMMMMNx.'dd..xWMMMMNo .OMMMMMNo..dXWWWWXo. ;0WMMMMNXWMMMK:  ...............................
                           ,xNMMMMMMWXkc.    :0MMMMWK; .',,,,,'. ;KWMMMMMMMMMWNKd,   .xNMMM0;,OMMMWk'  cXMMMMMN00NMMMMX:.cXMMMMMMWWWXo.  ...   ;0WMMWx,'lXMMMXo. .xWMMMMMMMWNWMMMNd. 'OWMMMMK:.:KMMMMWO, ..... .oNMMMMNx.'dd..xWMMMMNo .kMMMMMNo. .,,,,,,.  ;KWMMMMMMMMMWx. ............................... 
                            .;dKNMMMMMMWKo.  :KMMMMWK;           ;KWMMMMWNXWMMN0o'   ,0WMMMk..xMMMMK;  cXMMMMMMMMMMWNKo..cXMMMMMMMMMNo.  ...   lNMMMNl. ,KMMMWk. .xWMMMMMMMMMMMMMNd. 'OWMMMMK:.:KMMMMWO,       .oNMMMMNx..dd..xWMMMMNo .kMMMMMNo.           ;KWMMMMMMMMMM0,  .............................. 
                              .'lkXWMMMMMWk..:KMMMMWK; .;:::::;. ;KWMMMMKl:OWMMMWk'  cXMMMNd. lNMMMNl. cXMMMMMXkdddl:'. .cXMMMMMNkddo,   ...  .xWMMWK;  .OWMMM0, .xWMMMWXNMMMMMMMNd. 'OWMMMMK:.:KWMMMWO,   ..  .oNMMMMNx..do..xWMMMMNo .OMMMMMNo..':::::;'  ;KWMMMMWWWMMMWx. .............................. 
                          .lkkkkkdcoKWMMMMXc.;KMMMMWK; ;KMWWMMK; ;KWMMMM0;.dNMMMMX; .oNMMMNx;;dXMMMWx..cXMMMMWO'         cXMMMMMO'     .....  ,OWMMWKl,,:ONMMMXc..xWMMMNxxNMMMMMMNo. 'OWMMMMK:.:KWMMMWO,  ...  .oNMMMMNx..oo..xWMMMMNo .kMMMMMNo..xNMWWWXo. ;KWMMMMKkXMMMMXl. ............................. 
                          'OMMMMWO,.oNMMMMWd.;0MMMMWK; ;KMMMMMK, ;KWMMMM0;.oNMMMMX: 'kWMMMMWNNWMMMMWK;.cXMMMMWO'    .    cXMMMMWO'     .....  :KMMMMWWNNWWMMMMNx..xWMMMXc:0WMMMMMNd. 'OWMMMMK:.:KMMMMWO,  ...  .oNMMMMNx...'..xWMMMMNo .xWMMMMNo..xNMMMMXl. ;0WMMMMOcxNMMMW0,  .............................
                          .kWMMMW0;.oNMMMMNo..kWMMMWXc.cXMMMMWO' ;KWMMMM0;.oNMMMMX: ;KMMMMWWNNWWMMMMNl.cXMMMMWO'   .... .cXMMMMMKdccc;.  ... .oWMMMMWNNNNWMMMMM0,.xWMMMXc.oXMMMMMNd. 'OWMMMMXl'oNMMMMWO,  ...  .oNMMMMW0occ;..xWMMMMNo .oNMMMMNd.,OWMMMMKc  ;KWMMMMO,;OMMMMNd..,lxkl'.......................
                          .cKWMMMWK0XWMMMW0;  cXWMMMWX0XWMMMWKc. ;KWMMMM0;.oNMMMMX: cNMMMMKl,,:kWMMMWx,lXMMMMWO'   ...   cXMMMMMMMMMMK:. ... .kMMMMWk:,,,lKMMMMXl,xWMMMX: 'OWMMMMNo. 'OWMMMMWK0XMMMMMWx.       .oNMMMMMMMMMK;.xWMMMMNo  'kWMMMMN0KWMMMMNx.  ;KWMMMMO'.lXMMMMXc..:ooc'.......................
                           .;xKNWMMMMMWNKx;.  .;xKNWMMMMWNNKd,   ;KWMMMMK;.oNMMMMX:.dNMMMM0,  .xWMMMW0clXMMMMWO'  ....   cXMMMMMMMMMMKc. ..  ;0MMMMNd.   ;0MMMMNx:xWMMMXc .cKMMMMNd. 'OWMMMMMMMMMMMWXk;  ..    .oNMMMMMMMMMK;.xWMMMMWo.  'o0XWWMMMMWNXkc.   ;KWMMMMO' .xWMMMWO,  .......................... 
                             ..;clooooc;..      ..;cooool:,.     .coooooc..,looool..;looooc.  .;oooooc''cooooo:.         'cooooooooooc' ...  .cooool;.   .cooooo:';ooool'  .:ooool,  .:oooooooooooo:,.  ....    ,loooooooooc..;oooool,..;'..,:looool:'.     .cooooo:.  .cooool'  .......................... 
                                                                                                                                        .....         ...                          .                 ......             .',,;:;,,,,,,;oOKd.            .....         ..         ............................
                                                                             ....           ........                                    ..................................................    ...........     .....    .lXNWWWNNNXNNNNWWNx.                 ................  ..............................
                                                                            .....         .. ...                                         ................................................     ............   .........  :KWMMMWKxddkXWMMWk'       ....       ................  ............................ 
                                                                                                                                          ...............................................    ..............   .. .. ..  .xNMMMNOl::l0WMMNx.  .  ..........   .................  ........................... 
                                                                                                                                           ..............................................    ...............  .........  :OKKK0xc;;oOKKKOc. ..............  ..................  ..........................  
                                                                                                                                                                                                                          ......   ......                                                                   
                                                                                                                                                                                                                                                                                                            
"""