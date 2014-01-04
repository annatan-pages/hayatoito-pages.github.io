.. -*- mode: rst; coding: utf-8 -*-

====================================================
google-code-prettifyを導入してみる
====================================================

:slug: 2007googlecodeprettify
:date: 2007-03-26

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/5491597710803920210
  :published: 2007-03-26T23:45:00+09:00

`google-code-prettify`__ を導入してみました。
JavaScript + CSSでコード部分の色つけをしてくれるものです。

__ http://code.google.com/p/google-code-prettify/

デフォルトでは、class属性が"prettyprint"となっている、
<pre>タグや<code>タグがシンタックス・ハイライトの対象になるようです。
このブログはreStructuredTextで書いているので、
<pre>タグのclass属性は、clsss="literal-block"となっています。
<pre>タグの方を直すのはいまさら面倒なので、prettify.jsの方を少し修正して導入しました。
PythonとJavaは両方ともサポート言語ですので、どちらもなかなか派手に色がつきます。

