.. -*- mode: rst; coding: utf-8 -*-

====================================================
Subsetの生成
====================================================

:slug: 2007subset
:date: 2007-03-02

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/1943394391388127967
  :published: 2007-03-02T01:00:00.000+09:00


いままで、あるビットマスクsupersetのサブセットをすべて生成するには、

.. code-block:: java

  for (int subset = 1; subset < superset; subset++) {
   if ((subset|superset) == superset) {
     // do with subset
   }
  }

としていたんですけど、これだと、
superset = 10011(2)などの場合でも、約10011(2)回のループが必要です。
生成されるサブセットは、

  {10010, 10001, 00011, 10000, 00010, 00001,}

と6つしかないのに。すごい無駄です。

もっとうまい方法がありました。

.. code-block:: java

  for (int subset = superset; subset > 0; subset = (subset-1) & superset) {
    // do with subset
  }

これなら、サブセットのみをうまく生成できます。
この場合のサブセットはsupersetを含み、空セットは含みません。
