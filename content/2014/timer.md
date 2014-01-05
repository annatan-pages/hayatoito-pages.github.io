title: Simple timer application for the pomodoro technique
slug: timer
date: 2014-02-02


I've created a simple [timer application] for [the pomodoro technique].
You can use the timer here, <http://hayato.io/timer/>.

[timer application]: /timer/
[the pomodoro technique]: http://pomodorotechnique.com/

![timer](/static/2014/timer.png)

It seems that there are a lot of timer applications for the pomodoro technique, however, I couldn't find any timer which fits me.

I need a simple, tiny, easy-to-customize, non-distractive and web-based timer. Therefore, I made it.

Requirements
====

-   Modern browsers.

Features
=====

-   In addtion of the page, the title of the browser's tab also shows the progress.

    ![notification](/static/2014/timer-title.png)


-   Desktop notifications with sounds (only if a browser supports).

    ![notification](/static/2014/timer-notification.png)

-   Specialized for the pomodoro technique. Pre-set timers are:

    1. `25` minutes
    2. `5` minutes (short break)
    3. `25` minutes
    4. `5` minutes (short break)
    5. `25` minutes
    6. `5` minutes (short break)
    7. `25` minutes
    8. `20` minutes (long break)


Customize
====

You can customise the timer by URL's request parameters.

-   `t` - Comma separated timer intervals.

    Example: <http://hayato.io/timer/?t=50,10,50,10>

    In this case, timers are set to 50 mins, 10 mins, 50 mins and 10 mins.

    ![parameter-t](/static/2014/timer-t.png)

-   `mute` -  Turn the notification sound off.

    Example: <http://hayato.io/timer/?mute=1>

    ![parameter-mute](/static/2014/timer-mute.png)

-   `autostart` - Auto start the timer after the page is loaded.

    Example: <http://hayato.io/timer/?autostart=1>

-   `repeat` - Repeat the timers.

    Example: <http://hayato.io/timer/?repeat=1>

    ![parameter-repeat](/static/2014/timer-repeat.png)


You can combine the parameters freely, such as <http://hayato.io/timer/?t=50,10,50,10,50,30&autostart=1&repeat=1>


Future Plan
====

-   More customize.

    - Sounds, Icons.
