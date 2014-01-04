.. -*- mode: rst; coding: utf-8 -*-

=====================================================
Google Code Jam 2006 - Practice1
=====================================================

:slug: 200608googlecodejam-practice1
:date: 2006-08-16

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/115570083078395374
  :published: 2006-08-16T22:00:00+09:00

Google Code Jam 2006 、練習部屋が用意されていたので早速練習してみました。

まず、250点問題。
スタート都市(index=0)からゴールの都市(index=1)まで、セールスマンを何人派遣できるでしょうか？という問題です。
都市通しのつながり(adj)は、

.. code-block:: java

  "001111",
  "001111",
  "110000",
  "110000",
  "110000",
  "110000"

このようにマトリックス形式で与えられます。都市の数は最大12です。
入力の条件としてスタート都市とゴール都市は、直接つながっていないことが保障されています（adj[0][1] == adj[1][0] == 0です）。
スタート都市とゴールの都市を除いた、途中の通過都市はそれぞれ最大1人のセールスマンだけが通過できます。つまりあるセールスマンが通過した都市は、別のセールスマンは通過できません。
この入力の場合は、正解は4人です([0 -> 2 -> 1], [0 -> 3 -> 1], [0 -> 4 -> 1], [0 -> 5 -> 1]の4通り)。

いつもはJavaですが、せっかくですのでPythonで書いてみました。

.. code-block:: java

  class SalesRouting:

    def howMany(self, adj):

        def doit(u, mask):
            if (u, mask) in memo: return memo[u,mask]
            if adj[u][1] == '1': return doit(0, mask) + 1
            memo[u,mask] = max([0] +
                               [doit(v, mask | 1<<v) for v in range(2, len(adj)) 
                                if adj[u][v] == '1' and (mask & (1<<v)) == 0])
            return memo[u,mask]

        memo = {}
        return doit(0, 0)

状態空間は、現在いるcity: u(N通り) と、
これまで通過したcity全て: mask(2^N通り)の組み合わせになります。
ワーストケースでもたかだか12 * 2^12 = 50,000ほどですので、Pythonでも十分通ります。