.. -*- mode: rst; coding: utf-8 -*-

====================================================
Suffix Array
====================================================

:slug: 2007suffixarray
:date: 2007-03-27

.. meta::
  :edituri: http://www.blogger.com/feeds/15880554/posts/default/1391481673953214609
  :published: 2007-03-27T00:15:00+09:00


TopCoder SRM187、 DNAMultiMatcher__ は、

  Stringが3つ(それぞれの長さは最大2500)与えられたとき、
  3つ全てに含まれる最長のSubstringの長さを求めなさい。

__ http://www.topcoder.com/stat?c=problem_statement&pm=2224&rd=4755

という問題です。これに対して、

* 長さをBinary-Searchで絞りながら、
* Stringが含まれるかどうかの判定をJava標準のjava.lang.String#containsを使用

という方針で解く場合は、こうなります。

.. code-block:: java

  public class DNAMultiMatcher {

    public int longestMatch(String[] sequence1, String[] sequence2, String[] sequence3) {
        String s1 = join(sequence1);
        String s2 = join(sequence2);
        String s3 = join(sequence3);

        int low = 0;
        int high = s1.length();

        while (low < high) {
            int mid = low + (high-low+1)/2;
            boolean found = false;
            for (int i = 0; i + mid <= s1.length(); i++) {
                String p = s1.substring(i, i+mid);
                if (s2.contains(p) && s3.contains(p)) {
                    found = true;
                    break;
                }
            }
            if (found) {
                low = mid;
            } else {
                high = mid-1;
            }
        }
        return low;
    }

    String join(String[] sa) {
        StringBuilder sb = new StringBuilder();
        for (String s : sa) sb.append(s);
        return sb.toString();
    }
  }

この場合は、ワーストケースで軽く2分以上かかってしまい、タイムアウトです。
String Aの長さをn、String Bの長さをmとした場合、JavaのA.contains(B)は、
普通にO(m*n)っぽいですね。

AがBを含んでいるか?を高速に判定するときに使用できるのが、 `Suffix Array`__ です。

__ http://en.wikipedia.org/wiki/Suffix_array

ナイーブに実装してみると、

.. code-block:: java

    class SuffixArray {
        int len;
        String[] suffixes;

        SuffixArray(String s) {
            len = s.length();
            suffixes = new String[len];
            for (int i = 0; i < len; i++) {
                suffixes[i] = s.substring(i);
            }
            Arrays.sort(suffixes);
        }

        int find(String p) {
            if (len == 0) {
                return p.length() == 0 ? 0 : -1;
            }
            int low = 0;
            int high = suffixes.length-1;
            while (low < high) {
                int middle = low + (high-low)/2;
                if (suffixes[middle].compareTo(p) >= 0) {
                    high = middle;
                } else {
                    low = middle+1;
                }
            }
            if (suffixes[high].startsWith(p)) {
                return len - suffixes[high].length();
            }
            return -1;
        }
    }

Javaのjava.lang.String#substringメソッドは、
もとのStringと内部の配列char[]を共有したStringを返すので、
この実装でも無駄にメモリを消費しないはずです。

オーダーは、

* Aに対するSuffix Arrayの構築: O(n^2 log(n))
* AがBを含んでいるかの判定: O(m log(n))

になるでしょうか?
改良の余地はまだまだ残っていますが、今回の目的にはこれで十分です。
(Suffix ArrayをO(n)で作成するアルゴリズムもあるようです。。。)

先ほどの例を、Suffix Arrayを使用して書き直すとこうなります。

.. code-block:: java

  public class DNAMultiMatcher {

    public int longestMatch(String[] sequence1, String[] sequence2, String[] sequence3) {
        String s1 = join(sequence1);
        String s2 = join(sequence2);
        String s3 = join(sequence3);

        SuffixArray sa2 = new SuffixArray(s2);
        SuffixArray sa3 = new SuffixArray(s3);

        int low = 0;
        int high = s1.length();

        while (low < high) {
            int mid = low + (high-low+1)/2;
            boolean found = false;
            for (int i = 0; i + mid <= s1.length(); i++) {
                String p = s1.substring(i, i+mid);
                if (sa2.find(p) >= 0 && sa3.find(p) >= 0) {
                    found = true;
                    break;
                }
            }
            if (found) {
                low = mid;
            } else {
                high = mid-1;
            }
        }
        return low;
    }

これで、ワーストケースでも1秒以内に処理できるようになり、システムテストに通ります。
Suffix Arrayの応用例はほかにもいろいろあり、全文検索などでもよく使われるようです。
