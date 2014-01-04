.. -*- mode: rst; coding: utf-8 -*-

========================================
 2006 TopCoder Open Qualification Round
========================================

:slug: tco2006qr
:date: 2006-03-02

.. meta::
   :edituri: http://www.blogger.com/feeds/15880554/posts/default/114145530603255156
   :published: 2006-03-02T23:30:00+09:00

   :replace_{RD}: 9903
   :replace_{RM}: 247765
   :replace_{PM1}: 6105
   :replace_{PM2}: 4662

`2006 TopCoder Open - Algorithm Competition`__ - の予選 (Qualification Round)に挑戦です．
いよいよ，始まりました．
TopCoder Open はTopCoder の "Crown of Jewels" ．
一番，盛り上がるイベント・お祭りだそうです．

__ http://www.topcoder.com/tc?module=Static&d1=tournaments&d2=tco06&d3=alg_description

予選を通過できるのは750名．
普段のレーティングが上位の100名は，自動的に予選を免除されますので，
残された650の椅子を巡る戦いです．

* 予選 (Qualification Round): 750名通過
* Round1: 750名 -> 400名
* Round2: 400名 -> 200名
* Round3: 200名 -> 100名
* Round4: 100名 -> 48名

見事，Round4を勝ち抜いた48名は，ラスベガスにご招待され，オンサイトで決勝です．

通常のSRMと異なり，予選はちょっと形式が異なります．

* 問題は2問，制限時間は1時間
* 開始時間は決まっていない．24時間以内ならいつ挑戦をはじめてもよい
* チャレンジ・フェーズはなし

問題セットは，5種類用意され，そのうちどれか1種類が自動的にアサインされます．
各問題セットから，上位 (650/5 =) 130 名が予選を通過できます．
早速，アリーナに参加してみると

.. image:: http://static.flickr.com/44/107444859_1a8ad71a24_o.png
   :alt: 2006 qr

Set14にアサインされました．
問題1種類につき，Roomが3つ用意されていますね．
計15Roomです．

.. image:: http://static.flickr.com/43/107444871_c1ceae571b_o.png
   :alt: 2006 qr

各Roomごとに，およそ170名ほど割り振られていました．
ということは，参加者の総数は 170 x 15 = 2550 名ほどか．

予選通過のためには各Room 内で，130 /3 = 43 位 くらいに入るのが目安になるか．
自分が挑戦した時間が終了近かったので，もうすでに終わっている人のスコアをあらかじめみることができました．
自分がアサインされたRoom14では，こんな様子でした．

.. image:: http://static.flickr.com/44/107444874_3d04bb2d57_o.png
   :alt: 2006 qr

なるほど，ボーダーラインの43位に入るためには，2問とも確実に，その上ある程度スピードも要求されそうです．
まだシステムテストは終わっていないから，ボーダーはこれより下がるでしょうが，思っていたより，レベルが高そう．．
それとも問題が簡単なのか？．．

と思いつつ，自分もスタート．

SlowKeyboard__ (code__)
=======================

__ http://www.topcoder.com/stat?c=problem_statement&pm=6105&rd=9903
__ http://www.topcoder.com/stat?c=problem_solution&rm=247765&rd=9903&pm=6105&cr=15632820

250点問題．問題の意味をつかむのに，一苦労．

結局，Brute Force で全パターンを調べました．
この時点で，18分ほど時間をとられました．まずい．

DigitFilter__ (code__)
======================

__ http://www.topcoder.com/stat?c=problem_statement&pm=4662&rd=9903
__ http://www.topcoder.com/stat?c=problem_solution&rm=247765&rd=9903&pm=4662&cr=15632820

750点問題．

数字が与えられます．

  k = "12XX355"

Xのところは判明しない桁です．
この数字kが(num)で割り切れるとした場合，このような数字kは何通りありますか？
という問題です.たとえば，

  k = "1X"，num=3

ならば，"12", "15", "18" の3通りです．

  k = "23X34XX24XX34X", num=17

ならば，58823通りです．

DPでいけると思い，方針じたいは結構早めに決まったのですが，実装にとまどる，とまどる．
あせっていたのか．．結局，30分ほどかかり，Submit．

2問あわせてスコアは536.71．
Room14内で，65位ほどでした．．これはだめか．．

.. image:: http://static.flickr.com/38/107444883_c25d968b87_o.png
   :alt: 2006 qr

結果
====

最終的なシステムテストの結果です．( `Room Statistics`__ )

__ http://www.topcoder.com/stat?c=coder_room_stats&cr=15632820&rd=9903&rm=247765

Room7/9/14 は同じ問題セットだったそうです．そのRoom7/9/14をあわせた中での順位は，

.. image:: http://static.flickr.com/52/107444885_2ff125b400_o.png
   :alt: 2006 qr

85位．130位以内なので，予選通過ですよね？ まだ正式連絡はきていないけれど．

* Room14だけ，なぜかハイスコアの人が多かったこと
* 750点問題に落ちた人が，相当多かった

ということで，85位に入り込めたっぽいですね．

750点問題で落ちた人は，可能な数字をすべて生成してから，それらをnumで割り切れるかどうかをチェックしている人が多かったようです．
kの最大の長さの条件は18ですので，k = "XXXXXXXXXXXXXXXXXX" の場合，
必要な数字は10^18通りになってしまいます．
これを全て調べるのは，絶対無理ですね．．

今日の教訓
==========

* もっと正確かつ早い実装力が必要．．
