.. -*- mode: rst; coding: utf-8 -*-

====================================
Blogger Betaに移行
====================================

:slug: 200610bloggerbeta
:date: 2006-10-30

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/5236776380209684363
  :published: 2006-10-30T19:04:30Z

Blogger Betaに移行してみました。大きな変更点としては

* Labelが使えるようになった
* テンプレート・システムがまったく新しくなっている
* ページを動的に作成するようになったので、テンプレートを変更するとすぐにページに反映される

といったところでしょうか？

テンプレート・システム
========================

新しいテンプレート・システムのうりのひとつは、ブラウザ上でGUIでデザインできることです。
必ずGUIを使う必要はなく、全部自分で手作業で設定することももちろん可能でした。
いい機会ですので、新規にテンプレート・CSSを作成してみました。
テンプレートのタグも新規タグが用意されています。
これまでより細部で機能アップしてますね。
ほとんど全ての箇所をいじることができる自由度は相変わらず健在ですので、
特にデザイン上支障はありません。
GUIデザイン用に使用されるテンプレート内の変数部分は、わずらわしいので全部消去しました。

スタイルシートの動的切り替え
============================

「Printer Friendly View」 は `Alternative Style: Working With Alternate Style Sheets`__ を参考にしてみました。
スタイルシートを動的に切り替えることができます。

__ http://alistapart.com/stories/alternate/

Google Data APIs
================

ブラウザから記事を投稿する人には関係のない話ですが、
私の場合は、記事は `reStructuredText`__  形式でローカルで書いてから、
自作のPythonスクリプトで記事を投稿できるようにしています。
Bloggerでは、そのためにATOM APIが用意されています。
こちらもBetaでは変更が入り、 `Google Data APIs`__ を用いるようになりました。

__ http://docutils.sourceforge.net/rst.html
__ http://code.google.com/apis/gdata/

主な変更点としては、

* ATOM APIのバージョンが0.3から1.0に変更
* 認証システムも、Basic認証から、 `Google Account Authentication`__ に変更

といったところです。
`Blogger Data API`__ として使用方法が解説してありますので、ここを見れば簡単です。

__ http://code.google.com/apis/accounts/Authentication.html
__ http://code.google.com/apis/gdata/blogger.html

JavaやC#用のクライアント・ライブラリも用意されていましたが、
reStructutedTextの変換を考えるとやはりPythonのほうがよいと思い、
Pythonでクライアントを書きました。
ATOMを使用するにあたり、いくつかすんなりとはいかなかった点としては、

1. 指定されたPost先にPost要求を出すと、Betaのサーバはリダイレクトを返してきます。
2. 投稿に成功した場合、ステータスコード201を返してきます。

この2点です。
Pythonの標準のAPI(urllib/urllib2)では、Post要求に対してリダイレクトが返って来ると、
リダイレクト先へPostを再送するのではなくGet要求を出してしまいます。
また、ステータスコード201もエラー扱いするようになっていました。
そのため、自分で ``urllib2.HTTPRedirectHandler`` をもとにした、ちょっとしたハックが必要になります。

その他に気づいた問題点は、新規記事をATOM 1.0で送る時、<published>での日付指定が無視されてしまうことです。
これは、現在サーバ側の問題らしく、 `Blogger Dev Group`__ で議論されていますのでいずれ解決しそうです。

これでほぼ移行作業が完了しましたが、全体としてはBetaの方がはるかに使いやすくなりましたね。
なによりラベルが使えるようになったのがいちばんうれしいですね。

__ http://groups.google.com/group/bloggerDev/
