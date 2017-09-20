/*
The MIT License (MIT)

Copyright 2017 Pablo Pizarro R.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
*/

// Lista de wallpapers
var images_background = [
    ['09305524.jpg', 'center', '#343434'], // 0
    ['67535412.jpg', 'bottom', '#C96265'], // 1
    ['93314696.jpg', 'center', '#6A6061'], // 2
    ['background.jpg', 'center', '#5E4E2A'], // 3
    ['12939392.jpg', 'center', '#614654'], // 4
    ['19392139.jpg', 'center', '#4E3E25'], // 5
    ['46140562.jpg', 'center', '#EF3D4D'], // 6
    ['37320735.jpg', 'bottom', '#333132'], // 7
    ['71453949.jpg', 'top', '#4F4F51'], // 8
    ['39581671.jpg', 'bottom', '#262C3C'], // 9
    ['99206040.jpg', 'bottom', '#5284A9'], // 10
    ['92910382.jpg', 'bottom', '#444444'], // 11
    ['04274037.jpg', 'top', '#602A13'], // 12
    ['72131838.jpg', 'center', '#896956'], // 13
    ['80718230.jpg', 'bottom', '#4C44AB'], // 14
    ['08038477.jpg', 'center', '#616D61'], // 15
    ['22532189.jpg', 'bottom', '#000000'], // 16
    ['07086832.jpg', 'top', '#4F6068'], // 17
    ['11917378.jpg', 'bottom', '#393939'], // 18
    ['11944943.jpg', 'bottom', '#0A344F'], // 19
    ['15032996.jpg', 'bottom', '#304651'], // 20
    ['37994916.jpg', 'center', '#30307A'], // 21
    ['63330443.jpg', 'top', '#000000'], // 22
    ['46199258.jpg', 'bottom', '#5B4A48'], // 23
    ['39593777.jpg', 'bottom', '#014BBA'], // 24
    ['47702546.jpg', 'bottom', '#702269'], // 25
    ['51280378.jpg', 'center', '#174C82'], // 26
    ['80794446.jpg', 'center', '#6D5630'], // 27
    ['36752157.jpg', 'center', '#FE3060'], // 28
    ['42450256.jpg', 'bottom', '#50405B'], // 29
    ['89228305.jpg', 'bottom', '#C51A20'], // 30
    ['95243003.jpg', 'bottom', '#173966'], // 31
    ['16978868.jpg', 'center', '#7E5A40'], // 32
    ['22125894.jpg', 'bottom', '#272D69'], // 33
    ['77421788.jpg', 'center', '#4E6D44'], // 34
    ['91643340.jpg', 'bottom', '#197B30'], // 35
    ['88093858.jpg', 'bottom', '#485620'], // 36
    ['00939591.jpg', 'center', '#35455B'], // 37
    ['13838368.jpg', 'center', '#6C5640'], // 38
    ['14269512.jpg', 'center', '#4F63D5'], // 39
    ['37882132.jpg', 'bottom', '#223836'], // 40
    ['38920979.jpg', 'bottom', '#357789'], // 41
    ['39850828.jpg', 'center', '#435273'], // 42
    ['50989454.jpg', 'top', '#3e6f8f'], // 43
    ['57231197.jpg', 'bottom', '#4d3945'], // 44
    ['91853601.jpg', 'bottom', '#a32ab5'], // 45
    ['03081592.jpg', 'bottom', '#3c412a'], // 46
    ['15877230.jpg', 'center', '#3c5086'], // 47
    ['25528122.jpg', 'bottom', '#f94021'], // 48
    ['29656367.jpg', 'center', '#3b81fa'], // 49
    ['38184232.jpg', 'bottom', '#6c70a6'], // 50
    ['44532443.jpg', 'center', '#282828'], // 51
    ['45325963.jpg', 'bottom', '#2c5362'], // 52
    ['60192994.jpg', 'bottom', '#562554'], // 53
    ['62639926.jpg', 'bottom', '#54585b'], // 54
    ['65354463.jpg', 'bottom', '#3a3e3f'], // 55
    ['65737758.jpg', 'center', '#80688a'], // 56
    ['66539241.jpg', 'center', '#a62400'], // 57
    ['71516908.jpg', 'center', '#483f44'], // 58
    ['73822546.jpg', 'bottom', '#382952'], // 59
    ['80768085.jpg', 'bottom', '#323e58'], // 60
    ['93568387.jpg', 'bottom', '#354a5a'], // 61
    ['97469752.jpg', 'center', '#ba4234'], // 62
    ['02530621.jpg', 'center', '#313131'], // 63
    ['02534697.jpg', 'top', '#314200'], // 64
    ['02642756.jpg', 'center', '#5b1943'], // 65
    ['03625208.jpg', 'center', '#484f55'], // 66
    ['05378902.jpg', 'bottom', '#141b27'], // 67
    ['09553028.jpg', 'center', '#51363c'], // 68
    ['16845918.jpg', 'center', '#520031'], // 69
    ['18027342.jpg', 'center', '#123473'], // 70
    ['26185627.jpg', 'bottom', '#5142a3'], // 71
    ['30915665.jpg', 'bottom', '#4f6a99'], // 72
    ['31865394.jpg', 'bottom', '#782958'], // 73
    ['32064937.jpg', 'top', '#212224'], // 74
    ['39295944.jpg', 'center', '#a02426'], // 75
    ['45515453.jpg', 'center', '#6a2d1b'], // 76
    ['58763802.jpg', 'center', '#2d2c2a'], // 77
    ['64402687.jpg', 'center', '#1c234f'], // 78
    ['64597743.jpg', 'bottom', '#64202b'], // 79
    ['65086685.jpg', 'bottom', '#4a4e50'], // 80
    ['71169273.jpg', 'center', '#0472af'], // 81
    ['79989977.jpg', 'top', '#09182d'], // 82
    ['82956328.jpg', 'bottom', '#354b72'], // 83
    ['83984226.jpg', 'top', '#721f3f'], // 84
    ['86588736.jpg', 'center', '#5a5a5a'], // 85
    ['94052111.jpg', 'center', '#484e4e'], // 86
    ['94936130.jpg', 'center', '#561111'], // 87
    ['97039416.jpg', 'bottom', '#362d2e'], // 88
    ['07949312.jpg', 'bottom', '#4b6270'], // 89
    ['08760783.jpg', 'bottom', '#096e6a'], // 90
    ['33459034.jpg', 'center', '#2c3552'], // 91
    ['42501581.jpg', 'bottom', '#0c2747'], // 92
    ['50861756.jpg', 'center', '#47411a'], // 93
    ['68963144.jpg', 'center', '#462314'], // 94
    ['70290917.jpg', 'center', '#363635'], // 95
    ['91686162.jpg', 'bottom', '#644c3a'], // 96
    ['99917062.jpg', 'bottom', '#504e4c'], // 97
    ['05327721.jpg', 'top', '#3c3c56'], // 98
    ['19489238.jpg', 'bottom', '#4c4847'], // 99
    ['27241217.jpg', 'center', '#0d1023'], // 100
    ['31534692.jpg', 'bottom', '#403c30'], // 101
    ['45125712.jpg', 'center', '#1e4a0a'], // 102
    ['59272533.jpg', 'center', '#0f2645'], // 103
    ['82884717.jpg', 'bottom', '#1c0031'], // 104
    ['88649909.jpg', 'center', '#513954'], // 105
    ['95686782.jpg', 'bottom', '#2f1143'] // 106
];

// Se obtiene un elemento al azar
var images_indx_random = getRandomInt(0, images_background.length - 1);
var image_url = href_images_parent + images_background[images_indx_random][0];
var image_pos = images_background[images_indx_random][1];
var chosencolor = images_background[images_indx_random][2];
