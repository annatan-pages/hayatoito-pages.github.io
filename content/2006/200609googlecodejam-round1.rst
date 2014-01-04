.. -*- mode: rst; coding: utf-8 -*-

==========================================================
Google Code Jam 2006 - Round1に挑戦 - GenericsとAutoBoxing
==========================================================

:slug: 200609googlecodejam-round1
:date: 2006-09-15

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/115829354260826244
  :published: 2006-09-15T18:30:00+09:00

Google Code Jam 2006 Round1に挑戦。
予選を通過した1000名のうち500名が通過できます。

NearFrac
========

250点問題。
問題の条件をまちがって解釈してしまいました。
解が複数あった場合、たとえば「-1/3, -2/3」の場合は、「小さいほう」である「-2/3」を優先しなければいけないんですが、
「小さいほう」の説明を逆に解釈してしまい、「-1/3」を優先するようなコードを書いてしまいました。
よく問題を読めばちゃんと説明してあるんですけどね。反省。

BadBinary
=========

500点問題。
問題自体は難しくなくコーディングはさくさく10分ほどで完了。
しかし、Javaの罠にはまってしまいました。。。
たとえば、 

.. code-block:: java

  Map<Long, Long> memo = new HashMap<Long, Long>();
  long i = 1;
  memo.put(i, 2);

として、このMapから値を取得しようと、 

.. code-block:: java

  int j = 1;
  memo.get(j);

とします。するとmemo.get(j)の結果は、2ではなくnullになってしまいます。
memoは 

.. code-block:: java

  Map<Long, Long> memo

と宣言しているので、memo.get(j)の部分は、AutoBoxingが働いて 

.. code-block:: java

  memo.get(new Long(j))

と解釈されると思っていたのですが、実際は 

.. code-block:: java

  memo.get(new Integer(j))

とIntegerになるようですね。int->longの変換は行われません。
当然、memo.put(new Long(1), ..)したものは、memo.get(new Integer(1))では取得できません。

「Genericsのもつコンパイル時の型チェックは機能しないのか？」
と思ったら、そもそもMapのメソッドgetは 

.. code-block:: java

  public interface Map<K,V> {
    V get(Object key);

と定義されているんですね。てっきり 

.. code-block:: java

  public interface Map<K,V> {
    V get(K key);

だと思いこんでいました。パラメータの型チェックは行われないのか。。がく。

本番中はまさかこの部分に問題があるとは気づくことができず右往左往。
なぜかこういうときだけ無駄な想像力が異様に働き、関係ないところばかり追いかけてしまいました。
むなしく時間（50分も。。）を費やしたあげく、結局最後まで気づくことができないまま時間切れ。
memo.get(j)ではなくmemo.get((long)j)とするだけでよかったんですけど。気づくべきでした。
Google Code Jamくん、楽しませてもらったよ。また来年までさようなら。
