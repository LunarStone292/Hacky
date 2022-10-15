import os

try:
    from translate import Translator
except:
    ins = os.system("pip install translate")
    if(ins == 1):
        inss = os.system("pip3 install translate")
        if(inss == 1):
            print("\n Error")
            exit()
    os.system("cls")

#https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

def tran():
    print('''\n Available languages:
\n Abkhazian (ab)
 Afar (aa)
 Afrikaans (af)
 Akan (ak)
 Albanian (sq)
 Amharic (am)
 Arabic (ar)
 Aragonese (an)
 Armenian (hy)
 Assamese (as)
 Avaric (av)
 Avestan (ae)
 Aymara (ay)
 Azerbaijani (az)
 Bambara (bm)
 Bashkir (ba)
 Basque (eu)
 Belarusian (be)
 Bengali (bn)
 Bislama (bi)
 Bosnian (bs)
 Breton (br)
 Bulgarian (bg)
 Burmese (my)
 Catalan, Valencian (ca)
 Central Khmer (km)
 Chamorro (ch)
 Chechen (ce)
 Chichewa, Chewa, Nyanja (ny)
 Chinese (zh)
 Church Slavic, Old Slavonic, Church Slavonic, Old Bulgarian, Old Church Slavonic (cu)
 Chuvash (cv)
 Cornish (kw)
 Corsican (co)
 Cree (cr)
 Croatian (hr)
 Czech (cs)
 Danish (da)
 Divehi, Dhivehi, Maldivian (dv)
 Dutch, Flemish (nl)
 Dzongkha (dz)
 English (en)
 Esperanto (eo)
 Estonian (et)
 Ewe (ee)
 Faroese (fo)
 Fijian (fj)
 Finnish (fi)
 French (fr)
 Fulah (ff)
 Gaelic, Scottish Gaelic (gd)
 Galician (gl)
 Ganda (lg)
 Georgian (ka)
 German (de)
 Greek, Modern (el)
 Guarani (gn)
 Gujarati (gu)
 Haitian, Haitian Creole (ht)
 Hausa (ha)
 Hebrew (he)
 Herero (hz)
 Hindi (hi)
 Hiri Motu (ho)
 Hungarian (hu)
 Icelandic (is)
 Ido (io)
 Igbo (ig)
 Indonesian (id)
 Interlingue, Occidental (ie)
 Inuktitut (iu)
 Inupiaq (ik)
 Irish (ga)
 Italian (it)
 Japanese (ja)
 Javanese (jv)
 Kalaallisut, Greenlandic (kl)
 Kannada (kn)
 Kanuri (kr)
 Kashmiri (ks)
 Kazakh (kk)
 Kikuyu, Gikuyu (ki)
 Kinyarwanda (rw)
 Kirghiz, Kyrgyz (ky)
 Komi (kv)
 Kongo (kg)
 Korean (ko)
 Kuanyama, Kwanyama (kj)
 Kurdish (ku)
 Lao (lo)
 Latin (la)
 Latvian (lv)
 Limburgan, Limburger, Limburgish (li)
 Lingala (ln)
 Lithuanian (lt)
 Luba-Katanga (lu)
 Luxembourgish, Letzeburgesch (lb)
 Macedonian (mk)
 Malagasy (mg)
 Malay (ms)
 Malayalam (ml)
 Maltese (mt)
 Manx (gv)
 Maori (mi)
 Marathi (mr)
 Marshallese (mh)
 Mongolian (mn)
 Nauru (na)
 Navajo, Navaho (nv)
 Ndonga (ng)
 Nepali (ne)
 North Ndebele (nd)
 Northern Sami (se)
 Norwegian (no)
 Norwegian Bokmål (nb)
 Norwegian Nynorsk (nn)
 Occitan (oc)
 Ojibwa (oj)
 Oriya (or)
 Oromo (om)
 Ossetian, Ossetic (os)
 Pali (pi)
 Pashto, Pushto	(ps)
 Persian (fa)
 Polish	(pl)
 Portuguese	(pt)
 Punjabi, Panjabi (pa)
 Quechua (qu)
 Romanian, Moldavian, Moldovan (ro)
 Romansh (rm)
 Rundi (rn)
 Russian (ru)
 Samoan	(sm)
 Sango (sg)
 Sanskrit (sa)
 Sardinian (sc)
 Serbian (sr)
 Shona (sn)
 Sichuan Yi, Nuosu (ii)
 Sindhi (sd)
 Sinhala, Sinhalese	(si)
 Slovak	(sk)
 Slovenian (sl)
 Somali (so)
 South Ndebele (nr)
 Southern Sotho	(st)
 Spanish (es)
 Sundanese (su)
 Swahili (sw)
 Swati (ss)
 Swedish (sv)
 Tagalog (tl)
 Tahitian (ty)
 Tajik (tg)
 Tamil (ta)
 Tatar (tt)
 Telugu	(te)
 Thai (th)
 Tibetan (bo)
 Tigrinya (ti)
 Tonga (to)
 Tsonga	(ts)
 Tswana	(tn)
 Turkish (tr)
 Turkmen (tk)
 Twi (tw)
 Uighur, Uyghur	(ug)
 Ukrainian (uk)
 Urdu (ur)
 Uzbek (uz)
 Venda (ve)
 Vietnamese	(vi)
 Volapük (vo)
 Walloon (wa)
 Welsh (cy)
 Western Frisian (fy)
 Wolof (wo)
 Xhosa (xh)
 Yiddish (yi)
 Yoruba	(yo)
 Zhuang, Chuang	(za)
 Zulu (zu)

    ''')

    c_to_translate = input("\n Enter the language: ")

    translator= Translator(to_lang=c_to_translate)

    cc = input("\n Enter the word to be translated: ")

    translation = translator.translate(cc)

    print("\n Translated sentence: \n\n", translation)

tran()