.. -*- mode: rst; coding: utf-8 -*-

====================================
reStructuredTextでblogger
====================================

:slug: 2005rst
:date: 2005-12-16

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/113480537881336127
  :published: 2005-12-16T00:30:00+09:00

このBlogは， もともとは reStructuredText__ 形式で書いています．
ここで公開しているのはそれをHTMLに変換した結果です．
Blogger では， `ATOM API`__ が用意されているので，
ありがたいことにブラウザを使用しなくてもBlogの更新ができます．

__ http://docutils.sourceforge.net/rst.html
__ http://code.blogger.com/archives/atom-docs.html

以下のような手順をとっています．

1. reStructuredText形式で，テキストファイルを作成
2. Python，docutils で html に変換
3. 2のhtmlを ATOM API で Blogger.comへ更新

2と3はひとつのPythonスクリプト内で行っています．
reStructuredText から html への変換は，docutilsで行えます． :: 

        from docutils.core import publish_parts
        parts = publish_parts(
            content,
            writer_name='blogwriter'
            )

docutils付属の html_writer を継承して・ほんの少しだけ修正した 自作のblogwriter を使用しています．
変換された，htmlのタイトル( ``parts['title']`` )と，body部分 ``parts['body']`` を，以下のテンプレートにセットして 

.. code-block:: java

 entrytemplate = u'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
 <entry xmlns="http://purl.org/atom/ns#">
  <title mode="escaped" type="text/plain">%(title)s</title>
  <published>%(published)s</published>
  <generator url="http://www.yoursitesurlhere.com">python</generator>
  <content type="application/xhtml+xml">
    <div xmlns="http://www.w3.org/1999/xhtml">
    %(content)s
    </div>
  </content>
 %(draft)s
 </entry>'''

ATOM API で送れば，Blogの更新が行えます． 
これらの一連の作業を行う ``myblogger.py`` というPythonスクリプト を作成して使用しています．
テキストファイルを入力として，コマンド一発でBlogエントリの新規作成・更新を行えます． 
以下のような感じです 

.. code-block:: java

  myblogger.py merge 273.txt

書きなれた reStructuredText 形式で Blogを書けるのは快適です．
ATOM API はほとんどのBlogサービスがサポートしているはずですので，
もし将来Blogを引越しすることになっても，ローカルにあるテキストを全部再発行するだけですみます．

TopCoder のコンテストでは，現在，使用できる言語はJava, C#, C++, VB の4つだけです．
Pythonが使えるようにならないかなー．
