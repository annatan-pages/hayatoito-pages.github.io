title: About
icon: fa-user

Hayato Ito is a software engineer working at Google.

- <i class="fa fa-inbox"></i> <hayato@google.com>
- <i class="fa fa-github"></i> [hayatoito.github.com](http://hayatoito.github.com/)
- <i class="fa fa-google-plus"></i> [google.com/+HayatoIto](http://google.com/+HayatoIto)
- <i class="fa fa-twitter"></i> [@hayatoito](http://twitter.com/hayatoito)
- <i class="fa fa-twitter"></i> [@shadow_hayato](http://twitter.com/shadow_hayato)

---

Selected Accomplishments at Google
====

Shadow DOM specification (Q2’2013 - Present) (~ 45 commits)
-----

[Shadow DOM specification] enables [encapsulation] for DOM trees. Shadow DOM is designed to provide encapsulation by hiding DOM subtrees under shadow roots. I’ve been actively updating the Shadow DOM specification as a spec editor. Shadow DOM [is actually used][Shadow DOM in Polymer] in [Polymer Project] ([TechCrunch article]).

  * Rewrote the most of the Shadow DOM specification in Q3’2013 to make sure that the model and data structures, accompanying algorithms are clearly defined. I’ve invented the following algorithms (including, but not limited to): [distributions algorithms], [composed tree algorithm], [event path calculation algorithms].
  * [The most significant patch](https://dvcs.w3.org/hg/webcomponents/rev/dbf47f602628).
  * [Design Doc](https://docs.google.com/document/d/1iuf2DgzwKfMTscAX_xsymO73NmZ4NVYvfyFgUU4YINo/edit?usp=sharing) about refactoring and rewriting the specification.
  * [Anne van Kesteren] (Mozilla employee, [the DOM specification] editor and a member of [W3C TAG]) [was excited](http://lists.w3.org/Archives/Public/public-webapps/2013JulSep/0167.html) about my initiative at [public-webapps@w3.org]. Merging the Shadow DOM into the DOM is on my radar.

[Shadow DOM specification]: http://w3c.github.io/webcomponents/spec/shadow/index.html
[Encapsulation]: http://www.html5rocks.com/en/tutorials/#shadowdom
[Shadow DOM in Polymer]: http://www.polymer-project.org/platform/shadow-dom.html
[Polymer Project]: http://www.polymer-project.org/
[TechCrunch Article]:(http://techcrunch.com/2013/05/19/google-believes-web-components-are-the-future-of-web-development/

[distributions algorithms]: http://w3c.github.io/webcomponents/spec/shadow/index.html#dfn-distribution-algorithm
[composed tree algorithm]: http://w3c.github.io/webcomponents/spec/shadow/index.html##dfn-composed-tree-children-calculation-algorithm
[event path calculation algorithms]: http://w3c.github.io/webcomponents/spec/shadow/index.html#dfn-event-path-calculation-algorithm
[Anne van Kesteren]: http://wiki.whatwg.org/wiki/User:Annevk
[the DOM specification]: http://dom.spec.whatwg.org/
[W3C TAG]: http://www.w3.org/2001/tag/
[public-webapps@w3.org]: http://lists.w3.org/Archives/Public/public-webapps/


Shadow DOM implementations in Chrome WebKit / Blink (Q2’2011 - Present) (~ 300 commits)
-----

Shadow DOM implementation is a project to implement [Shadow DOM specification] in WebKit/Blink. Shadow DOM is one of the most important breakthrough for the current Web development. Our goal is to deliver a  component model (as [Web Components]) to the Web platform, where is the Google’s primary business platform. I’ve been working and involved on the most of the implementations of the Shadow DOM specification both as a spec editor and an implementer.

* Specced and implemented a new [distribution resolution algorithm], where <shadow\> elements act as if it were a constructor of a superclass (the implementation is [on-going](https://code.google.com/p/chromium/issues/detail?id=263701)).
* Specced and implemented a [focus navigation] for Shadow DOM, which is based on a [tree of trees] (Q3’2013)
* Specced and implemented an [Event Path] API (Q1’2013)
* Specced and implemented [Touch Events retargeting] for multiple touches for Shadow DOM (Q1’2013), which enables touch events to be dispatched in shadow trees.
   * Safari Official Blog picked up this accomplishment as '[Touch Events support for shadow DOM]'.
* Specced and implemented an [Element.getDestinationInsertionPoints()] API (Q3’2013)
* Implemented a ‘[::distributed()]’ functional pseudo elements.
   * This is the first-ever pseudo element which can take parameters.
   * This is also the first-ever CSS rule which crosses shadow boundaries.
* Contributed to the [CSS relative selector] spec and implemented that in WebKit/Blink. Supported that in ‘[::distributed()]’ pseudo elements.
* Implemented a /select/ reference combinator, which was replaced by ‘::distributed()’ pseudo element later.
* Implemented an [InsertionPoint.getDistributedNodes()] API.
* [Shipped in Chrome M25]. “Today, 310M people got Shadow DOM.”
* Implemented [reprojection] for distributed nodes both for content insertion points and shadow insertion points (Q4’2012) . [Specced that][Distrubution Result] clearly later in the Shadow DOM specification.
* Implemented a focus navigation based on a [composed tree] (Q1’2012).
* Implemented a ComposedShadowTreeWalker, which enables traversing nodes in [composed tree] order.
   * [Design Doc][Composed Tree Walker Design Doc].
   * Wrote the API document at WebKit’s official wiki, [Traversing Shadow DOM Tree].
* Implemented the most of [ShadowRoot JS bindings].
* Implemented [<shadow> element] and its behavior as a [shadow insertion point].
* Fixed the critical crashes related to editing facility in Shadow DOM (with shinyak@ rniwa@). [HTML editing specification] and implementation is one of the most difficult areas in WebKit according to Apple engineers.
* Made <iframe\> elements [ready for Shadow DOM][HTML Element and Their Shadow Trees].
* Made [events model][Shadow DOM Events] work with Shadow DOM.
   * Described as a separate accomplishment.


[Web Components]: http://www.w3.org/TR/components-intro/
[distribution resolution algorithm]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-distribution-resolution-algorithm
[focus navigation]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#focus-navigation
[tree Of trees]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-tree-of-trees
[Event Path]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-event-path-calculation-algorithm

[Touch Events retargeting]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#retargeting-touch-events
[Touch Events support for shadow DOM]: https://www.webkit.org/blog/2278/last-week-in-webkit-touch-events-for-shadow-dom-and-an-updated-calendar-picker-ui/

[Element.getDestinationInsertionPoints()]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#api-partial-element-get-destination-insertion-points

[::distributed()]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-content-pseudo-element
[CSS relative selector]: http://www.w3.org/TR/selectors4/#scope-relative

[InsertionPoint.getDistributedNodes()]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#api-html-content-element-get-distributed-nodes

[Shipped in Chrome M25]: https://twitter.com/ebidel/status/304759211341017088
[Reprojection]: http://www.w3.org/TR/shadow-dom/#reprojection

[Distribution Result]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-distribution-result
[Composed Tree]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-composed-tree

[Composed Tree Walker Design Doc]:  https://docs.google.com/a/google.com/document/d/1lXywNJgUnjMSiKFwtrrah-w5l3m0jPhEXXOXQloVf1k/edit?usp=sharing

[Traversing Shadow DOM Tree]: http://trac.webkit.org/wiki/TraversingShadowDOMTree

[ShadowRoot JS Bindings]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#shadow-root-object

[<shadow> element]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#shadow-element
[Shadow Insertion Point]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#dfn-shadow-insertion-point

[Editing]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#editing

[HTML editing specification]: https://dvcs.w3.org/hg/editing/raw-file/tip/editing.html

[HTML Element and Their Shadow Trees]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#html-elements-and-their-shadow-trees

[Shadow DOM Events]: https://dvcs.w3.org/hg/webcomponents/raw-file/tip/spec/shadow/index.html#events


Shadow DOM / New event model (Q2’2012 - Present) (~ 60 commits)
-----

Designed the [new event dispatching model][Shadow DOM Events] for Shadow DOM and implemented that in Chrome WebKit/Blink. I’ve been in charge of all [DOM Events] related features and issues so far in WebKit / Blink, not limited to the Shadow DOM.

* [Design doc](https://docs.google.com/document/d/1PY7KkTRI-doU9Hew3Mud9JBgjj5xtVqH8sY0Ui305nw/edit?usp=sharing) (Events in Shadows, which would help other browser vendors understand the event model for Shadow DOM):
* [Design doc](https://docs.google.com/a/google.com/document/d/1lEhofMfCOSbcZEULOjGZ1xs76VdQwN1SQRROqQ_oIec/edit?usp=sharing) (Revised one to explain new event targeting model, which was used in 2012 WebKit contributors meeting held in Apple)
* I’ve successfully invented a new event dispatching model which works seamlessly for both DOM worlds, light DOM world and Shadow DOM world, establishing encapsulation at the same time. The new event model has worked in stable condition in the real Web platform for years.
* [Public post](https://plus.google.com/103330502635338602217/posts/XmzHwEezx2d) on Google+ mentioned that, “+Hayato Ito is the Shadow DOM Events Wizard”.

[DOM Events]: http://www.w3.org/TR/DOM-Level-3-Events/


Chrome WebKit / StyleResolver Refactoring (Q1’2013)
----

StyleResolver is a god-object class in WebKit/Blink, which has been developed incrementally and grew severely barnacled. I‘ve decoupling and splitting it up into more hackable set of classes with tasak@ and dglazkov@.


Chrome WebKit - Open Source Project (Q3’2010 - Q1’2013 )
----

* Designed and implemented a non-recursive iterative algorithm to match CSS rules in CSS Selector.
* Became Chromium Committer (Q4’2009).
* Became WebKit Committer (Q3’2010 ). Nominated by Darin Adler from Apple
* Implemented GDB’s pretty printer for fundamental classes used in WebKit, such as String, Vector and so on.
* Updated upload.py which is used in chromium’s code reivew and upstreamed that to the rietveld, reviewed by guido@.

Chrome WebKit - Reftests (Q3’2010 - Q1’2011)
----
Supported [Reftests] in WebKit. Reftests are mainly being used in Mozilla project. Writing tests in reftests format is highly recommended in W3C. Sharing tests between browser vendors is very important for Web and Google.

* Published the document to WebKit’s official Wiki: [Writing Reftests].
* About 1600 reftests have been written in WebKit/Blink so far  (as of 2013 Q3). We love reftests.

[Reftests]: http://wiki.csswg.org/test/reftest
[Writing Reftests]: http://trac.webkit.org/wiki/Writing%20Reftests

Chrome WebKit, CSS3 Paged Media (Q1’2010 - Q2’2010)
----

Implemented [CSS3 Paged Media specification]. Designed and implemented a page break position calculation algorithm based on dynamic programming technique.

* Supported CSS3’s properties such as page-break-{before, after}, orphan, widow and so on.

[CSS3 Paged Media specification]: http://www.w3.org/TR/css3-page/

Chrome WebKit - LTTF (Layout Tests Task force) (Q4’2009)
----

Layout tests are regression tests for WebKit.

* Fixed about 40 issues about Layout tests.
