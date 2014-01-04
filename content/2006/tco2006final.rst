.. -*- mode: rst; coding: utf-8 -*-

====================================
 2006 TopCoder Open Final Round
====================================

:slug: tco2006final
:date: 2006-05-07

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/114718377259229629
  :published: 2006-05-07T23:30:00+09:00


`2006 TopCoder Open - Algorithm Competition`__ の決勝戦が行われました。オンライン・ラウンドを勝ち抜けた48人が、ラスベガス・アラジンホテルに招待されオンサイトで5/3-5/5の3日間にわたり戦いを繰り広げました。
最後に勝ち残った8名による決勝戦の模様は通常のTopCoderのアリーナ上でリアルタイムで見ることができました。
といっても、ライブ映像が流れていたわけではなくて、こんな感じで

__ http://www.topcoder.com/tc?module=Static&d1=tournaments&d2=tco06&d3=alg_description

.. image:: http://static.flickr.com/44/143378605_08950cdd11_o.png
   :alt: 2006 toc final


競技者が行っている「問題をOpen」「コンパイル」「テスト」「コードを提出」等の行動をリアルタイムで知ることができたわけです。問題の内容や各競技者が提出したコードもリアルタイムで見ることができました。
アリーナ上では見学者が集まって、それを見ながら「あーだこーだ」いって楽しんでいます。

Finalに残ったのは以下の8名。

* tomek : ポーランド・Purdue大学。現在TopCoderでレーティングトップ。優勝候補の最右翼。
* Petr : ロシア・モスクワ大学。TopCoderでは珍しいC#使い。数々のプログラミングコンテストで名を残しているそうです。Google Code Jam 2005でも3位に入っています。いつも綺麗な読みやすいコードを書いてくれるので、参考になります。
* misof : スロバキア・Comenius大学。
* John Dethridge: オーストラリア・メルボルン大学。
* andrewzta: ロシア。
* cyfra: ポーランド・ワルシャワ大学。
* natori : 上位陣には珍しいJava使い。日本人です。
* fuwenjie: 中国・TsingHua大学。

蒼々たる面子です。。ホスト国のUS勢はひとりもFinalに残れなかったのか。。
問題セットはFinalにふさわしく通常のSRMよりもはるかに難しいものばかりそろっています。

実況開始！
==================

250点問題は比較的容易だったらしく、ほとんどの競技者はそれほど苦労せずにSubmit。
500点問題もfuwenjie, Petr, tomekと続々とSubmit。
こんな感じでリアルタイムに問題と提出されたコードを見ることができました。

.. image:: http://static.flickr.com/51/143382049_7fb44ec2fd_o.png
   :alt: 2006 tco final

優勝するには1000点問題を解く必要がある雰囲気が漂いはじめました。
そんな中残り時間26分でtomekが1000点問題を提出！

.. image:: http://static.flickr.com/54/143380229_903b8124f2_o.png
   :alt: 2006 tco final

この時点でトップに立ちます。

.. image:: http://static.flickr.com/48/143380591_980e98ef5c_o.png
   :alt: 2006 tco final

Petrが続きます。

.. image:: http://static.flickr.com/49/143383228_bb6a895f46_o.png
   :alt: 2006 tco final

Petr人気者です。「go Petr!!!」

.. image:: http://static.flickr.com/47/143383770_5dc1fffed3_o.png
   :alt: 2006 tco final

見学者たちは、「tomekの1000点理解できねー。」「tomekのはgreedy algorithmだ」「Petrのはよさそうだ」とわいわいチャットしてました。

.. image:: http://static.flickr.com/48/143384405_45218e28b4_o.png
   :alt: 2006 tco final

Petrの1k(1000点問題）を見てみましたが、binary searchを使用しています。。。この問題からbinary searchを思いつくとは。。その発想がすごい。。
そうこういってるうちに、なんとnatoriが1kを提出！

.. image:: http://static.flickr.com/54/143386042_389c1b9fcf_o.png
   :alt: 2006 tco final

Petr残り5分というところで、500点問題を再提出。。

.. image:: http://static.flickr.com/55/143387190_d16a5b2c2c_o.png
   :alt: 2006 tco final

コーディング・フェーズ終了。現時点での順位はこのとおり。natoriがトップ。tomek、Petrが続きます。

.. image:: http://static.flickr.com/52/143387588_cb6ad21779_o.png
   :alt: 2006 tco final

チャレンジ・フェーズ
====================

5分間の休憩後、チャレンジ・フェーズの始まりです。
Petr開始直後に立て続けに500点問題で3つ撃破！！いっきょにもりあがります。

.. image:: http://static.flickr.com/46/143388256_b99595593f_o.png
   :alt: 2006 tco final

tomekとnatoriの1kも撃墜されました。チャレンジ・フェーズ終了時点でPetrがトップにたちます。

.. image:: http://static.flickr.com/49/143389107_eea870cfaa_o.png
   :alt: 2006 tco final

いよいよ、あとはシステム・テストの結果まちです。。。。

結果
==================

.. image:: http://static.flickr.com/50/143390301_a35d55d1fe_o.png
   :alt: 2006 tco final

見事、Petrが栄冠に輝きました。賞金2万ドルGetです。。おめでとう！！
結局1kに正解したのはPetrだけでしたね。Petrの1kは

* Binary Search
* SortしてからGreedy
* union-find

と基本的なアルゴリズムの組み合わせって感じですね。見事です。。。
