(function() {
    var i = void 0
      , k = null;
    function aa(a) {
        return function() {
            return this[a]
        }
    }
    function ba(a) {
        return function() {
            return a
        }
    }
    var n, o = this;
    function da(a, b) {
        var c = a.split(".")
          , d = o;
        !(c[0]in d) && d.execScript && d.execScript("var " + c[0]);
        for (var e; c.length && (e = c.shift()); )
            !c.length && p(b) ? d[e] = b : d = d[e] ? d[e] : d[e] = {}
    }
    function ea(a) {
        for (var a = a.split("."), b = o, c; c = a.shift(); )
            if (b[c] != k)
                b = b[c];
            else
                return k;
        return b
    }
    function fa() {}
    function ga(a) {
        var b = typeof a;
        if (b == "object")
            if (a) {
                if (a instanceof Array)
                    return "array";
                else if (a instanceof Object)
                    return b;
                var c = Object.prototype.toString.call(a);
                if (c == "[object Window]")
                    return "object";
                if (c == "[object Array]" || typeof a.length == "number" && typeof a.splice != "undefined" && typeof a.propertyIsEnumerable != "undefined" && !a.propertyIsEnumerable("splice"))
                    return "array";
                if (c == "[object Function]" || typeof a.call != "undefined" && typeof a.propertyIsEnumerable != "undefined" && !a.propertyIsEnumerable("call"))
                    return "function"
            } else
                return "null";
        else if (b == "function" && typeof a.call == "undefined")
            return "object";
        return b
    }
    function p(a) {
        return a !== i
    }
    function ha(a) {
        return ga(a) == "array"
    }
    function ia(a) {
        var b = ga(a);
        return b == "array" || b == "object" && typeof a.length == "number"
    }
    function ja(a) {
        return typeof a == "string"
    }
    function ka(a) {
        return typeof a == "number"
    }
    function la(a) {
        return ga(a) == "function"
    }
    function ma(a) {
        a = ga(a);
        return a == "object" || a == "array" || a == "function"
    }
    function na(a) {
        return a[oa] || (a[oa] = ++pa)
    }
    var oa = "closure_uid_" + Math.floor(Math.random() * 2147483648).toString(36)
      , pa = 0;
    function qa(a, b, c) {
        return a.call.apply(a.bind, arguments)
    }
    function sa(a, b, c) {
        if (!a)
            throw Error();
        if (arguments.length > 2) {
            var d = Array.prototype.slice.call(arguments, 2);
            return function() {
                var c = Array.prototype.slice.call(arguments);
                Array.prototype.unshift.apply(c, d);
                return a.apply(b, c)
            }
        } else
            return function() {
                return a.apply(b, arguments)
            }
    }
    function ta(a, b, c) {
        ta = Function.prototype.bind && Function.prototype.bind.toString().indexOf("native code") != -1 ? qa : sa;
        return ta.apply(k, arguments)
    }
    function ua(a, b) {
        var c = Array.prototype.slice.call(arguments, 1);
        return function() {
            var b = Array.prototype.slice.call(arguments);
            b.unshift.apply(b, c);
            return a.apply(this, b)
        }
    }
    var va = Date.now || function() {
        return +new Date
    }
    ;
    function s(a, b) {
        function c() {}
        c.prototype = b.prototype;
        a.kb = b.prototype;
        a.prototype = new c
    }
    ;var xa = {}, ya, za, Aa;
    function t(a, b) {
        this.x = p(a) ? a : 0;
        this.y = p(b) ? b : 0
    }
    t.prototype.r = function() {
        return new t(this.x,this.y)
    }
    ;
    function Ba(a) {
        var b = new t(0,0)
          , c = a.x - b.x
          , a = a.y - b.y;
        return Math.sqrt(c * c + a * a)
    }
    ;function Ca(a, b, c, d) {
        this.top = a;
        this.right = b;
        this.bottom = c;
        this.left = d
    }
    Ca.prototype.r = function() {
        return new Ca(this.top,this.right,this.bottom,this.left)
    }
    ;
    Ca.prototype.contains = function(a) {
        return !this || !a ? !1 : a instanceof Ca ? a.left >= this.left && a.right <= this.right && a.top >= this.top && a.bottom <= this.bottom : a.x >= this.left && a.x <= this.right && a.y >= this.top && a.y <= this.bottom
    }
    ;
    Ca.prototype.expand = function(a, b, c, d) {
        ma(a) ? (this.top -= a.top,
        this.right += a.right,
        this.bottom += a.bottom,
        this.left -= a.left) : (this.top -= a,
        this.right += b,
        this.bottom += c,
        this.left -= d);
        return this
    }
    ;
    function Da(a, b) {
        this.width = a;
        this.height = b
    }
    n = Da.prototype;
    n.r = function() {
        return new Da(this.width,this.height)
    }
    ;
    function Ea(a) {
        return a.width * a.height
    }
    n.ceil = function() {
        this.width = Math.ceil(this.width);
        this.height = Math.ceil(this.height);
        return this
    }
    ;
    n.floor = function() {
        this.width = Math.floor(this.width);
        this.height = Math.floor(this.height);
        return this
    }
    ;
    n.round = function() {
        this.width = Math.round(this.width);
        this.height = Math.round(this.height);
        return this
    }
    ;
    n.scale = function(a) {
        this.width *= a;
        this.height *= a;
        return this
    }
    ;
    Ca.prototype.size = function() {
        return new Da(this.right - this.left,this.bottom - this.top)
    }
    ;
    function Fa() {}
    Fa.prototype.R = fa;
    function Ga(a) {
        return a.ue ? a.ue : a
    }
    function Ha(a, b) {
        Ia(b, a);
        b.ue = Ga(a);
        return b
    }
    ;var u = new Fa;
    u.Gb = function() {}
    ;
    u.Jf = function() {
        var a = this.Wb, b = this.zc(), c = this.Ia || 1, d = c / a, e;
        if (this.k) {
            this.Jc && this.Jc.contains(b) && (e = Ea(this.Jc.size()) / Ea(b.size())) && e < 1.6 && e > 0.5 ? b = this.Jc : this.wh != 1 && this.s.length != 0 && (this instanceof Ja || b.expand(12, 12, 12, 12));
            this.Jc = b;
            var g = b.size();
            e = g.r().scale(c).ceil();
            if (this.k.width != e.width || this.k.height != e.height)
                this.k.width = e.width,
                this.k.height = e.height,
                this.bd = 1;
            var h = this.T.r();
            this.L[Ka] && (h = this.L[Ka]);
            e.width != 0 ? h.scale(g.width * d / e.width) : h.scale(1 / a);
            a = this.m();
            this.pd = (a.left - b.left) * c;
            this.qd = (a.top - b.top) * c;
            b = this.t().r();
            a = this.yb();
            b.width *= a.x;
            b.height *= a.y;
            b = b.scale(c);
            c = this.f.r();
            this.L[La] && (c = this.L[La]);
            c.x *= d;
            c.y *= d;
            c.x -= b.width + this.pd;
            c.y -= b.height + this.qd;
            Ma(this.k, (this.pd + b.width) / e.width * 100, (this.qd + b.height) / e.height * 100, !0);
            !this.ua[La] && !this.ua[Ka] && !this.ua[Na] && (d = -Oa(this),
            p(this.L[Na]) && (d = -this.L[Na]),
            Pa(this.k, Qa(new Ra, 0.1).translate(c.x, c.y).scale(h.x, h.y).rotate(d)));
            if (this.bd)
                d = this.k.getContext("2d"),
                c = this.Ia || 1,
                d.clearRect(0, 0, e.width, e.height),
                d.save(),
                d.translate(this.pd, this.qd),
                d.scale(c, c),
                e = this.t(),
                h = this.yb(),
                d.translate(e.width * h.x, e.height * h.y),
                this.N.Je.call(this, d),
                d.restore(),
                this.bd = 0
        }
    }
    ;
    u.update = function() {}
    ;
    u.Je = function(a) {
        if (this.Y && (this.A != this.La && (this.La && v.sf.call(this),
        this.A && v.oe.call(this)),
        !this.ib && !this.Pc && !(this.ca == 0 || this.Ld == 1))) {
            this.ca != 1 && (a.globalAlpha *= this.ca);
            if (this.A) {
                v.we.call(this.A);
                var b = this.La
                  , c = this.T;
                a.save();
                a.save();
                a.translate(b.af.x, b.af.y);
                a.rotate(-b.bf);
                this.Ac && a.rotate(Oa(this) * Math.PI / 180);
                a.beginPath();
                a.moveTo(0, 0);
                a.lineTo(b.Rd / c.x, 0);
                a.lineTo(b.Rd / c.x, b.Qd / c.y);
                a.lineTo(0, b.Qd / c.y);
                a.closePath();
                a.restore();
                a.clip()
            }
            b = new t(0,0);
            this.N.R.call(this, a);
            for (var d = 0, e; e = this.s[d]; d++) {
                var g = Sa(e, b).r()
                  , h = Oa(e)
                  , c = e.T;
                a.save();
                a.translate(g.x, g.y);
                a.scale(c.x, c.y);
                h != 0 && a.rotate(-h * Math.PI / 180);
                this.N.Je.call(e, a);
                a.restore()
            }
            this.ca != 1 && (a.globalAlpha /= this.ca);
            this.La && a.restore()
        }
    }
    ;
    function Ta(a) {
        return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g, "")
    }
    function Ua(a) {
        if (!Va.test(a))
            return a;
        a.indexOf("&") != -1 && (a = a.replace(Wa, "&amp;"));
        a.indexOf("<") != -1 && (a = a.replace(Xa, "&lt;"));
        a.indexOf(">") != -1 && (a = a.replace(Ya, "&gt;"));
        a.indexOf('"') != -1 && (a = a.replace(Za, "&quot;"));
        return a
    }
    var Wa = /&/g
      , Xa = /</g
      , Ya = />/g
      , Za = /\"/g
      , Va = /[&<>\"]/;
    function $a(a, b) {
        for (var c = 0, d = Ta(String(a)).split("."), e = Ta(String(b)).split("."), g = Math.max(d.length, e.length), h = 0; c == 0 && h < g; h++) {
            var m = d[h] || ""
              , l = e[h] || ""
              , q = RegExp("(\\d*)(\\D*)", "g")
              , A = RegExp("(\\d*)(\\D*)", "g");
            do {
                var r = q.exec(m) || ["", "", ""]
                  , X = A.exec(l) || ["", "", ""];
                if (r[0].length == 0 && X[0].length == 0)
                    break;
                c = ab(r[1].length == 0 ? 0 : parseInt(r[1], 10), X[1].length == 0 ? 0 : parseInt(X[1], 10)) || ab(r[2].length == 0, X[2].length == 0) || ab(r[2], X[2])
            } while (c == 0)
        }
        return c
    }
    function ab(a, b) {
        if (a < b)
            return -1;
        else if (a > b)
            return 1;
        return 0
    }
    var bb = {};
    function cb(a) {
        return bb[a] || (bb[a] = String(a).replace(/\-([a-z])/g, function(a, c) {
            return c.toUpperCase()
        }))
    }
    ;var db = Array.prototype
      , eb = db.indexOf ? function(a, b, c) {
        return db.indexOf.call(a, b, c)
    }
    : function(a, b, c) {
        c = c == k ? 0 : c < 0 ? Math.max(0, a.length + c) : c;
        if (ja(a))
            return !ja(b) || b.length != 1 ? -1 : a.indexOf(b, c);
        for (; c < a.length; c++)
            if (c in a && a[c] === b)
                return c;
        return -1
    }
      , fb = db.forEach ? function(a, b, c) {
        db.forEach.call(a, b, c)
    }
    : function(a, b, c) {
        for (var d = a.length, e = ja(a) ? a.split("") : a, g = 0; g < d; g++)
            g in e && b.call(c, e[g], g, a)
    }
      , gb = db.filter ? function(a, b, c) {
        return db.filter.call(a, b, c)
    }
    : function(a, b, c) {
        for (var d = a.length, e = [], g = 0, h = ja(a) ? a.split("") : a, m = 0; m < d; m++)
            if (m in h) {
                var l = h[m];
                b.call(c, l, m, a) && (e[g++] = l)
            }
        return e
    }
      , hb = db.map ? function(a, b, c) {
        return db.map.call(a, b, c)
    }
    : function(a, b, c) {
        for (var d = a.length, e = Array(d), g = ja(a) ? a.split("") : a, h = 0; h < d; h++)
            h in g && (e[h] = b.call(c, g[h], h, a));
        return e
    }
    ;
    function ib(a, b) {
        eb(a, b) >= 0 || a.push(b)
    }
    function jb(a, b) {
        var c = eb(a, b);
        c >= 0 && db.splice.call(a, c, 1)
    }
    function kb(a) {
        return db.concat.apply(db, arguments)
    }
    function lb(a) {
        if (ha(a))
            return kb(a);
        else {
            for (var b = [], c = 0, d = a.length; c < d; c++)
                b[c] = a[c];
            return b
        }
    }
    function mb(a) {
        return ha(a) ? kb(a) : lb(a)
    }
    function nb(a, b, c, d) {
        db.splice.apply(a, ob(arguments, 1))
    }
    function ob(a, b, c) {
        return arguments.length <= 2 ? db.slice.call(a, b) : db.slice.call(a, b, c)
    }
    ;function pb(a, b) {
        this.x = a;
        this.y = b
    }
    s(pb, t);
    pb.prototype.r = function() {
        return new pb(this.x,this.y)
    }
    ;
    pb.prototype.scale = function(a) {
        this.x *= a;
        this.y *= a;
        return this
    }
    ;
    var qb, rb, sb, tb, ub, vb;
    function wb() {
        return o.navigator ? o.navigator.userAgent : k
    }
    ub = tb = sb = rb = qb = !1;
    var xb;
    if (xb = wb()) {
        var yb = o.navigator;
        qb = xb.indexOf("Opera") == 0;
        rb = !qb && xb.indexOf("MSIE") != -1;
        tb = (sb = !qb && xb.indexOf("WebKit") != -1) && xb.indexOf("Mobile") != -1;
        ub = !qb && !sb && yb.product == "Gecko"
    }
    var zb = qb, Ab = rb, Bb = ub, Cb = sb, Db = tb, Eb, Fb = o.navigator;
    Eb = Fb && Fb.platform || "";
    vb = Eb.indexOf("Mac") != -1;
    var Gb = Eb.indexOf("Win") != -1, Hb;
    a: {
        var Ib = "", Jb;
        if (zb && o.opera)
            var Kb = o.opera.version
              , Ib = typeof Kb == "function" ? Kb() : Kb;
        else if (Bb ? Jb = /rv\:([^\);]+)(\)|;)/ : Ab ? Jb = /MSIE\s+([^\);]+)(\)|;)/ : Cb && (Jb = /WebKit\/(\S+)/),
        Jb)
            var Lb = Jb.exec(wb())
              , Ib = Lb ? Lb[1] : "";
        if (Ab) {
            var Mb, Nb = o.document;
            Mb = Nb ? Nb.documentMode : i;
            if (Mb > parseFloat(Ib)) {
                Hb = String(Mb);
                break a
            }
        }
        Hb = Ib
    }
    var Ob = {};
    function Pb(a) {
        return Ob[a] || (Ob[a] = $a(Hb, a) >= 0)
    }
    var Qb = {};
    function Rb() {
        return Qb[9] || (Qb[9] = Ab && document.documentMode && document.documentMode >= 9)
    }
    ;function Sb(a, b) {
        for (var c in a)
            b.call(i, a[c], c, a)
    }
    var Tb = "constructor,hasOwnProperty,isPrototypeOf,propertyIsEnumerable,toLocaleString,toString,valueOf".split(",");
    function Ia(a, b) {
        for (var c, d, e = 1; e < arguments.length; e++) {
            d = arguments[e];
            for (c in d)
                a[c] = d[c];
            for (var g = 0; g < Tb.length; g++)
                c = Tb[g],
                Object.prototype.hasOwnProperty.call(d, c) && (a[c] = d[c])
        }
    }
    ;var Ub;
    !Ab || Rb();
    var Vb = Ab && !Pb("8");
    function Wb() {}
    Wb.prototype.Ie = !1;
    Wb.prototype.Oa = function() {
        if (!this.Ie)
            this.Ie = !0,
            this.ja()
    }
    ;
    Wb.prototype.ja = function() {
        this.Hf && Xb.apply(k, this.Hf)
    }
    ;
    function Xb(a) {
        for (var b = 0, c = arguments.length; b < c; ++b) {
            var d = arguments[b];
            ia(d) ? Xb.apply(k, d) : d && typeof d.Oa == "function" && d.Oa()
        }
    }
    ;function Yb(a, b) {
        this.type = a;
        this.currentTarget = this.target = b
    }
    s(Yb, Wb);
    n = Yb.prototype;
    n.ja = function() {
        delete this.type;
        delete this.target;
        delete this.currentTarget
    }
    ;
    n.Ta = !1;
    n.Dc = !0;
    n.stopPropagation = function() {
        this.Ta = !0
    }
    ;
    n.preventDefault = function() {
        this.Dc = !1
    }
    ;
    function Zb(a) {
        Zb[" "](a);
        return a
    }
    Zb[" "] = fa;
    function $b(a, b) {
        a && this.Qc(a, b)
    }
    s($b, Yb);
    n = $b.prototype;
    n.target = k;
    n.relatedTarget = k;
    n.offsetX = 0;
    n.offsetY = 0;
    n.clientX = 0;
    n.clientY = 0;
    n.screenX = 0;
    n.screenY = 0;
    n.button = 0;
    n.keyCode = 0;
    n.charCode = 0;
    n.ctrlKey = !1;
    n.altKey = !1;
    n.shiftKey = !1;
    n.metaKey = !1;
    n.zg = !1;
    n.Ra = k;
    n.Qc = function(a, b) {
        var c = this.type = a.type;
        Yb.call(this, c);
        this.target = a.target || a.srcElement;
        this.currentTarget = b;
        var d = a.relatedTarget;
        if (d) {
            if (Bb) {
                var e;
                a: {
                    try {
                        Zb(d.nodeName);
                        e = !0;
                        break a
                    } catch (g) {}
                    e = !1
                }
                e || (d = k)
            }
        } else if (c == "mouseover")
            d = a.fromElement;
        else if (c == "mouseout")
            d = a.toElement;
        this.relatedTarget = d;
        this.offsetX = a.offsetX !== i ? a.offsetX : a.layerX;
        this.offsetY = a.offsetY !== i ? a.offsetY : a.layerY;
        this.clientX = a.clientX !== i ? a.clientX : a.pageX;
        this.clientY = a.clientY !== i ? a.clientY : a.pageY;
        this.screenX = a.screenX || 0;
        this.screenY = a.screenY || 0;
        this.button = a.button;
        this.keyCode = a.keyCode || 0;
        this.charCode = a.charCode || (c == "keypress" ? a.keyCode : 0);
        this.ctrlKey = a.ctrlKey;
        this.altKey = a.altKey;
        this.shiftKey = a.shiftKey;
        this.metaKey = a.metaKey;
        this.zg = vb ? a.metaKey : a.ctrlKey;
        this.state = a.state;
        this.Ra = a;
        delete this.Dc;
        delete this.Ta
    }
    ;
    n.stopPropagation = function() {
        $b.kb.stopPropagation.call(this);
        this.Ra.stopPropagation ? this.Ra.stopPropagation() : this.Ra.cancelBubble = !0
    }
    ;
    n.preventDefault = function() {
        $b.kb.preventDefault.call(this);
        var a = this.Ra;
        if (a.preventDefault)
            a.preventDefault();
        else if (a.returnValue = !1,
        Vb)
            try {
                if (a.ctrlKey || a.keyCode >= 112 && a.keyCode <= 123)
                    a.keyCode = -1
            } catch (b) {}
    }
    ;
    n.ja = function() {
        $b.kb.ja.call(this);
        this.relatedTarget = this.currentTarget = this.target = this.Ra = k
    }
    ;
    function ac() {}
    var bc = 0;
    n = ac.prototype;
    n.key = 0;
    n.Yb = !1;
    n.td = !1;
    n.Qc = function(a, b, c, d, e, g) {
        if (la(a))
            this.We = !0;
        else if (a && a.handleEvent && la(a.handleEvent))
            this.We = !1;
        else
            throw Error("Invalid listener argument");
        this.yc = a;
        this.of = b;
        this.src = c;
        this.type = d;
        this.capture = !!e;
        this.Id = g;
        this.td = !1;
        this.key = ++bc;
        this.Yb = !1
    }
    ;
    n.handleEvent = function(a) {
        return this.We ? this.yc.call(this.Id || this.src, a) : this.yc.handleEvent.call(this.yc, a)
    }
    ;
    var dc, ec = (dc = "ScriptEngine"in o && o.ScriptEngine() == "JScript") ? o.ScriptEngineMajorVersion() + "." + o.ScriptEngineMinorVersion() + "." + o.ScriptEngineBuildVersion() : "0";
    function fc(a, b) {
        this.ef = b;
        this.xb = [];
        if (a > this.ef)
            throw Error("[goog.structs.SimplePool] Initial cannot be greater than max");
        for (var c = 0; c < a; c++)
            this.xb.push(this.Na ? this.Na() : {})
    }
    s(fc, Wb);
    fc.prototype.Na = k;
    fc.prototype.He = k;
    fc.prototype.getObject = function() {
        return this.xb.length ? this.xb.pop() : this.Na ? this.Na() : {}
    }
    ;
    function gc(a, b) {
        a.xb.length < a.ef ? a.xb.push(b) : hc(a, b)
    }
    function hc(a, b) {
        if (a.He)
            a.He(b);
        else if (ma(b))
            if (la(b.Oa))
                b.Oa();
            else
                for (var c in b)
                    delete b[c]
    }
    fc.prototype.ja = function() {
        fc.kb.ja.call(this);
        for (var a = this.xb; a.length; )
            hc(this, a.pop());
        delete this.xb
    }
    ;
    var ic, jc, kc, lc, mc, nc, oc, pc, qc, rc, sc;
    (function() {
        function a() {
            return {
                Ga: 0,
                xa: 0
            }
        }
        function b() {
            return []
        }
        function c() {
            function a(b) {
                b = h.call(a.src, a.key, b);
                if (!b)
                    return b
            }
            return a
        }
        function d() {
            return new ac
        }
        function e() {
            return new $b
        }
        var g = dc && !($a(ec, "5.7") >= 0), h;
        nc = function(a) {
            h = a
        }
        ;
        if (g) {
            ic = function() {
                return m.getObject()
            }
            ;
            jc = function(a) {
                gc(m, a)
            }
            ;
            kc = function() {
                return l.getObject()
            }
            ;
            lc = function(a) {
                gc(l, a)
            }
            ;
            mc = function() {
                return q.getObject()
            }
            ;
            oc = function() {
                gc(q, c())
            }
            ;
            pc = function() {
                return A.getObject()
            }
            ;
            qc = function(a) {
                gc(A, a)
            }
            ;
            rc = function() {
                return r.getObject()
            }
            ;
            sc = function(a) {
                gc(r, a)
            }
            ;
            var m = new fc(0,600);
            m.Na = a;
            var l = new fc(0,600);
            l.Na = b;
            var q = new fc(0,600);
            q.Na = c;
            var A = new fc(0,600);
            A.Na = d;
            var r = new fc(0,600);
            r.Na = e
        } else
            ic = a,
            jc = fa,
            kc = b,
            lc = fa,
            mc = c,
            oc = fa,
            pc = d,
            qc = fa,
            rc = e,
            sc = fa
    }
    )();
    var tc = {}
      , uc = {}
      , vc = {}
      , wc = {};
    function w(a, b, c, d, e) {
        if (b)
            if (ha(b)) {
                for (var g = 0; g < b.length; g++)
                    w(a, b[g], c, d, e);
                return k
            } else {
                var d = !!d
                  , h = uc;
                b in h || (h[b] = ic());
                h = h[b];
                d in h || (h[d] = ic(),
                h.Ga++);
                var h = h[d], m = na(a), l;
                h.xa++;
                if (h[m]) {
                    l = h[m];
                    for (g = 0; g < l.length; g++)
                        if (h = l[g],
                        h.yc == c && h.Id == e) {
                            if (h.Yb)
                                break;
                            return l[g].key
                        }
                } else
                    l = h[m] = kc(),
                    h.Ga++;
                g = mc();
                g.src = a;
                h = pc();
                h.Qc(c, g, a, b, d, e);
                c = h.key;
                g.key = c;
                l.push(h);
                tc[c] = h;
                vc[m] || (vc[m] = kc());
                vc[m].push(h);
                a.addEventListener ? (a == o || !a.ud) && a.addEventListener(b, g, d) : a.attachEvent(b in wc ? wc[b] : wc[b] = "on" + b, g);
                return c
            }
        else
            throw Error("Invalid event type");
    }
    function xc(a, b, c, d, e) {
        if (ha(b))
            for (var g = 0; g < b.length; g++)
                xc(a, b[g], c, d, e);
        else
            a = w(a, b, c, d, e),
            tc[a].td = !0
    }
    function yc(a, b, c, d, e) {
        if (ha(b))
            for (var g = 0; g < b.length; g++)
                yc(a, b[g], c, d, e);
        else {
            d = !!d;
            a: {
                g = uc;
                if (b in g && (g = g[b],
                d in g && (g = g[d],
                a = na(a),
                g[a]))) {
                    a = g[a];
                    break a
                }
                a = k
            }
            if (a)
                for (g = 0; g < a.length; g++)
                    if (a[g].yc == c && a[g].capture == d && a[g].Id == e) {
                        zc(a[g].key);
                        break
                    }
        }
    }
    function zc(a) {
        if (tc[a]) {
            var b = tc[a];
            if (!b.Yb) {
                var c = b.src
                  , d = b.type
                  , e = b.of
                  , g = b.capture;
                c.removeEventListener ? (c == o || !c.ud) && c.removeEventListener(d, e, g) : c.detachEvent && c.detachEvent(d in wc ? wc[d] : wc[d] = "on" + d, e);
                c = na(c);
                e = uc[d][g][c];
                if (vc[c]) {
                    var h = vc[c];
                    jb(h, b);
                    h.length == 0 && delete vc[c]
                }
                b.Yb = !0;
                e.hf = !0;
                Ac(d, g, c, e);
                delete tc[a]
            }
        }
    }
    function Ac(a, b, c, d) {
        if (!d.Vc && d.hf) {
            for (var e = 0, g = 0; e < d.length; e++)
                if (d[e].Yb) {
                    var h = d[e].of;
                    h.src = k;
                    oc(h);
                    qc(d[e])
                } else
                    e != g && (d[g] = d[e]),
                    g++;
            d.length = g;
            d.hf = !1;
            g == 0 && (lc(d),
            delete uc[a][b][c],
            uc[a][b].Ga--,
            uc[a][b].Ga == 0 && (jc(uc[a][b]),
            delete uc[a][b],
            uc[a].Ga--),
            uc[a].Ga == 0 && (jc(uc[a]),
            delete uc[a]))
        }
    }
    function Bc(a) {
        var b, c = 0, d = b == k;
        b = !!b;
        if (a == k)
            Sb(vc, function(a) {
                for (var e = a.length - 1; e >= 0; e--) {
                    var g = a[e];
                    if (d || b == g.capture)
                        zc(g.key),
                        c++
                }
            });
        else if (a = na(a),
        vc[a])
            for (var a = vc[a], e = a.length - 1; e >= 0; e--) {
                var g = a[e];
                if (d || b == g.capture)
                    zc(g.key),
                    c++
            }
    }
    function Cc(a, b, c, d, e) {
        var g = 1
          , b = na(b);
        if (a[b]) {
            a.xa--;
            a = a[b];
            a.Vc ? a.Vc++ : a.Vc = 1;
            try {
                for (var h = a.length, m = 0; m < h; m++) {
                    var l = a[m];
                    l && !l.Yb && (g &= Dc(l, e) !== !1)
                }
            } finally {
                a.Vc--,
                Ac(c, d, b, a)
            }
        }
        return Boolean(g)
    }
    function Dc(a, b) {
        var c = a.handleEvent(b);
        a.td && zc(a.key);
        return c
    }
    nc(function(a, b) {
        if (!tc[a])
            return !0;
        var c = tc[a]
          , d = c.type
          , e = uc;
        if (!(d in e))
            return !0;
        var e = e[d], g, h;
        Ub === i && (Ub = Ab && !o.addEventListener);
        if (Ub) {
            g = b || ea("window.event");
            var m = !0 in e
              , l = !1 in e;
            if (m) {
                if (g.keyCode < 0 || g.returnValue != i)
                    return !0;
                a: {
                    var q = !1;
                    if (g.keyCode == 0)
                        try {
                            g.keyCode = -1;
                            break a
                        } catch (A) {
                            q = !0
                        }
                    if (q || g.returnValue == i)
                        g.returnValue = !0
                }
            }
            q = rc();
            q.Qc(g, this);
            g = !0;
            try {
                if (m) {
                    for (var r = kc(), X = q.currentTarget; X; X = X.parentNode)
                        r.push(X);
                    h = e[!0];
                    h.xa = h.Ga;
                    for (var ca = r.length - 1; !q.Ta && ca >= 0 && h.xa; ca--)
                        q.currentTarget = r[ca],
                        g &= Cc(h, r[ca], d, !0, q);
                    if (l) {
                        h = e[!1];
                        h.xa = h.Ga;
                        for (ca = 0; !q.Ta && ca < r.length && h.xa; ca++)
                            q.currentTarget = r[ca],
                            g &= Cc(h, r[ca], d, !1, q)
                    }
                } else
                    g = Dc(c, q)
            } finally {
                if (r)
                    r.length = 0,
                    lc(r);
                q.Oa();
                sc(q)
            }
            return g
        }
        d = new $b(b,this);
        try {
            g = Dc(c, d)
        } finally {
            d.Oa()
        }
        return g
    });
    function Ec() {}
    s(Ec, Wb);
    n = Ec.prototype;
    n.ud = !0;
    n.$d = k;
    n.addEventListener = function(a, b, c, d) {
        w(this, a, b, c, d)
    }
    ;
    n.removeEventListener = function(a, b, c, d) {
        yc(this, a, b, c, d)
    }
    ;
    n.dispatchEvent = function(a) {
        var b = a.type || a
          , c = uc;
        if (b in c) {
            if (ja(a))
                a = new Yb(a,this);
            else if (a instanceof Yb)
                a.target = a.target || this;
            else {
                var d = a
                  , a = new Yb(b,this);
                Ia(a, d)
            }
            var d = 1, e, c = c[b], b = !0 in c, g;
            if (b) {
                e = [];
                for (g = this; g; g = g.$d)
                    e.push(g);
                g = c[!0];
                g.xa = g.Ga;
                for (var h = e.length - 1; !a.Ta && h >= 0 && g.xa; h--)
                    a.currentTarget = e[h],
                    d &= Cc(g, e[h], a.type, !0, a) && a.Dc != !1
            }
            if (!1 in c)
                if (g = c[!1],
                g.xa = g.Ga,
                b)
                    for (h = 0; !a.Ta && h < e.length && g.xa; h++)
                        a.currentTarget = e[h],
                        d &= Cc(g, e[h], a.type, !1, a) && a.Dc != !1;
                else
                    for (e = this; !a.Ta && e && g.xa; e = e.$d)
                        a.currentTarget = e,
                        d &= Cc(g, e, a.type, !1, a) && a.Dc != !1;
            a = Boolean(d)
        } else
            a = !0;
        return a
    }
    ;
    n.ja = function() {
        Ec.kb.ja.call(this);
        Bc(this);
        this.$d = k
    }
    ;
    var Fc, Gc, Hc, Ic, Jc, Kc = wb();
    Gc = (Fc = Cb && Db && /(ipod|iphone|ipad)/i.test(Kc)) && la(Object.freeze);
    Hc = Cb && Db && /(android)/i.test(Kc);
    Ic = Cb && /playbook/i.test(Kc);
    Jc = p(document.ontouchmove) && Db;
    function Lc(a, b, c, d) {
        this.left = a;
        this.top = b;
        this.width = c;
        this.height = d
    }
    Lc.prototype.r = function() {
        return new Lc(this.left,this.top,this.width,this.height)
    }
    ;
    function Mc(a) {
        return new Lc(a.left,a.top,a.right - a.left,a.bottom - a.top)
    }
    function Nc(a, b) {
        var c = Math.max(a.left, b.left)
          , d = Math.min(a.left + a.width, b.left + b.width);
        if (c <= d) {
            var e = Math.max(a.top, b.top)
              , g = Math.min(a.top + a.height, b.top + b.height);
            if (e <= g)
                return new Lc(c,e,d - c,g - e)
        }
        return k
    }
    Lc.prototype.contains = function(a) {
        return a instanceof Lc ? this.left <= a.left && this.left + this.width >= a.left + a.width && this.top <= a.top && this.top + this.height >= a.top + a.height : a.x >= this.left && a.x <= this.left + this.width && a.y >= this.top && a.y <= this.top + this.height
    }
    ;
    Lc.prototype.t = function() {
        return new Da(this.width,this.height)
    }
    ;
    var Oc;
    function Pc(a) {
        return (a = a.className) && typeof a.split == "function" ? a.split(/\s+/) : []
    }
    function Qc(a, b) {
        var c = Pc(a), d = ob(arguments, 1), e;
        e = c;
        for (var g = 0, h = 0; h < d.length; h++)
            eb(e, d[h]) >= 0 || (e.push(d[h]),
            g++);
        e = g == d.length;
        a.className = c.join(" ");
        return e
    }
    function Rc(a, b) {
        for (var c = Pc(a), d = ob(arguments, 1), e = c, g = 0, h = 0; h < e.length; h++)
            eb(d, e[h]) >= 0 && (nb(e, h--, 1),
            g++);
        a.className = c.join(" ")
    }
    ;var Sc = !Ab || Rb();
    !Bb && !Ab || Ab && Rb() || Bb && Pb("1.9.1");
    Ab && Pb("9");
    function Tc(a) {
        return a ? new Uc(Vc(a)) : Oc || (Oc = new Uc)
    }
    function Wc(a, b) {
        var c = b && b != "*" ? b.toUpperCase() : "";
        return a.querySelectorAll && a.querySelector && (!Cb || Xc(document) || Pb("528")) && c ? a.querySelectorAll(c + "") : a.getElementsByTagName(c || "*")
    }
    function Yc(a, b) {
        Sb(b, function(b, d) {
            d == "style" ? a.style.cssText = b : d == "class" ? a.className = b : d == "for" ? a.htmlFor = b : d in Zc ? a.setAttribute(Zc[d], b) : d.lastIndexOf("aria-", 0) == 0 ? a.setAttribute(d, b) : a[d] = b
        })
    }
    var Zc = {
        cellpadding: "cellPadding",
        cellspacing: "cellSpacing",
        colspan: "colSpan",
        rowspan: "rowSpan",
        valign: "vAlign",
        height: "height",
        width: "width",
        usemap: "useMap",
        frameborder: "frameBorder",
        maxlength: "maxLength",
        type: "type"
    };
    function $c(a) {
        var b = a.document;
        if (Cb && !Pb("500") && !Db) {
            typeof a.innerHeight == "undefined" && (a = window);
            var b = a.innerHeight
              , c = a.document.documentElement.scrollHeight;
            a == a.top && c < b && (b -= 15);
            return new Da(a.innerWidth,b)
        }
        a = Xc(b) ? b.documentElement : b.body;
        return new Da(a.clientWidth,a.clientHeight)
    }
    function ad(a, b, c) {
        return bd(document, arguments)
    }
    function bd(a, b) {
        var c = b[0]
          , d = b[1];
        if (!Sc && d && (d.name || d.type)) {
            c = ["<", c];
            d.name && c.push(' name="', Ua(d.name), '"');
            if (d.type) {
                c.push(' type="', Ua(d.type), '"');
                var e = {};
                Ia(e, d);
                d = e;
                delete d.type
            }
            c.push(">");
            c = c.join("")
        }
        c = a.createElement(c);
        if (d)
            ja(d) ? c.className = d : ha(d) ? Qc.apply(k, [c].concat(d)) : Yc(c, d);
        b.length > 2 && cd(a, c, b, 2);
        return c
    }
    function cd(a, b, c, d) {
        function e(c) {
            c && b.appendChild(ja(c) ? a.createTextNode(c) : c)
        }
        for (; d < c.length; d++) {
            var g = c[d];
            ia(g) && !(ma(g) && g.nodeType > 0) ? fb(dd(g) ? lb(g) : g, e) : e(g)
        }
    }
    function ed() {
        return document.createElement("div")
    }
    function Xc(a) {
        return a.compatMode == "CSS1Compat"
    }
    function fd(a, b) {
        b.parentNode && b.parentNode.insertBefore(a, b)
    }
    function gd(a, b) {
        b.parentNode && b.parentNode.insertBefore(a, b.nextSibling)
    }
    function hd(a) {
        a && a.parentNode && a.parentNode.removeChild(a)
    }
    function id(a, b) {
        if (a.contains && b.nodeType == 1)
            return a == b || a.contains(b);
        if (typeof a.compareDocumentPosition != "undefined")
            return a == b || Boolean(a.compareDocumentPosition(b) & 16);
        for (; b && a != b; )
            b = b.parentNode;
        return b == a
    }
    function Vc(a) {
        return a.nodeType == 9 ? a : a.ownerDocument || a.document
    }
    function jd(a, b) {
        if ("textContent"in a)
            a.textContent = b;
        else if (a.firstChild && a.firstChild.nodeType == 3) {
            for (; a.lastChild != a.firstChild; )
                a.removeChild(a.lastChild);
            a.firstChild.data = b
        } else {
            for (var c; c = a.firstChild; )
                a.removeChild(c);
            a.appendChild(Vc(a).createTextNode(b))
        }
    }
    function dd(a) {
        if (a && typeof a.length == "number")
            if (ma(a))
                return typeof a.item == "function" || typeof a.item == "string";
            else if (la(a))
                return typeof a.item == "function";
        return !1
    }
    function Uc(a) {
        this.Za = a || o.document || document
    }
    n = Uc.prototype;
    n.Ee = function(a, b, c) {
        return bd(this.Za, arguments)
    }
    ;
    n.createElement = function(a) {
        return this.Za.createElement(a)
    }
    ;
    n.createTextNode = function(a) {
        return this.Za.createTextNode(a)
    }
    ;
    n.appendChild = function(a, b) {
        a.appendChild(b)
    }
    ;
    n.append = function(a, b) {
        cd(Vc(a), a, arguments, 1)
    }
    ;
    n.contains = id;
    function kd(a, b, c) {
        a.style[cb(c)] = b
    }
    function ld(a, b) {
        var c;
        a: {
            c = Vc(a);
            if (c.defaultView && c.defaultView.getComputedStyle && (c = c.defaultView.getComputedStyle(a, k))) {
                c = c[b] || c.getPropertyValue(b);
                break a
            }
            c = ""
        }
        return c || (a.currentStyle ? a.currentStyle[b] : k) || a.style[b]
    }
    function md(a) {
        var b = a.getBoundingClientRect();
        if (Ab)
            a = a.ownerDocument,
            b.left -= a.documentElement.clientLeft + a.body.clientLeft,
            b.top -= a.documentElement.clientTop + a.body.clientTop;
        return b
    }
    function nd(a) {
        if (Ab)
            return a.offsetParent;
        for (var b = Vc(a), c = ld(a, "position"), d = c == "fixed" || c == "absolute", a = a.parentNode; a && a != b; a = a.parentNode)
            if (c = ld(a, "position"),
            d = d && c == "static" && a != b.documentElement && a != b.body,
            !d && (a.scrollWidth > a.clientWidth || a.scrollHeight > a.clientHeight || c == "fixed" || c == "absolute" || c == "relative"))
                return a;
        return k
    }
    function od(a, b, c) {
        if (b instanceof Da)
            c = b.height,
            b = b.width;
        else if (c == i)
            throw Error("missing height argument");
        a.style.width = pd(b);
        a.style.height = pd(c)
    }
    function pd(a) {
        typeof a == "number" && (a = Math.round(a) + "px");
        return a
    }
    function qd(a) {
        if (ld(a, "display") != "none")
            return rd(a);
        var b = a.style
          , c = b.display
          , d = b.visibility
          , e = b.position;
        b.visibility = "hidden";
        b.position = "absolute";
        b.display = "inline";
        a = rd(a);
        b.display = c;
        b.position = e;
        b.visibility = d;
        return a
    }
    function rd(a) {
        var b = a.offsetWidth
          , c = a.offsetHeight
          , d = Cb && !b && !c;
        return (!p(b) || d) && a.getBoundingClientRect ? (a = md(a),
        new Da(a.right - a.left,a.bottom - a.top)) : new Da(b,c)
    }
    function sd(a) {
        var b = Tc(i)
          , c = k;
        if (Ab)
            c = b.Za.createStyleSheet(),
            td(c, a);
        else {
            var d = Wc(b.Za, "head")[0];
            d || (c = Wc(b.Za, "body")[0],
            d = b.Ee("head"),
            c.parentNode.insertBefore(d, c));
            c = b.Ee("style");
            td(c, a);
            b.appendChild(d, c)
        }
        return c
    }
    function td(a, b) {
        Ab ? a.cssText = b : a[Cb ? "innerText" : "innerHTML"] = b
    }
    ;var ud, vd, wd, xd, yd, zd, Ad;
    (function() {
        var a = Cb ? "Webkit" : Bb ? "Moz" : zb ? "O" : Ab ? "ms" : ""
          , b = ad("div").style;
        ud = "-" + a.toLowerCase() + "-transform";
        vd = function(a) {
            return b[a] !== i ? a : !1
        }
        ;
        wd = function(b) {
            var d = b.charAt(0).toLowerCase() + b.substr(1)
              , e = a + b;
            return vd(b) ? b : vd(d) ? d : vd(e) ? e : i
        }
    }
    )();
    var Bd = function() {
        var a = wd("BorderRadius");
        return function(b, c, d, e) {
            e = e ? "%" : "px";
            d = p(d) ? d : c;
            c = (ha(c) ? c.join(e + " ") : c) + e + "/" + ((ha(d) ? d.join(e + " ") : d) + e);
            if (c != b.Af)
                b.style[a] = b.Af = c
        }
    }();
    function Ra(a) {
        this.jd = [];
        this.Vb = 1;
        this.Mc = !0;
        this.nh && Qa(this, a)
    }
    function Cd(a, b) {
        a.Mc = b;
        return a
    }
    Ra.prototype.scale = function(a, b) {
        this.jd.push("scale(" + a + "," + b + ")");
        return this
    }
    ;
    Ra.prototype.rotate = function(a, b) {
        var c;
        c = this.Mc && (Fc || Ic) ? "rotate3d(0, 0, 1, " + a + (b ? b : "deg") + ")" : "rotate(" + a + (b ? b : "deg") + ")";
        a != 0 && this.jd.push(c);
        return this
    }
    ;
    Ra.prototype.translate = function(a, b, c) {
        var d = 1 / this.Vb
          , e = "translate";
        if (this.Mc && (Fc || Ic))
            e += "3d";
        e += "(" + a * d + "px," + b * d + "px";
        if (this.Mc && (Fc || Ic))
            e += "," + (c ? c : 0) * d + "px";
        this.jd.push(e + ")");
        return this
    }
    ;
    function Qa(a, b) {
        if (a.Vb != 1) {
            var c = 1 / a.Vb;
            a.scale(c, c);
            a.Vb = 1
        }
        if (b != 1)
            a.scale(b, b),
            a.Vb = b;
        return a
    }
    Ra.prototype.toString = function() {
        this.Vb != 1 && Qa(this, 1);
        return this.jd.join(" ")
    }
    ;
    var Pa = function() {
        var a = wd("Transform");
        return function(b, c) {
            var d = c.toString();
            if (d != b.Tg)
                b.style[a] = b.Tg = d;
            ya = 1
        }
    }()
      , Ma = function() {
        var a = wd("TransformOrigin");
        return function(b, c, d, e) {
            e = e ? "%" : "px";
            c = c + e + " " + d + e;
            if (c != b.Ug)
                b.style[a] = b.Ug = c
        }
    }();
    (function() {
        function a(a, b) {
            if (!a.length)
                return a;
            for (var e = a.split("),"), g = 0; g < e.length - 1; g++)
                e[g] += ")";
            e = gb(e, function(a) {
                return a.indexOf(b) == -1
            });
            return e.join(",")
        }
        var b = wd("Transition");
        xd = !!b && !zb;
        yd = function(c, d, e, g) {
            if (b) {
                var h = a(c.style[b], d);
                h.length && (h += ", ");
                h += d + " " + e + "s cubic-bezier(" + g[1] + "," + g[2] + "," + g[3] + "," + g[4] + ")";
                c.style[b] = h
            }
        }
        ;
        zd = function(c, d) {
            b && c && (c.style[b] = a(c.style[b], d))
        }
        ;
        Ad = function(a, b, e) {
            if (a.Zg != b || a.Yf != e)
                a.Zg = b,
                a.Yf = e,
                od(a, b, e)
        }
    }
    )();
    var v = new Fa;
    v.Gb = function() {
        for (var a = 0, b, c = 0; b = this.s[c]; c++)
            b = b instanceof Dd ? b.da : b,
            b == this.k.childNodes[a] ? a++ : (id(this.pa, b) && hd(b),
            v.yf(this.pa, b, a++))
    }
    ;
    v.Kf = function() {
        var a = this.t()
          , b = this.Wb
          , c = this.f
          , d = this.Ia || 1
          , e = this.re;
        this.L[La] && (c = this.L[La]);
        var g = Math.round(a.width * d)
          , h = Math.round(a.height * d)
          , m = this.T.r();
        this.L[Ka] && (m = this.L[Ka].r());
        g != 0 ? m.scale(a.width / (g * b / d)) : m.scale(1 / b);
        Ad(this.k, g, h);
        Ma(this.k, this.Jb.x * 100, this.Jb.y * 100, !0);
        g = this.Jb.x * a.width * d;
        h = this.Jb.y * a.height * d;
        a = c.x * d / b - g;
        b = c.y * d / b - h;
        c = this.ea ? this.ea.Wa : 0;
        (g - c != 0 || h - c != 0) && this.k == this.pa && this.s.length && v.kg.call(this);
        this.k != this.pa && !this.ua[La] && !this.ua[Ka] && !this.ua[Na] && Pa(this.pa, Cd(new Ra, e).translate(g - c, h - c));
        this.A != this.La && (this.La && v.sf.call(this),
        this.A && v.oe.call(this));
        e = Cd(Qa(new Ra, 0.1), e);
        this.A && (v.we.call(this.A),
        Qa(Qa(e, 0.1).translate(-this.A.ig - g, -this.A.jg - h).rotate(this.A.bf, "rad").translate(g, h), 1));
        g = -Oa(this);
        p(this.L[Na]) && (g = -this.L[Na]);
        e.translate(a, b).scale(m.x, m.y).rotate(g);
        !this.ua[La] && !this.ua[Ka] && !this.ua[Na] && Pa(this.k, e)
    }
    ;
    v.update = function() {
        if (this.k) {
            v.Kf.call(this);
            if (!this.ua[Ed]) {
                var a = this.ca;
                p(this.L[Ed]) && (a = this.L[Ed]);
                if (this.aa & Fd) {
                    var b = this.k.style;
                    if ("opacity"in b)
                        b.opacity = a;
                    else if ("MozOpacity"in b)
                        b.MozOpacity = a;
                    else if ("filter"in b)
                        b.filter = a === "" ? "" : "alpha(opacity=" + a * 100 + ")"
                }
            }
            this.aa & Gd && (this.k.style.display = this.Pc ? "none" : "block");
            this.ib || this.N.R.call(this, this.k)
        }
    }
    ;
    v.we = function() {
        if (p(this.fd) && this.fd.Y) {
            var a = this.fd
              , b = this.m()
              , c = new t(b.left,b.top)
              , d = new t(b.right,b.top)
              , e = new t(b.right,b.bottom)
              , b = a.getParent()
              , c = Hd(this, c, b)
              , d = Hd(this, d, b)
              , e = Hd(this, e, b)
              , b = Math.atan2(c.y - d.y, d.x - c.x)
              , g = d.x - c.x
              , h = c.y - d.y
              , m = e.x - d.x
              , l = e.y - d.y
              , d = Math.cos(b)
              , e = Math.sin(b);
            this.Rd = Math.round(Math.sqrt(g * g + h * h));
            this.Qd = Math.round(Math.sqrt(m * m + l * l));
            if (Ga(a.N) == v)
                g = a.da,
                od(g, this.Rd, this.Qd),
                Pa(g, Cd(Qa(new Ra, 0.1), this.re).translate(c.x, c.y).rotate(-b, "rad"));
            Ga(this.N) == v && (this.k.style.display = "none");
            this.af = Id(a, c.r());
            this.hg = !0;
            this.ig = d * c.x - e * c.y;
            this.jg = d * c.y + e * c.x;
            this.bf = b
        }
    }
    ;
    v.yf = function(a, b, c) {
        c == i || a.childNodes.length <= c ? a.appendChild(b) : a.insertBefore(b, a.childNodes[c])
    }
    ;
    v.kg = function() {
        this.pa = ad("div");
        for (var a = document.createDocumentFragment(), b; b = this.k.firstChild; )
            this.k.removeChild(b),
            a.appendChild(b);
        this.pa.appendChild(a);
        this.k.appendChild(this.pa)
    }
    ;
    v.sf = function() {
        if (this.k != this.da) {
            if (Ga(this.N) == v) {
                hd(this.k);
                var a = this.da
                  , b = a.parentNode;
                b && b.replaceChild(this.k, a);
                this.da = this.k
            }
            this.La.Ld = 0;
            this.La = k
        }
    }
    ;
    v.oe = function() {
        if (Ga(this.N) == v) {
            this.da = ad("div");
            this.da.style.cssText = "position:absolute;overflow:hidden;";
            Ma(this.da, 0, 0);
            var a = this.k
              , b = a.parentNode;
            b && b.replaceChild(this.da, a);
            this.da.appendChild(this.k)
        }
        this.A.Ld = 1;
        this.A.fd = this;
        this.La = this.A;
        z(this.A, Jd)
    }
    ;
    function Kd(a, b) {
        this.Ea = dc ? [] : "";
        a != k && this.append.apply(this, arguments)
    }
    dc ? (Kd.prototype.sd = 0,
    Kd.prototype.append = function(a, b, c) {
        b == k ? this.Ea[this.sd++] = a : (this.Ea.push.apply(this.Ea, arguments),
        this.sd = this.Ea.length);
        return this
    }
    ) : Kd.prototype.append = function(a, b, c) {
        this.Ea += a;
        if (b != k)
            for (var d = 1; d < arguments.length; d++)
                this.Ea += arguments[d];
        return this
    }
    ;
    Kd.prototype.clear = function() {
        dc ? this.sd = this.Ea.length = 0 : this.Ea = ""
    }
    ;
    Kd.prototype.toString = function() {
        if (dc) {
            var a = this.Ea.join("");
            this.clear();
            a && this.append(a);
            return a
        } else
            return this.Ea
    }
    ;
    Ab && Pb(8);
    (function() {
        var a = [[], []]
          , b = [[], []];
        za = function(c, d, e) {
            ib((e ? b : a)[d || 0], c)
        }
        ;
        Aa = function() {
            for (var c, d = 0; d < 2; d++) {
                for (; a[d].length; )
                    c = a[d][0],
                    c.update(d),
                    c.aa = 0,
                    c == a[d][0] && a[d].shift();
                a[d] = []
            }
            b = [[], []]
        }
    }
    )();
    var Jd = 1, Fd = 16, Gd = 32, La = 1, Ka = 2, Na = 4, Ed = 5, Ld;
    var Md = new Kd;
    Md.append(".", "lime-director", " {position:absolute; -webkit-transform-origin: 0 0; -moz-transform-origin: 0 0; -o-transform-origin: 0 0; image-rendering:  optimizeSpeed; overflow: hidden;}.", "lime-director", " div, .", "lime-director", " img, .", "lime-director", " canvas {-webkit-transform-origin: 0 0; -moz-transform-origin: 0 0; -o-transform-origin: 0 0; position: absolute; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; -moz-user-select: none; -webkit-user-select: none; -webkit-user-drag: none;}.", "lime-scene", " {position:absolute; width:100%; height:100%; left: 0px; top: 0px; overflow: hidden; -moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box;}.", "lime-fps", " {float: left; background: #333; color: #fff; position: absolute; top:0px; left: 0px; padding:2px 4px;}div.", "lime-layer", " {position: absolute; left: 0px; top: 0px; width:0px; height:0px; border: none !important;}.", "lime-cover", " {position: absolute; left: 0px; top: 0px;}.", "lime-button", " {cursor: pointer;}");
    Ld = Md.toString();
    sd(Ld);
    function Dd() {
        this.s = [];
        this.v = k;
        this.Ba = {};
        this.L = {};
        this.ua = {};
        this.he = {};
        this.re = !0;
        this.Y = !1;
        this.de = this.yd = k;
        this.ha = {};
        this.l(1);
        this.a(0, 0);
        this.b(0, 0);
        this.Wb = 1;
        this.d(0.5, 0.5);
        Nd(this, 0);
        this.od = 0;
        z(this, 7);
        this.ca = 1;
        Od(this, k);
        Pd(this, Ga(this.Va[0]));
        z(this, 64)
    }
    s(Dd, Ec);
    n = Dd.prototype;
    n.Va = [v, u];
    function Pd(a, b) {
        if (!a.N || Ga(a.N) != b) {
            for (var c = -1, d = 0; d < a.Va.length; d++)
                if (Ga(a.Va[d]) == b) {
                    c = d;
                    break
                }
            if (c != -1) {
                a.N = a.Va[d];
                z(a, 64);
                for (d = 0; c = a.s[d]; d++)
                    Pd(c, b)
            }
        }
    }
    n.Ac = function() {
        return !(this.v && Ga(this.v.N) == u)
    }
    ;
    function Qd(a) {
        if (a.Ac())
            return a.Ac() ? Rd(a) : Sd(a),
            a;
        else if (a.v)
            return Qd(a.v);
        return k
    }
    function Td(a) {
        if (!a.v || a instanceof Ja)
            return [];
        var b = a.v.s.indexOf(a)
          , a = Td(a.v);
        a.push(b);
        return a
    }
    function Ud(a, b) {
        if (a == b)
            return 0;
        for (var c = Td(a), d = Td(b), e = 0; ; ) {
            if (c.length <= e)
                return 1;
            if (d.length <= e)
                return -1;
            if (c[e] == d[e])
                e++;
            else
                return c[e] > d[e] ? -1 : 1
        }
    }
    n.ud = !1;
    function z(a, b, c, d) {
        b && !a.aa && za(a, c, d);
        a.aa |= b;
        if (b == 64)
            for (c = 0; d = a.s[c]; c++)
                d instanceof Dd && z(d, 64);
        if (!p(a.aa) || !b)
            a.aa = 0;
        if (b && a.ib)
            a.hg = !1,
            z(a.ib, -1);
        return a
    }
    n.l = function(a, b) {
        this.T = arguments.length == 1 && ka(a) ? new pb(a,a) : arguments.length == 2 ? new pb(arguments[0],arguments[1]) : a;
        return this.L[Ka] ? this : z(this, 2)
    }
    ;
    n.a = function(a, b) {
        this.f = arguments.length == 2 ? new t(arguments[0],arguments[1]) : a;
        return this.L[La] ? this : z(this, Jd)
    }
    ;
    function Od(a, b) {
        if (b != a.A) {
            if (a.A) {
                var c = a.A;
                delete c.xd;
                Vd(c, c.getParent());
                delete a.A.ib
            }
            a.A = b;
            if (a.A)
                Wd(a.A),
                a.A.ib = a;
            z(a, 4)
        }
    }
    n.yb = aa("Jb");
    n.d = function(a, b) {
        this.Jb = arguments.length == 2 ? new pb(arguments[0],arguments[1]) : a;
        return z(this, Jd)
    }
    ;
    function Oa(a) {
        return a.Cb %= 360
    }
    function Nd(a, b) {
        a.Cb = b;
        return a.L[Na] ? a : z(a, Jd)
    }
    function B(a, b) {
        a.Pc = b;
        z(a, Gd);
        a.te = 0;
        return a
    }
    n.t = aa("U");
    n.b = function(a, b) {
        var c = this.U, d, e;
        d = arguments.length == 2 ? new Da(arguments[0],arguments[1]) : a;
        var g = this.yb();
        if (c && this.s.length)
            for (var h = 0; h < this.s.length; h++) {
                var m = this.s[h];
                if (m.Rf) {
                    var l = m.od;
                    if (l != 0) {
                        var q = C(m);
                        e = c.width;
                        var A = q.left + g.x * c.width
                          , r = q.right - q.left
                          , X = e - q.right - g.x * c.width;
                        l & 1 && (e -= A);
                        l & 2 && (e -= r);
                        l & 4 && (e -= X);
                        e != c.width && (e = (d.width - e) / (c.width - e),
                        l & 1 && (A *= e),
                        l & 2 && (r *= e));
                        e = c.height;
                        var X = q.top + g.y * c.height
                          , ca = q.bottom - q.top
                          , q = e - q.bottom - g.y * c.height;
                        l & 8 && (e -= X);
                        l & 16 && (e -= ca);
                        l & 32 && (e -= q);
                        e != c.height && (e = (d.height - e) / (c.height - e),
                        l & 8 && (X *= e),
                        l & 16 && (ca *= e));
                        l = m.yb();
                        m.b(r, ca);
                        m.a(A + l.x * r - g.x * d.width, X + l.y * ca - g.y * d.height)
                    }
                }
            }
        this.U = d;
        return z(this, 2)
    }
    ;
    function Xd(a) {
        a.Ia || Yd(a);
        return a.Ia
    }
    function Yd(a) {
        var b = p(a.Ia) ? a.Ia : a.Wb;
        a.v && a.v.Ia && (b = a.Wb * a.v.Ia);
        if (b != a.Ia) {
            a.Ia = b;
            for (var b = 0, c; c = a.s[b]; b++)
                c instanceof Dd && Yd(c);
            z(a, 2)
        }
    }
    n.Rf = aa("od");
    n.Ja = function(a) {
        return !this.Y ? a : Id(this, this.getParent().Ja(a))
    }
    ;
    function Id(a, b) {
        if (!a.getParent())
            return k;
        b.x -= a.f.x;
        b.y -= a.f.y;
        b.x /= a.T.x;
        b.y /= a.T.y;
        if (a.Cb != 0) {
            var c = b.r()
              , d = a.Cb * Math.PI / 180
              , e = Math.cos(d)
              , d = Math.sin(d);
            b.x = e * c.x - d * c.y;
            b.y = e * c.y + d * c.x
        }
        return b
    }
    n.Uc = function(a) {
        return !this.Y ? a : this.getParent().Uc(Sa(this, a))
    }
    ;
    function Sa(a, b) {
        if (!a.getParent())
            return b;
        var c = b.r();
        if (a.Cb != 0) {
            var d = -a.Cb * Math.PI / 180
              , e = Math.cos(d)
              , d = Math.sin(d);
            c.x = e * b.x - d * b.y;
            c.y = e * b.y + d * b.x
        }
        c.x *= a.T.x;
        c.y *= a.T.y;
        c.x += a.f.x;
        c.y += a.f.y;
        return c
    }
    function Hd(a, b, c) {
        return !a.Y ? b : c.Ja(a.Uc(b))
    }
    function D(a, b) {
        a.ca = b;
        var c = a.Pc;
        a.ca == 0 && !c ? (B(a, !0),
        a.te = 1) : a.ca != 0 && c && a.te && B(a, !1);
        if (p(a.L[Ed]))
            return a;
        z(a, Fd);
        return a
    }
    function Rd(a) {
        function b() {
            this.k = this.da = this.pa = ad(c);
            this.qc && Qc(this.k, this.qc);
            this.aa |= -1
        }
        var c = Ga(a.N) == u ? "canvas" : "div";
        if (a.k) {
            if (a.k.tagName.toLowerCase() != c) {
                var d = a.da;
                b.call(a);
                d.parentNode && d.parentNode.replaceChild(a.da, d)
            }
        } else
            b.call(a)
    }
    function Sd(a) {
        a.da && (hd(a.da),
        delete a.k,
        delete a.da,
        delete a.pa)
    }
    n.Gb = function() {
        this.aa &= -65;
        this.Ac() ? Rd(this) : Sd(this);
        if (this.v && this.v.aa & 64)
            this.v.Gb();
        else if (this.Ac()) {
            for (var a = 0, b; b = this.s[a]; a++)
                b instanceof Dd && b.Gb();
            this.N.Gb.call(this)
        }
    }
    ;
    n.update = function(a) {
        var b, c, a = a || 0;
        na(this);
        this.aa & 64 && this.Gb();
        var d = Ga(this.N) == v || a;
        if (d) {
            for (var e in this.he)
                delete this.L[e],
                delete this.ua[e],
                b = parseInt(e, 10) == Ed ? "opacity" : ud,
                zd(this.k, b),
                this.k != this.pa && zd(this.bh, b);
            b = 0;
            for (e in this.Ba)
                c = this.Ba[e],
                c[3] || (c[3] = 1,
                e == La && this.Cg != this.f && (z(this, Jd, 0, !0),
                b = 1),
                e == Ka && this.Hg != this.T && (z(this, 2, 0, !0),
                b = 1),
                e == Ed && this.xg != this.ca && (z(this, Fd, 0, !0),
                b = 1),
                e == Na && this.Gg != this.Cb && (z(this, 128, 0, !0),
                b = 1));
            if (!b)
                for (e in this.Ba) {
                    c = this.Ba[e];
                    b = parseInt(e, 10) == Ed ? "opacity" : ud;
                    if (Ga(this.N) == v || b != "opacity")
                        this.L[e] = c[0],
                        yd(this.k, b, c[1], c[2]),
                        this.k != this.pa && b == ud && yd(this.pa, b, c[1], c[2]);
                    delete this.Ba[e]
                }
            this.Cg = this.f;
            this.Hg = this.T;
            this.xg = this.ca;
            this.Gg = this.Cb;
            this.he = {}
        }
        if (a)
            this.N.Jf.call(this);
        else {
            if (Ga(this.N) == u) {
                c = Qd(this);
                c.bd = 1;
                if (c == this && this.aa == Jd && !this.A)
                    c.bd = 0;
                za(Qd(this), 1)
            }
            this.N.update.call(this)
        }
        if (d)
            for (e in this.L)
                this.L[e] && (this.ua[e] = !0);
        if (this.tb)
            for (e = 0; e < this.tb.length; e++)
                z(this.tb[e], 7);
        z(this, 0, a)
    }
    ;
    n.getParent = function() {
        return this.v ? this.v : k
    }
    ;
    n.appendChild = function(a, b) {
        a instanceof Dd && a.getParent() ? a.getParent().removeChild(a) : a.parentNode && hd(a);
        a.v = this;
        b == i ? this.s.push(a) : nb(this.s, b, 0, a);
        Ga(this.N) != v && Pd(a, Ga(this.N));
        a instanceof Dd && (Yd(a),
        this.Y && Zd(a));
        return z(this, 64)
    }
    ;
    function $d(a) {
        return a.s.length
    }
    function E(a, b) {
        return b >= 0 && $d(a) > b ? a.s[b] : k
    }
    n.removeChild = function(a) {
        return ae(this, this.s.indexOf(a))
    }
    ;
    function ae(a, b) {
        if (b >= 0 && $d(a) > b) {
            var c = E(a, b);
            c.ib && Od(c.ib, k);
            c instanceof Dd ? (a.Y && be(c),
            Sd(c),
            c.v = k) : hd(c);
            a.s.splice(b, 1);
            return z(a, 64)
        }
        return a
    }
    function ce(a) {
        var b = F.q
          , c = $d(F.q)
          , d = b.s.indexOf(a);
        d != -1 && d != c && (b.s.splice(d, 1),
        nb(b.s, c, 0, a),
        b.ba() && de(b.ba().vb, a),
        z(b, 64))
    }
    n.addEventListener = function(a) {
        Jc && a.substring(0, 5) == "mouse" || (p(this.ha[a]) || (this.ha[a] = [0, 0]),
        this.Y && this.ha[a][0] == 0 && (this.ha[a][0] = 1,
        this.ba().vb.cd(this, a)),
        this.ha[a][1]++)
    }
    ;
    n.removeEventListener = function(a) {
        Jc && a.substring(0, 5) == "mouse" || (this.Y && this.ha[a][1] == 1 && (this.ha[a][0] = 0,
        this.ba().vb.Bc(this, a)),
        this.ha[a][1]--,
        this.ha[a][1] || delete this.ha[a])
    }
    ;
    n.ba = function() {
        return !this.Y ? k : this.yd
    }
    ;
    n.Nc = function() {
        return !this.Y ? k : this.de
    }
    ;
    function be(a) {
        var b;
        a.xd || Vd(a, a.getParent());
        for (var c = 0; b = a.s[c]; c++)
            b instanceof Dd && be(b);
        for (var d in a.ha) {
            a.ha[d][0] = 0;
            if (!a.ba())
                debugger ;a.ba().vb.Bc(a, d)
        }
        de(a.ba().vb, a);
        a.Y = !1;
        a.yd = k;
        a.de = k
    }
    function Zd(a) {
        a.Y = !0;
        a.yd = a.v.ba();
        a.de = a.v.Nc();
        for (var b = 0, c; c = a.s[b]; b++)
            c instanceof Dd && Zd(c);
        for (var d in a.ha)
            a.ha[d][0] = 1,
            a.ba().vb.cd(a, d);
        a.xd && Wd(a);
        de(a.ba().vb, a)
    }
    function Wd(a) {
        a.xd = !0;
        a.Y && ee(a, a.getParent())
    }
    function ee(a, b) {
        if (!b.tb)
            b.tb = [];
        ib(b.tb, a);
        !b && !(b.getParent()instanceof Ja) && ee(a, b.getParent())
    }
    function Vd(a, b) {
        b && b.tb && (jb(b.tb, a),
        Vd(a, b.getParent()))
    }
    n.m = function() {
        var a = this.t()
          , b = this.yb();
        return new Ca(-a.height * b.y,a.width * (1 - b.x),a.height * (1 - b.y),-a.width * b.x)
    }
    ;
    function C(a, b) {
        var c = b || a.m()
          , d = new t(c.left,c.top)
          , e = new t(c.right,c.top)
          , g = new t(c.left,c.bottom)
          , c = new t(c.right,c.bottom)
          , d = Sa(a, d)
          , e = Sa(a, e)
          , g = Sa(a, g)
          , c = Sa(a, c);
        return new Ca(Math.floor(Math.min(d.y, e.y, g.y, c.y)),Math.ceil(Math.max(d.x, e.x, g.x, c.x)),Math.ceil(Math.max(d.y, e.y, g.y, c.y)),Math.floor(Math.min(d.x, e.x, g.x, c.x)))
    }
    n.zc = function() {
        var a = this.m();
        a.left == a.right && this.s.length && (a = C(this.s[0], this.s[0].zc()));
        for (var b = 0, c; c = this.s[b]; b++)
            if (c.Ld != 1) {
                var d = a;
                c = C(c, c.zc());
                d.left = Math.min(d.left, c.left);
                d.top = Math.min(d.top, c.top);
                d.right = Math.max(d.right, c.right);
                d.bottom = Math.max(d.bottom, c.bottom)
            }
        return a
    }
    ;
    n.ga = function(a) {
        this.he[a] = 1
    }
    ;
    n.i = function(a) {
        var b = this.Ja(a.Q);
        return this.m().contains(b) ? (a.position = b,
        !0) : !1
    }
    ;
    function G(a, b) {
        b.qb(a);
        b.play()
    }
    ;function H() {
        Dd.call(this);
        this.qc = "lime-layer"
    }
    s(H, Dd);
    H.prototype.i = function(a) {
        for (var b = 0, c; c = this.s[b]; b++)
            if (c.i(a))
                return a.position = this.Ja(a.Q),
                !0;
        return !1
    }
    ;
    function fe(a) {
        return ge(a || arguments.callee.caller, [])
    }
    function ge(a, b) {
        var c = [];
        if (eb(b, a) >= 0)
            c.push("[...circular reference...]");
        else if (a && b.length < 50) {
            c.push(he(a) + "(");
            for (var d = a.arguments, e = 0; e < d.length; e++) {
                e > 0 && c.push(", ");
                var g;
                g = d[e];
                switch (typeof g) {
                case "object":
                    g = g ? "object" : "null";
                    break;
                case "string":
                    break;
                case "number":
                    g = String(g);
                    break;
                case "boolean":
                    g = g ? "true" : "false";
                    break;
                case "function":
                    g = (g = he(g)) ? g : "[fn]";
                    break;
                default:
                    g = typeof g
                }
                g.length > 40 && (g = g.substr(0, 40) + "...");
                c.push(g)
            }
            b.push(a);
            c.push(")\n");
            try {
                c.push(ge(a.caller, b))
            } catch (h) {
                c.push("[exception trying to get caller]\n")
            }
        } else
            a ? c.push("[...long stack...]") : c.push("[end]");
        return c.join("")
    }
    function he(a) {
        if (ie[a])
            return ie[a];
        a = String(a);
        if (!ie[a]) {
            var b = /function ([^\(]+)/.exec(a);
            ie[a] = b ? b[1] : "[Anonymous]"
        }
        return ie[a]
    }
    var ie = {};
    function je(a, b, c, d, e) {
        this.reset(a, b, c, d, e)
    }
    je.prototype.Ig = 0;
    je.prototype.Le = k;
    je.prototype.Ke = k;
    var ke = 0;
    je.prototype.reset = function(a, b, c, d, e) {
        this.Ig = typeof e == "number" ? e : ke++;
        this.xh = d || va();
        this.xc = a;
        this.ug = b;
        this.jh = c;
        delete this.Le;
        delete this.Ke
    }
    ;
    je.prototype.uf = function(a) {
        this.xc = a
    }
    ;
    function le(a) {
        this.vg = a
    }
    le.prototype.v = k;
    le.prototype.xc = k;
    le.prototype.s = k;
    le.prototype.Se = k;
    function me(a, b) {
        this.name = a;
        this.value = b
    }
    me.prototype.toString = aa("name");
    var ne = new me("CONFIG",700);
    le.prototype.getParent = aa("v");
    le.prototype.uf = function(a) {
        this.xc = a
    }
    ;
    function oe(a) {
        return a.xc ? a.xc : a.v ? oe(a.v) : k
    }
    le.prototype.log = function(a, b, c) {
        if (a.value >= oe(this).value) {
            a = this.Sf(a, b, c);
            b = "log:" + a.ug;
            o.console && (o.console.timeStamp ? o.console.timeStamp(b) : o.console.markTimeline && o.console.markTimeline(b));
            o.msWriteProfilerMark && o.msWriteProfilerMark(b);
            for (b = this; b; ) {
                var c = b
                  , d = a;
                if (c.Se)
                    for (var e = 0, g = i; g = c.Se[e]; e++)
                        g(d);
                b = b.getParent()
            }
        }
    }
    ;
    le.prototype.Sf = function(a, b, c) {
        var d = new je(a,String(b),this.vg);
        if (c) {
            d.Le = c;
            var e;
            var g = arguments.callee.caller;
            try {
                var h;
                var m = ea("window.location.href");
                if (ja(c))
                    h = {
                        message: c,
                        name: "Unknown error",
                        lineNumber: "Not available",
                        fileName: m,
                        stack: "Not available"
                    };
                else {
                    var l, q, A = !1;
                    try {
                        l = c.lineNumber || c.ih || "Not available"
                    } catch (r) {
                        l = "Not available",
                        A = !0
                    }
                    try {
                        q = c.fileName || c.filename || c.sourceURL || m
                    } catch (X) {
                        q = "Not available",
                        A = !0
                    }
                    h = A || !c.lineNumber || !c.fileName || !c.stack ? {
                        message: c.message,
                        name: c.name,
                        lineNumber: l,
                        fileName: q,
                        stack: c.stack || "Not available"
                    } : c
                }
                e = "Message: " + Ua(h.message) + '\nUrl: <a href="view-source:' + h.fileName + '" target="_new">' + h.fileName + "</a>\nLine: " + h.lineNumber + "\n\nBrowser stack:\n" + Ua(h.stack + "-> ") + "[end]\n\nJS stack traversal:\n" + Ua(fe(g) + "-> ")
            } catch (ca) {
                e = "Exception trying to expose exception! You win, we lose. " + ca
            }
            d.Ke = e
        }
        return d
    }
    ;
    var pe = {}
      , qe = k;
    function re(a) {
        qe || (qe = new le(""),
        pe[""] = qe,
        qe.uf(ne));
        var b;
        if (!(b = pe[a])) {
            b = new le(a);
            var c = a.lastIndexOf(".")
              , d = a.substr(c + 1)
              , c = re(a.substr(0, c));
            if (!c.s)
                c.s = {};
            c.s[d] = b;
            b.v = c;
            pe[a] = b
        }
        return b
    }
    ;re("goog.net.xhrMonitor");
    function se() {
        var a = String(te);
        if (/^\s*$/.test(a) ? 0 : /^[\],:{}\s\u2028\u2029]*$/.test(a.replace(/\\["\\\/bfnrtu]/g, "@").replace(/"[^"\\\n\r\u2028\u2029\x00-\x08\x10-\x1f\x80-\x9f]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?/g, "]").replace(/(?:^|:|,)(?:[\s\u2028\u2029]*\[)+/g, "")))
            try {
                return eval("(" + a + ")")
            } catch (b) {}
        throw Error("Invalid JSON string: " + a);
    }
    function ue() {
        return eval("(undefined)")
    }
    function ve() {}
    function we(a) {
        var b = [];
        xe(new ve, a, b);
        return b.join("")
    }
    function xe(a, b, c) {
        switch (typeof b) {
        case "string":
            ye(b, c);
            break;
        case "number":
            c.push(isFinite(b) && !isNaN(b) ? b : "null");
            break;
        case "boolean":
            c.push(b);
            break;
        case "undefined":
            c.push("null");
            break;
        case "object":
            if (b == k) {
                c.push("null");
                break
            }
            if (ha(b)) {
                var d = b.length;
                c.push("[");
                for (var e = "", g = 0; g < d; g++)
                    c.push(e),
                    xe(a, b[g], c),
                    e = ",";
                c.push("]");
                break
            }
            c.push("{");
            d = "";
            for (e in b)
                Object.prototype.hasOwnProperty.call(b, e) && (g = b[e],
                typeof g != "function" && (c.push(d),
                ye(e, c),
                c.push(":"),
                xe(a, g, c),
                d = ","));
            c.push("}");
            break;
        case "function":
            break;
        default:
            throw Error("Unknown type: " + typeof b);
        }
    }
    var ze = {
        '"': '\\"',
        "\\": "\\\\",
        "/": "\\/",
        "\u0008": "\\b",
        "\u000c": "\\f",
        "\n": "\\n",
        "\r": "\\r",
        "\t": "\\t",
        "\u000b": "\\u000b"
    }
      , Ae = /\uffff/.test("\uffff") ? /[\\\"\x00-\x1f\x7f-\uffff]/g : /[\\\"\x00-\x1f\x7f-\xff]/g;
    function ye(a, b) {
        b.push('"', a.replace(Ae, function(a) {
            if (a in ze)
                return ze[a];
            var b = a.charCodeAt(0)
              , e = "\\u";
            b < 16 ? e += "000" : b < 256 ? e += "00" : b < 4096 && (e += "0");
            return ze[a] = e + b.toString(16)
        }), '"')
    }
    ;var Be = {}, Ce, De, Ee, Fe, Ge, He, Ie, Je, Ke, Le, Me, Ne, Oe, Pe, Qe, Re, Se, Te, Ue, te, I;
    function Ve(a, b, c, d, e) {
        H.call(this);
        for (var g = 0; g < $d(F.q); g++) {
            var h = E(F.q, g);
            h.type == "puzzlePiece" && yc(h, ["mousedown", "touchstart"], We)
        }
        this.appendChild((new Xe).c(J + "popupLevel.png").b(c + 20, d + 20));
        g = K(L(M(new N, "futuraBold"), "#000"), 44).b(500, 70);
        g.a(0, -155);
        g.g(a);
        this.appendChild(g);
        g = K(L(M(new N, "futuraBold"), "#000"), 20).b(550, 70);
        g.a(0, -95);
        g.g(b);
        this.appendChild(g);
        O.X(chrono, F);
        b = F.hd.Ka;
        g = F.Ic;
        c = Ye(g);
        a = Ze(g, F.K);
        $e(g, c);
        g = K(L(M(new N, "futuraBold"), "#000"), 20).b(215, 35);
        g.a(0, -75);
        g.g(I["time:"] + " " + b);
        this.appendChild(g);
        for (g = 1; g <= 3; g++)
            this.appendChild(g <= a ? (new P).c(J + "star.png").b(35, 35).a(-80 + g * 40, -50) : (new P).c(J + "emptyStar.png").b(35, 35).a(-80 + g * 40, -50));
        var m = window.getRandomPopup();
        m.img != "" ? (a = af(K(L(M(new N, bf()), "#000"), 18).b(425, 35), "center"),
        a.a(0, -15),
        a.g(m["txt_" + Ce]),
        w(a, ["mouseup", "touchend"], function() {
            window.open(m.url)
        }),
        this.appendChild(a),
        a = (new P).c(J + m.img).a(0, 65),
        this.appendChild(a),
        w(a, ["mouseup", "touchend"], function() {
            window.open(m.url)
        })) : this.appendChild((new P).c(J + "sgLogo.png").a(0, 65));
        var l;
        e ? (l = (new cf(I.home,"iconHome.png")).a(0, 175).l(0.6),
        w(l, ["mousedown", "touchstart"], function() {
            l.l(1.1);
            var a = new Q(!0);
            R(a, df)
        })) : F.Xd != "Expert" ? (l = (new ef(I["play next"])).a(0, 185),
        w(l, ["mousedown", "touchstart"], function() {
            l.l(1.1);
            var a = new F(F.Xd,F.next);
            De ? R(a) : R(a, ff)
        })) : (l = (new ef("More games")).a(0, 185),
        w(l, ["mousedown", "touchstart"], function() {
            l.l(1.1);
            var a = new gf(!1,"Expert",0);
            De ? R(a) : R(a, ff)
        }));
        this.appendChild(l);
        this.a(300, -300);
        De ? this.a(300, 300) : (movePopup = (new S(300,300)).e(0.5),
        G(this, movePopup))
    }
    s(Ve, H);
    var O = new function() {
        this.Aa = [];
        this.Ib = !1;
        this.Ve = 0;
        this.Ad = 1E3 / 30;
        this.Ab = 0
    }
    ;
    function hf(a, b) {
        this.V = this.ff = a;
        this.Nd = p(b) ? b : -1;
        this.cb = []
    }
    hf.prototype.bc = function(a) {
        if (this.cb.length)
            if (this.V > a)
                this.V -= a;
            else {
                var b = this.ff + a - this.V;
                this.V = this.ff - (a - this.V);
                if (this.V < 0)
                    this.V = 0;
                for (var c, a = this.cb.length; --a >= 0; )
                    (c = this.cb[a]) && c[0] && la(c[1]) && c[1].call(c[2], b);
                this.Nd != -1 && (this.Nd--,
                this.Nd == 0 && O.X(c[1], c[2]))
            }
    }
    ;
    O.Aa.push(new hf(0));
    O.me = o.mozRequestAnimationFrame || o.webkitRequestAnimationFrame;
    O.fh = aa("Ad");
    O.rh = function(a) {
        this.Ad = a;
        this.Ib && (O.Fe(),
        O.ne())
    }
    ;
    O.dd = function(a, b, c) {
        c = p(c) ? c : this.Aa[0];
        ib(c.cb, [1, a, b]);
        ib(this.Aa, c);
        this.Ib || O.ne()
    }
    ;
    O.X = function(a, b) {
        for (var c = this.Aa.length; --c >= 0; ) {
            for (var d = this.Aa[c], e = d.cb, g, h = e.length; --h >= 0; )
                g = e[h],
                g[1] == a && g[2] == b && jb(e, g);
            e.length == 0 && c != 0 && jb(this.Aa, d)
        }
        this.Aa.length == 1 && this.Aa[0].cb.length == 0 && O.Fe()
    }
    ;
    O.ne = function() {
        if (!this.Ib)
            this.Ab = va(),
            O.me ? o.mozRequestAnimationFrame ? Hb >= 11 ? (this.rb = ta(O.se, this),
            o.mozRequestAnimationFrame(this.rb)) : (o.mozRequestAnimationFrame(),
            this.ve = ta(O.zf, this),
            o.addEventListener("MozBeforePaint", this.ve, !1)) : (this.rb = ta(O.se, this),
            o.webkitRequestAnimationFrame(this.rb)) : this.Ve = setInterval(ta(O.Qg, this), O.Ad),
            this.Ib = !0
    }
    ;
    O.Fe = function() {
        if (this.Ib)
            O.me ? o.mozRequestAnimationFrame ? Hb >= 11 ? o.mozCancelRequestAnimationFrame(this.rb) : o.removeEventListener("MozBeforePaint", this.ve, !1) : o.webkitCancelRequestAnimationFrame(this.rb) : clearInterval(this.Ve),
            this.Ib = !1
    }
    ;
    O.se = function(a) {
        var b = o.performance, c;
        b && (c = b.now || b.webkitNow) ? a = b.timing.navigationStart + c.call(b) : a || (a = va());
        b = a - this.Ab;
        b < 0 && (b = 1);
        O.zd(b);
        this.Ab = a;
        o.webkitRequestAnimationFrame ? o.webkitRequestAnimationFrame(this.rb) : o.mozRequestAnimationFrame(this.rb)
    }
    ;
    O.zf = function(a) {
        O.zd(a.timeStamp - this.Ab);
        this.Ab = a.timeStamp;
        o.mozRequestAnimationFrame()
    }
    ;
    O.Qg = function() {
        var a = va()
          , b = a - this.Ab;
        b < 0 && (b = 1);
        O.zd(b);
        this.Ab = a
    }
    ;
    O.zd = function(a) {
        for (var b = this.Aa.slice(), c = b.length; --c >= 0; )
            b[c].bc(a);
        if (ya == 1 && /Firefox\/4./.test(wb()) && !xa.$g)
            O.kf ? (document.body.style.MozTransform = "",
            O.kf = 0) : (document.body.style.MozTransform = "scale(1,1)",
            O.kf = 1),
            ya = 0
    }
    ;
    O.Cf = function(a) {
        for (var b, c, d, e, g = this.Aa.length; --g >= 0; ) {
            b = this.Aa[g];
            for (e = b.cb.length; --e >= 0; )
                d = b.cb[e],
                c = d[2],
                la(c.ba) && (c = c.ba(),
                c == a && (d[0] = !0))
        }
    }
    ;
    O.Bf = function(a, b) {
        O.Db(a, b, 100, 1)
    }
    ;
    O.Db = function(a, b, c, d) {
        O.dd(a, b, new hf(c,d))
    }
    ;
    var jf;
    function kf() {
        this.Fb = [];
        this.Kd = [];
        this.gd = {};
        this.hh = !1;
        this.z = 1;
        this.bb = lf;
        this.$ = 0
    }
    s(kf, Ec);
    kf.prototype.scope = "";
    var T = "stop";
    n = kf.prototype;
    n.e = function(a) {
        this.z = a;
        return this
    }
    ;
    function mf(a, b) {
        a.bb = b;
        return a
    }
    n.qb = function(a) {
        ib(this.Fb, a);
        return this
    }
    ;
    n.play = function() {
        this.nf = 0;
        this.Me = this.$ = 1;
        O.dd(this.bc, this);
        this.dispatchEvent({
            type: "start"
        })
    }
    ;
    n.stop = function() {
        if (this.$ != 0) {
            var a = this.Kd;
            if (nf(this) && this.ga)
                for (var b = a.length; --b >= 0; )
                    this.ga(a[b]);
            this.Kd = [];
            this.gd = {};
            this.$ = 0;
            O.X(this.bc, this);
            this.dispatchEvent({
                type: T
            })
        }
    }
    ;
    n.Bb = function() {
        return {}
    }
    ;
    function of(a, b) {
        var c = na(b);
        p(a.gd[c]) || (a.zb(b),
        a.gd[c] = a.Bb(b));
        return a.gd[c]
    }
    n.zb = function(a) {
        pf.cd(this, a);
        this.$ = 1;
        ib(this.Kd, a);
        this.Fc && !this.ee && this.lc && this.lc()
    }
    ;
    n.ba = function() {
        return this.Fb[0] ? this.Fb[0].ba() : k
    }
    ;
    n.bc = function(a) {
        this.Fc && !this.ee && this.lc && this.lc();
        this.Me && (delete this.Me,
        a = 1);
        this.nf += a;
        this.eh = a;
        a = this.nf / (this.z * 1E3);
        if (isNaN(a) || a >= 1)
            a = 1;
        a = this.nb(a, this.Fb);
        a == 1 && this.stop()
    }
    ;
    n.nb = function(a, b) {
        a = this.bb[0](a);
        isNaN(a) && (a = 1);
        for (var c = b.length; --c >= 0; )
            this.update(a, b[c]);
        return a
    }
    ;
    function nf(a) {
        return a.z > 0 && xd && a.yg && !Hc && !Bb
    }
    function qf(a) {
        a.yg = p(i) ? i : !0;
        return a
    }
    var pf = new function() {
        this.C = {}
    }
    ;
    pf.cd = function(a, b) {
        if (a.scope.length) {
            var c = na(b);
            p(this.C[c]) || (this.C[c] = {});
            p(this.C[c][a.scope]) && this.C[c][a.scope].stop();
            this.C[c][a.scope] = a
        }
    }
    ;
    pf.Rg = function(a) {
        a = na(a);
        if (p(this.C[a]))
            for (var b in this.C[a])
                this.C[a][b].stop(),
                delete this.C[a][b]
    }
    ;
    (function() {
        function a(a) {
            var e, g, h, r;
            for (h = a,
            g = 0; g < 8; g++) {
                r = ((b * h + c) * h + d) * h - a;
                if ((r >= 0 ? r : 0 - r) < 5.0E-5)
                    return h;
                e = (3 * b * h + 2 * c) * h + d;
                if ((e >= 0 ? e : 0 - e) < 1.0E-6)
                    break;
                h -= r / e
            }
            e = 0;
            g = 1;
            h = a;
            if (h < e)
                return e;
            if (h > g)
                return g;
            for (; e < g; ) {
                r = ((b * h + c) * h + d) * h;
                if ((r - a >= 0 ? r - a : 0 - (r - a)) < 5.0E-5)
                    break;
                a > r ? e = h : g = h;
                h = (g - e) * 0.5 + e
            }
            return h
        }
        var b = 0
          , c = 0
          , d = 0
          , e = 0
          , g = 0
          , h = 0;
        jf = function(m, l, q, A) {
            return [function(r) {
                d = 3 * m;
                c = 3 * (q - m) - d;
                b = 1 - d - c;
                h = 3 * l;
                g = 3 * (A - l) - h;
                e = 1 - h - g;
                return ((e * a(r) + g) * a(r) + h) * a(r)
            }
            , m, l, q, A]
        }
    }
    )();
    var rf = jf(0.42, 0, 1, 1)
      , sf = jf(0, 0, 0.58, 1)
      , lf = jf(0.42, 0, 0.58, 1);
    var tf = {
        aliceblue: "#f0f8ff",
        antiquewhite: "#faebd7",
        aqua: "#00ffff",
        aquamarine: "#7fffd4",
        azure: "#f0ffff",
        beige: "#f5f5dc",
        bisque: "#ffe4c4",
        black: "#000000",
        blanchedalmond: "#ffebcd",
        blue: "#0000ff",
        blueviolet: "#8a2be2",
        brown: "#a52a2a",
        burlywood: "#deb887",
        cadetblue: "#5f9ea0",
        chartreuse: "#7fff00",
        chocolate: "#d2691e",
        coral: "#ff7f50",
        cornflowerblue: "#6495ed",
        cornsilk: "#fff8dc",
        crimson: "#dc143c",
        cyan: "#00ffff",
        darkblue: "#00008b",
        darkcyan: "#008b8b",
        darkgoldenrod: "#b8860b",
        darkgray: "#a9a9a9",
        darkgreen: "#006400",
        darkgrey: "#a9a9a9",
        darkkhaki: "#bdb76b",
        darkmagenta: "#8b008b",
        darkolivegreen: "#556b2f",
        darkorange: "#ff8c00",
        darkorchid: "#9932cc",
        darkred: "#8b0000",
        darksalmon: "#e9967a",
        darkseagreen: "#8fbc8f",
        darkslateblue: "#483d8b",
        darkslategray: "#2f4f4f",
        darkslategrey: "#2f4f4f",
        darkturquoise: "#00ced1",
        darkviolet: "#9400d3",
        deeppink: "#ff1493",
        deepskyblue: "#00bfff",
        dimgray: "#696969",
        dimgrey: "#696969",
        dodgerblue: "#1e90ff",
        firebrick: "#b22222",
        floralwhite: "#fffaf0",
        forestgreen: "#228b22",
        fuchsia: "#ff00ff",
        gainsboro: "#dcdcdc",
        ghostwhite: "#f8f8ff",
        gold: "#ffd700",
        goldenrod: "#daa520",
        gray: "#808080",
        green: "#008000",
        greenyellow: "#adff2f",
        grey: "#808080",
        honeydew: "#f0fff0",
        hotpink: "#ff69b4",
        indianred: "#cd5c5c",
        indigo: "#4b0082",
        ivory: "#fffff0",
        khaki: "#f0e68c",
        lavender: "#e6e6fa",
        lavenderblush: "#fff0f5",
        lawngreen: "#7cfc00",
        lemonchiffon: "#fffacd",
        lightblue: "#add8e6",
        lightcoral: "#f08080",
        lightcyan: "#e0ffff",
        lightgoldenrodyellow: "#fafad2",
        lightgray: "#d3d3d3",
        lightgreen: "#90ee90",
        lightgrey: "#d3d3d3",
        lightpink: "#ffb6c1",
        lightsalmon: "#ffa07a",
        lightseagreen: "#20b2aa",
        lightskyblue: "#87cefa",
        lightslategray: "#778899",
        lightslategrey: "#778899",
        lightsteelblue: "#b0c4de",
        lightyellow: "#ffffe0",
        lime: "#00ff00",
        limegreen: "#32cd32",
        linen: "#faf0e6",
        magenta: "#ff00ff",
        maroon: "#800000",
        mediumaquamarine: "#66cdaa",
        mediumblue: "#0000cd",
        mediumorchid: "#ba55d3",
        mediumpurple: "#9370d8",
        mediumseagreen: "#3cb371",
        mediumslateblue: "#7b68ee",
        mediumspringgreen: "#00fa9a",
        mediumturquoise: "#48d1cc",
        mediumvioletred: "#c71585",
        midnightblue: "#191970",
        mintcream: "#f5fffa",
        mistyrose: "#ffe4e1",
        moccasin: "#ffe4b5",
        navajowhite: "#ffdead",
        navy: "#000080",
        oldlace: "#fdf5e6",
        olive: "#808000",
        olivedrab: "#6b8e23",
        orange: "#ffa500",
        orangered: "#ff4500",
        orchid: "#da70d6",
        palegoldenrod: "#eee8aa",
        palegreen: "#98fb98",
        paleturquoise: "#afeeee",
        palevioletred: "#d87093",
        papayawhip: "#ffefd5",
        peachpuff: "#ffdab9",
        peru: "#cd853f",
        pink: "#ffc0cb",
        plum: "#dda0dd",
        powderblue: "#b0e0e6",
        purple: "#800080",
        red: "#ff0000",
        rosybrown: "#bc8f8f",
        royalblue: "#4169e1",
        saddlebrown: "#8b4513",
        salmon: "#fa8072",
        sandybrown: "#f4a460",
        seagreen: "#2e8b57",
        seashell: "#fff5ee",
        sienna: "#a0522d",
        silver: "#c0c0c0",
        skyblue: "#87ceeb",
        slateblue: "#6a5acd",
        slategray: "#708090",
        slategrey: "#708090",
        snow: "#fffafa",
        springgreen: "#00ff7f",
        steelblue: "#4682b4",
        tan: "#d2b48c",
        teal: "#008080",
        thistle: "#d8bfd8",
        tomato: "#ff6347",
        turquoise: "#40e0d0",
        violet: "#ee82ee",
        wheat: "#f5deb3",
        white: "#ffffff",
        whitesmoke: "#f5f5f5",
        yellow: "#ffff00",
        yellowgreen: "#9acd32"
    };
    function uf(a) {
        var b = {}
          , a = String(a)
          , c = a.charAt(0) == "#" ? a : "#" + a;
        if (vf.test(c))
            return b.Jd = wf(c),
            b.type = "hex",
            b;
        else {
            a: {
                var d = a.match(xf);
                if (d) {
                    var c = Number(d[1])
                      , e = Number(d[2])
                      , d = Number(d[3]);
                    if (c >= 0 && c <= 255 && e >= 0 && e <= 255 && d >= 0 && d <= 255) {
                        c = [c, e, d];
                        break a
                    }
                }
                c = []
            }
            if (c.length) {
                e = c[0];
                a = c[1];
                c = c[2];
                e = Number(e);
                a = Number(a);
                c = Number(c);
                if (isNaN(e) || e < 0 || e > 255 || isNaN(a) || a < 0 || a > 255 || isNaN(c) || c < 0 || c > 255)
                    throw Error('"(' + e + "," + a + "," + c + '") is not a valid RGB color');
                e = yf(e.toString(16));
                a = yf(a.toString(16));
                c = yf(c.toString(16));
                b.Jd = "#" + e + a + c;
                b.type = "rgb";
                return b
            } else if (tf && (c = tf[a.toLowerCase()]))
                return b.Jd = c,
                b.type = "named",
                b
        }
        throw Error(a + " is not a valid color string");
    }
    var zf = /#(.)(.)(.)/;
    function wf(a) {
        if (!vf.test(a))
            throw Error("'" + a + "' is not a valid hex color");
        a.length == 4 && (a = a.replace(zf, "#$1$1$2$2$3$3"));
        return a.toLowerCase()
    }
    function Af(a, b, c) {
        c < 0 ? c += 1 : c > 1 && (c -= 1);
        if (6 * c < 1)
            return a + (b - a) * 6 * c;
        else if (2 * c < 1)
            return b;
        else if (3 * c < 2)
            return a + (b - a) * (2 / 3 - c) * 6;
        return a
    }
    var vf = /^#(?:[0-9a-f]{3}){1,2}$/i
      , xf = /^(?:rgb)?\((0|[1-9]\d{0,2}),\s?(0|[1-9]\d{0,2}),\s?(0|[1-9]\d{0,2})\)$/i;
    function yf(a) {
        return a.length == 1 ? "0" + a : a
    }
    ;function Bf() {}
    s(Bf, Ec);
    Bf.prototype.vc = fa;
    function Cf(a) {
        if (a[0]instanceof Bf)
            return a[0];
        ha(a) || (a = mb(arguments));
        if (a.length > 2)
            return new Df(a);
        else if (ja(a[0]) && (a[0].substring(0, 4) == "rgb(" || a[0].substring(0, 5) == "rgba(" || a[0].substring(0, 1) == "#"))
            return new Df(a[0]);
        return new Ef(a[0])
    }
    Bf.prototype.Eb = fa;
    Bf.prototype.Zb = fa;
    function Df(a) {
        this.pb = 1;
        this.Ua(a)
    }
    s(Df, Bf);
    n = Df.prototype;
    n.id = "color";
    function Ff(a, b) {
        return Gf(a, 2, b)
    }
    function Gf(a, b, c) {
        var c = c || 0.1, d, e = k;
        if (ka(a.Xb) && ka(a.Rb) && ka(a.Kb))
            e = [a.Xb, a.Rb, a.Kb, a.pb];
        else if (ja(a.la)) {
            var g = uf(a.la);
            if (g.type != "named")
                e = g.Jd,
                e = wf(e),
                e = [parseInt(e.substr(1, 2), 16), parseInt(e.substr(3, 2), 16), parseInt(e.substr(5, 2), 16)];
            e.push(1)
        }
        d = e;
        if (!d)
            return a;
        d.pop();
        e = d[0] / 255;
        g = d[1] / 255;
        d = d[2] / 255;
        var h = Math.max(e, g, d)
          , m = Math.min(e, g, d)
          , l = 0
          , q = 0
          , A = 0.5 * (h + m);
        h != m && (h == e ? l = 60 * (g - d) / (h - m) : h == g ? l = 60 * (d - e) / (h - m) + 120 : h == d && (l = 60 * (e - g) / (h - m) + 240),
        q = 0 < A && A <= 0.5 ? (h - m) / (2 * A) : (h - m) / (2 - 2 * A));
        d = [Math.round(l + 360) % 360, q, A];
        d[b] += c;
        d[b] > 1 && (d[b] = 1);
        b = d[1];
        c = d[2];
        h = g = e = 0;
        d = d[0] / 360;
        b == 0 ? e = g = h = c * 255 : (m = h = 0,
        m = c < 0.5 ? c * (1 + b) : c + b - b * c,
        h = 2 * c - m,
        e = 255 * Af(h, m, d + 1 / 3),
        g = 255 * Af(h, m, d),
        h = 255 * Af(h, m, d - 1 / 3));
        d = [Math.round(e), Math.round(g), Math.round(h)];
        d.push(a.pb);
        return a.Ua(d)
    }
    n.Ua = function(a) {
        var b = a;
        if (ja(a))
            return this.la = a,
            this;
        arguments.length > 2 && (b = arguments);
        if (b.length >= 3)
            this.Xb = b[0],
            this.Rb = b[1],
            this.Kb = b[2];
        if (b.length == 4)
            this.pb = b[3];
        this.la = this.pb == 1 ? "rgb(" + this.Xb + "," + this.Rb + "," + this.Kb + ")" : "rgba(" + this.Xb + "," + this.Rb + "," + this.Kb + "," + this.pb + ")";
        return this
    }
    ;
    n.Eb = function(a) {
        a.style.background = this.la
    }
    ;
    n.Zb = function(a) {
        a.fillStyle = this.la
    }
    ;
    n.r = function() {
        var a = new Df("");
        a.Xb = this.Xb;
        a.Rb = this.Rb;
        a.Kb = this.Kb;
        a.pb = this.pb;
        a.la = this.la;
        return a
    }
    ;
    function Hf(a, b) {
        var c = ha(a) ? a : mb(arguments);
        this.Wa = c[0] || 1;
        c.shift();
        this.Ua.apply(this, c)
    }
    s(Hf, Bf);
    n = Hf.prototype;
    n.id = "stroke";
    n.Eb = function(a) {
        a.style.border = this.Wa + "px solid " + this.sb.la
    }
    ;
    n.Zb = function(a) {
        a.strokeStyle = this.sb.la;
        a.lineWidth = this.Wa
    }
    ;
    n.Ua = function(a) {
        var b = mb(arguments);
        b[0]instanceof Df ? this.sb = b[0] : (this.sb = new Df("#000"),
        b.length && this.sb.Ua.apply(this.sb, b));
        return this
    }
    ;
    n.r = function() {
        var a = new Hf;
        a.Wa = this.Wa;
        a.sb = this.sb;
        return a
    }
    ;
    function Ef(a) {
        a && la(a.data) && (a = a.data());
        if (ja(a)) {
            this.na = a;
            if (this.na.length > 50)
                this.na = this.na.substr(-50);
            If[this.na] ? this.J = If[this.na] : (this.J = new Image,
            this.J.src = a)
        } else {
            this.na = a.src;
            if (this.na.length > 50)
                this.na = this.na.substr(-50);
            this.J = If[this.na] ? If[this.na] : a
        }
        this.Tb() || w(this.J, "load", this.ag, !1, this);
        If[this.na] = this.J
    }
    s(Ef, Bf);
    var If = {};
    n = Ef.prototype;
    n.id = "image";
    n.vc = function(a) {
        var b = a.t()
          , c = this;
        !b.width && !b.height && (this.Tb() ? a.b(this.J.width, this.J.height) : w(this, "load", function() {
            var a = this.t();
            !a.width && !a.height && this.b(c.J.width, c.J.height)
        }, !1, a));
        this.Tb() || w(this, "load", function() {
            z(a, 4)
        }, !1, this)
    }
    ;
    n.ag = function(a) {
        this.dispatchEvent(a)
    }
    ;
    n.Qe = aa("J");
    n.Tb = function() {
        return !(!this.J || !this.J.width || !this.J.height)
    }
    ;
    n.b = function(a, b, c) {
        ka(a) && (a = new Da(a,b),
        b = c || !1);
        this.U = a;
        this.Kg = b;
        return this
    }
    ;
    function Jf(a, b) {
        var c = b.t().r();
        if (a.U)
            a.Kg ? (c.width *= a.U.width,
            c.height *= a.U.height) : c = a.U;
        var d = new t(0,0);
        if (a.Zd)
            a.mh ? (d.x = c.width * a.Zd.x,
            d.y = c.height * a.Zd.y) : d = a.Zd;
        return [c, d]
    }
    function Kf(a, b, c) {
        var d = Jf(a, c)
          , e = d[0]
          , d = d[1]
          , g = Xd(c);
        b.style[wd("BackgroundSize")] = e.width * g + "px " + e.height * g + "px";
        c = c.ea ? c.ea.Wa : 0;
        b.style.backgroundPosition = d.x * g - c + "px " + (d.y * g - c) + "px";
        a.qh && (b.style.imageRendering = "optimizeQuality")
    }
    n.Eb = function(a, b) {
        a.style.background = "url(" + this.J.src + ")";
        Kf(this, a, b)
    }
    ;
    n.Zb = function(a, b) {
        var c = b.t()
          , d = b.m();
        if (c.width && c.height)
            try {
                var e = this.Qe()
                  , g = Jf(this, b)
                  , h = g[0]
                  , m = g[1]
                  , l = a.createPattern(e, "repeat")
                  , q = h.width / e.width
                  , A = h.height / e.height;
                a.save();
                a.translate(d.left + m.x, d.top + m.y);
                a.scale(q, A);
                a.fillStyle = l;
                a.fillRect(-m.x / q, -m.y / A, c.width / q, c.height / A);
                a.restore()
            } catch (r) {}
    }
    ;
    u.O = {};
    v.O = {};
    function P() {
        Dd.call(this);
        this.ea = this.Qb = k
    }
    s(P, Dd);
    P.prototype.id = "sprite";
    P.prototype.Va = [Ha(v, v.O), Ha(u, u.O)];
    P.prototype.c = function(a, b, c, d) {
        this.Qb = Cf(mb(arguments));
        this.Qb.vc(this);
        z(this, 4);
        return this
    }
    ;
    P.prototype.vf = function(a) {
        a && !(a instanceof Hf) && (a = new Hf(mb(arguments)));
        this.ea = a;
        z(this, 4);
        return this
    }
    ;
    v.O.R = function(a) {
        this.Qb === k || this.Qb.Eb(a, this);
        this.ea === k ? ja("border-width") ? kd(a, 0, "border-width") : Sb("border-width", ua(kd, a)) : this.ea.Eb(a, this)
    }
    ;
    u.O.R = function(a) {
        var b = this.t()
          , c = this.Qb
          , d = this.ea;
        if (c || d) {
            var e = this.m();
            c && (c.Zb(a, this),
            c.id != "image" && c.id != "frame" && a.fillRect(e.left, e.top, b.width, b.height));
            if (d && (d.Zb(a, this),
            this.id == "sprite" || this.id == "label"))
                c = d.Wa / 2,
                a.strokeRect(e.left + c, e.top + c, b.width - 2 * c, b.height - 2 * c)
        }
    }
    ;
    function Lf(a, b) {
        kf.call(this);
        this.nc = arguments.length == 2 ? new t(arguments[0],arguments[1]) : a
    }
    s(Lf, kf);
    n = Lf.prototype;
    n.scope = "move";
    n.Bb = function(a) {
        nf(this) && (a.Ba[La] = [new t(a.f.x + this.nc.x,a.f.y + this.nc.y), this.z, this.bb, 0],
        z(a, Jd));
        return {
            Gc: a.f
        }
    }
    ;
    n.lc = function() {
        if (this.Fc)
            this.e(this.Fc * Ba(this.nc) / 100),
            this.ee = 1
    }
    ;
    n.update = function(a, b) {
        if (this.$ != 0) {
            var c = of(this, b);
            b.a(c.Gc.x + this.nc.x * a, c.Gc.y + this.nc.y * a)
        }
    }
    ;
    n.ga = function(a) {
        nf(this) && (a.ga(La),
        z(a, Jd))
    }
    ;
    function Mf(a, b) {
        this.z = 1;
        this.jb = a;
        this.ra = b;
        this.Mf = !1
    }
    s(Mf, Ec);
    Mf.prototype.e = function(a) {
        this.z = a;
        return this
    }
    ;
    Mf.prototype.start = function() {
        this.ra.a(new t(0,0));
        B(this.ra, !1);
        this.finish()
    }
    ;
    Mf.prototype.finish = function() {
        this.dispatchEvent(new Yb("end"));
        this.Mf = !0
    }
    ;
    function Nf(a, b, c) {
        Mf.call(this, a, b);
        this.gf = Of;
        this.tg = c || !1
    }
    s(Nf, Mf);
    var Of = 0;
    Nf.prototype.start = function() {
        var a = this.ra.t()
          , b = new t(0,0);
        switch (this.gf) {
        case Of:
            this.ra.a(-a.width, 0);
            b.x = a.width;
            break;
        case 1:
            this.ra.a(0, -a.height);
            b.y = a.height;
            break;
        case 2:
            this.ra.a(a.width, 0);
            b.x = -a.width;
            break;
        case 4:
            this.ra.a(0, a.height),
            b.y = -a.height
        }
        B(this.ra, !1);
        a = (new Lf(b)).e(this.z);
        this.jb && !this.tg && a.qb(this.jb);
        a.qb(this.ra);
        w(a, T, this.finish, !1, this);
        a.play()
    }
    ;
    Nf.prototype.finish = function() {
        this.jb && this.jb.a(0, 0);
        Mf.prototype.finish.call(this)
    }
    ;
    function ff(a, b, c) {
        Nf.call(this, a, b, c);
        this.gf = 4
    }
    s(ff, Nf);
    function S(a, b) {
        kf.call(this);
        this.f = arguments.length == 2 ? new t(arguments[0],arguments[1]) : a
    }
    s(S, kf);
    n = S.prototype;
    n.scope = "move";
    n.Bb = function(a) {
        var b = a.f
          , c = new t(this.f.x - b.x,this.f.y - b.y);
        nf(this) && (a.Ba[La] = [this.f, this.z, this.bb, 0],
        z(a, Jd));
        return {
            Gc: b,
            V: c
        }
    }
    ;
    n.lc = function() {
        if (this.Fc && this.Fb.length) {
            var a = this.Fb[0].f;
            this.e(this.Fc * Ba(new t(this.f.x - a.x,this.f.y - a.y)) / 100);
            this.ee = 1
        }
    }
    ;
    n.update = function(a, b) {
        if (this.$ != 0) {
            var c = of(this, b);
            b.a(c.Gc.x + c.V.x * a, c.Gc.y + c.V.y * a)
        }
    }
    ;
    n.ga = function(a) {
        nf(this) && (a.ga(La),
        z(a, Jd))
    }
    ;
    function Pf() {
        P.call(this);
        this.b(100, 100);
        var a = (new P).c("#c00").b(100, 100);
        a.od = 63;
        this.Fa = z(a, 7);
        this.appendChild(this.Fa);
        Od(this, this.Fa);
        this.F = new H;
        Dd.prototype.appendChild.call(this, this.F);
        w(this, ["mousedown", "touchstart"], this.If, !1, this);
        this.$b(Qf)
    }
    s(Pf, P);
    var Qf = 0;
    n = Pf.prototype;
    n.Oa = function() {
        if (this.event)
            this.event.ja(),
            this.event = k;
        if (this.Fa)
            Bc(this.Fa),
            this.Fa.ib = k,
            this.Fa = this.Fa.fd = k;
        if (this.F) {
            Bc(this.F);
            for (var a = this.F; $d(a); )
                ae(a, 0);
            this.F = k
        }
        this.La = this.A = k;
        Pf.kb.Oa.call(this)
    }
    ;
    n.$b = function(a) {
        this.oc = a;
        return this
    }
    ;
    n.d = function() {
        this.Fa && this.Fa.d.apply(this.Fa, arguments);
        return Dd.prototype.d.apply(this, arguments)
    }
    ;
    n.appendChild = function() {
        return this.F ? this.F.appendChild.apply(this.F, arguments) : Dd.prototype.appendChild.apply(this, arguments)
    }
    ;
    n.removeChild = function() {
        return this.F ? this.F.removeChild.apply(this.F, arguments) : Dd.prototype.removeChild.apply(this, arguments)
    }
    ;
    function Rf(a) {
        var b = a.F.zc();
        if (a.oc == Qf) {
            a.sc = a.F.f.y;
            var c = a.t().width;
            a.fa = -b.left;
            a.oa = Math.min(c - b.right, -b.left);
            b = b.right - b.left - c
        } else
            a.rc = a.F.f.x,
            c = a.t().height,
            a.fa = -b.top,
            a.oa = Math.min(c - b.bottom, -b.top),
            b = b.bottom - b.top - c;
        b > 0 && (a.fa -= b,
        a.oa += b)
    }
    n.scrollTo = function(a, b) {
        var c = this.F.f.r()
          , d = b || 0;
        Rf(this);
        a < 0 && (a = 0);
        if (this.oc == Qf) {
            if (c.x = this.oa - a,
            c.x < this.fa)
                c.x = this.fa
        } else if (c.y = this.oa - a,
        c.y < this.fa)
            c.y = this.fa;
        d ? G(this.F, mf(qf((new S(c.x,c.y)).e(d)), jf(0.19, 0.6, 0.35, 0.97))) : this.F.a(c)
    }
    ;
    n.If = function(a) {
        if (!this.Md)
            a.position = Hd(this, a.position, this.F),
            this.rc = a.position.x,
            this.sc = a.position.y,
            this.dc = 0,
            this.Md = 1,
            this.Zc = this.oc == Qf ? this.ad = this.F.f.x : this.ad = this.F.f.y,
            Rf(this),
            pf.Rg(this.F),
            O.dd(this.xe, this),
            a.w(["touchmove", "mousemove"], this.Vd),
            a.w(["touchend", "mouseup", "touchcancel"], this.Xg),
            this.event = a.r()
    }
    ;
    n.xe = function() {
        if (this.Md)
            this.dc = (this.ad - this.Zc) * 1.05,
            this.Zc = this.ad;
        this.dc *= 0.95
    }
    ;
    n.Vd = function(a) {
        var a = a.position.r(), b = this.oc, c;
        b == Qf ? (a.x -= this.rc,
        a.y = this.sc,
        c = a.x) : (a.x = this.rc,
        a.y -= this.sc,
        c = a.y);
        c < this.fa && (c = this.fa - c,
        c > 250 && (c = 250),
        c = this.fa - c * 0.4);
        c > this.oa && (c -= this.oa,
        c > 250 && (c = 250),
        c = this.oa + c * 0.4);
        this.ad = c;
        b == Qf ? a.x = c : a.y = c;
        this.F.a(a)
    }
    ;
    n.Xg = function(a) {
        var a = a.position.r(), b = this.oc, c;
        b == Qf ? (a.x -= this.rc,
        a.y = this.sc,
        c = a.x) : (a.x = this.rc,
        a.y -= this.sc,
        c = a.y);
        O.X(this.xe, this);
        var d = Math.log(0.5 / Math.abs(this.dc)) / Math.log(0.95)
          , e = d / 30
          , d = Math.abs(this.dc) * (Math.pow(0.95, d) - 1) / (0.95 - 1) * (this.dc > 0 ? 1 : -1);
        c += d;
        this.Md = 0;
        if (this.dc != 0) {
            var g = d;
            if (c < this.fa)
                g = this.fa - (c - d),
                c = this.fa;
            if (c > this.oa)
                g = this.oa - (c - d),
                c = this.oa;
            e *= g / d
        }
        if (this.Zc < this.fa)
            c = this.fa,
            e = 0.3;
        if (this.Zc > this.oa)
            c = this.oa,
            e = 0.3;
        b == Qf ? a.x = c : a.y = c;
        Math.abs(e) < 10 && G(this.F, mf(qf((new S(a.x,a.y)).e(e)), jf(0.19, 0.6, 0.35, 0.97)))
    }
    ;
    function Ja() {
        Dd.call(this);
        this.d(0, 0);
        this.qc = "lime-scene";
        Rd(this)
    }
    s(Ja, Dd);
    Ja.prototype.Nc = function() {
        return this
    }
    ;
    Ja.prototype.zc = function() {
        return this.m()
    }
    ;
    function gf(a, b, c) {
        Ja.call(this);
        moveToPosY = 250;
        currentPage = 1;
        this.appendChild((new P).c(J + "bgLevelSelect.jpg").b(960, 750).a(0, -150).d(0, 0));
        Ee = (new H).a(490, 250);
        this.appendChild(Ee);
        var d = K(L(M(new N, "futuraBold"), "#fff"), 28).b(650, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Check out the new SmartGames for 2015!").a(0, -95).d(0.5, 0.5);
        Ee.appendChild(d);
        var d = (new P).d(0, 0).a(0, 0)
          , e = (new P).b(350, 350).d(0, 0).c(J + "3piggies.png").d(0.5, 0.5).a(-210, 100)
          , g = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("THREE LITTLE PIGGIES").a(-165, -50).d(0, 0)
          , h = K(L(M(new N, "futuraBold"), "#fff"), 18).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Once upon a time... ").a(-202, 5).d(0, 0)
          , m = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Three Little Piggies is a perfect brain game for young children. It features 3 big puzzle pieces that are easy to hold, and kids will be intrigued by the way the pigs fit inside the houses and look through the windows.");
        af(m.a(5, 150).d(0, 0.5), "left");
        var l = (new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 300);
        d.appendChild(e);
        d.appendChild(g);
        d.appendChild(h);
        d.appendChild(m);
        d.appendChild(l);
        e = (new P).d(0, 0).a(0, 420);
        g = (new P).b(350, 350).d(0, 0).c(J + "butterflies.png").d(0.5, 0.5).a(-210, 100);
        h = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("BUTTERFLIES").a(-219, -50).d(0, 0);
        m = K(L(M(new N, "futuraBold"), "#fff"), 16).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Spread your wings... ").a(-207, 5).d(0, 0);
        l = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Wings of Wonder is a unique and fun sliding puzzle featuring 48 challenges, from easy to expert. A perfect, compact travel game that includes a storage compartment for the puzzle pieces and challenge booklet.");
        af(l.a(5, 150).d(0, 0.5), "left");
        var q = (new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 300);
        e.appendChild(g);
        e.appendChild(h);
        e.appendChild(m);
        e.appendChild(l);
        e.appendChild(q);
        g = (new P).d(0, 0).a(0, 820);
        h = (new P).b(350, 350).d(0, 0).c(J + "iqblox.png").d(0.5, 0.5).a(-210, 100);
        m = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("IQ-BLOX").a(-243, -50).d(0, 0);
        l = K(L(M(new N, "futuraBold"), "#fff"), 16).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Think out of the Blox!").a(-205, 5).d(0, 0);
        q = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("In IQ-Blox the walls don\u2019t block, instead they help you find solutions. Use the walls as guides as you fill the game board with colorful puzzle pieces. From easy to expert, IQ-Blox includes 120 challenges that are easy to set up ... but hard to put down!");
        af(q.a(5, 150).d(0, 0.5), "left");
        var A = (new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 300);
        g.appendChild(h);
        g.appendChild(m);
        g.appendChild(l);
        g.appendChild(q);
        g.appendChild(A);
        h = (new P).d(0, 0).a(0, 1220);
        m = (new P).b(350, 350).d(0, 0).c(J + "iqcandy.png").d(0.5, 0.5).a(-210, 100);
        l = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("IQ-CANDY").a(-230, -50).d(0, 0);
        q = K(L(M(new N, "futuraBold"), "#fff"), 16).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Dessert...for your brain!").a(-193, 5).d(0, 0);
        A = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Can you fit all of the candy-colored puzzle pieces on the game board? Treat your mind with this unique puzzle game. Featuring 60 challenges\u2026you\u2019ll be on a (sugar-free) rush for hours! A perfect birthday gift. WARNING! IQ Candy may look sweet, but it is not edible. Don\u2019t eat the pieces!");
        af(A.a(5, 150).d(0, 0.5), "left");
        var r = (new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 300);
        h.appendChild(m);
        h.appendChild(l);
        h.appendChild(q);
        h.appendChild(A);
        h.appendChild(r);
        m = (new P).d(0, 0).a(0, 1620);
        l = (new P).b(350, 350).d(0, 0).c(J + "penguinsparade.png").d(0.5, 0.5).a(-210, 100);
        q = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("PENGUINS PARADE").a(-175, -50).d(0, 0);
        A = K(L(M(new N, "futuraBold"), "#fff"), 16).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Get the penguins in line!").a(-193, 5).d(0, 0);
        r = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("If you liked Penguins on Ice from SmartGames, get ready for Penguins Parade! This new magnetic travel game provides hours of fun, with 48 challenges included. Penguins Parade is a great brain game for kids, and perfect for travel.");
        af(r.a(5, 150).d(0, 0.5), "left");
        var X = (new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 300);
        m.appendChild(l);
        m.appendChild(q);
        m.appendChild(A);
        m.appendChild(r);
        m.appendChild(X);
        l = (new P).d(0, 0).a(0, 2020);
        q = (new P).b(350, 350).d(0, 0).c(J + "tangoesanimals.png").d(0.5, 0.5).a(-210, 100);
        A = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("TANGOES ANIMALS").a(-175, -50).d(0, 0);
        r = af(K(L(M(new N, "futuraBold"), "#fff"), 16).b(250, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("'seven shapes, endless ways to combine'").a(5, 5).d(0, 0), "left");
        X = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Travel Tangoes delivers all the fun of traditional Tangrams \u2026. in a compact form! Great for short trips, long journeys or even staying at home. Tangoes Animals includes a total of 48 challenges. ");
        af(X.a(5, 170).d(0, 0.5), "left");
        var ca = (new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 300);
        l.appendChild(q);
        l.appendChild(A);
        l.appendChild(r);
        l.appendChild(X);
        l.appendChild(ca);
        q = (new P).d(0, 0).a(0, 2420);
        A = (new P).b(350, 350).d(0, 0).c(J + "tangoesparadox.png").d(0.5, 0.5).a(-210, 100);
        r = K(L(M(new N, "futuraBold"), "#fff"), 24).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("TANGOES PARADOX").a(-170, -50).d(0, 0);
        X = K(L(M(new N, "futuraBold"), "#fff"), 16).b(600, 70).B("rgba(0,0,0,0.4)", 2, 2, 2).g("'A mystery wrapped in a puzzle'").a(-162, 5).d(0, 0);
        ca = K(L(M(new N, "futuraBold"), "#fff"), 16).b(300, 200).B("rgba(0,0,0,0.4)", 2, 2, 2).g("Each pair of challenges shows two nearly identical images, except that one image appears to be missing a piece, Yet both images can be recreated using the same 7 tangram puzzle pieces. How is this possible? Can you solve this paradox? Great for short trips, long journeys or even staying at home.");
        af(ca.a(5, 150).d(0, 0.5), "left");
        var cc = Nd((new P).b(300, 15).c(J + "stripeArrow.png").d(0.5, 0.5).a(0, 340), 180);
        q.appendChild(A);
        q.appendChild(r);
        q.appendChild(X);
        q.appendChild(ca);
        q.appendChild(cc);
        Ee.appendChild(d);
        Ee.appendChild(e);
        Ee.appendChild(g);
        Ee.appendChild(h);
        Ee.appendChild(m);
        Ee.appendChild(l);
        Ee.appendChild(q);
        this.appendChild((new P).c(J + "banner.png").b(960, 129).a(0, 0).d(0, 0));
        this.appendChild(Nd((new P).c(J + "levelSelectArrowBg.png").a(870, 245).d(0.5, 0.5), 90).l(0.75));
        this.appendChild(Nd((new P).c(J + "levelSelectArrowBg.png").a(870, 360).d(0.5, 0.5), 270).l(0.75));
        Fe = B(Nd((new P).c(J + "levelSelectArrow.png").b(47, 81).a(870, 245).d(0.5, 0.5), 90), !0);
        w(Fe, ["mousedown", "touchstart"], function() {
            currentPage--;
            currentPage < 7 && B(Ge, !1);
            currentPage == 1 && B(Fe, !0);
            moveToPosY += currentPage < 6 ? 400 : 440;
            if (currentPage > 0) {
                var a = mf((new S(490,moveToPosY)).e(0.6), sf);
                G(Ee, a)
            }
            a = new Sf((new U(1.5)).e(0.1),(new U(1)).e(0.1));
            G(Fe, a);
            Q.n.reload();
            Q.n.play()
        });
        this.appendChild(Fe);
        Ge = Nd((new P).c(J + "levelSelectArrow.png").b(47, 81).a(870, 360).d(0.5, 0.5), 270);
        w(Ge, ["mousedown", "touchstart"], function() {
            currentPage++;
            currentPage > 1 && B(Fe, !1);
            currentPage == 7 && B(Ge, !0);
            moveToPosY -= currentPage < 7 ? 400 : 440;
            if (currentPage < 8) {
                var a = mf((new S(490,moveToPosY)).e(0.6), sf);
                G(Ee, a)
            }
            a = new Sf((new U(1.5)).e(0.1),(new U(1)).e(0.1));
            G(Ge, a);
            Q.n.reload();
            Q.n.play()
        });
        this.appendChild(Ge);
        d = new Tf(new Sf((new V(0.65)).e(0.75),(new V(1)).e(0.75)));
        d.qb(Fe);
        d.qb(Ge);
        d.play();
        He == "all" ? (d = (new cf(I.home,"iconHome.png")).a(100, 570),
        w(d, ["mousedown", "touchstart"], function() {
            var a = new Q;
            Q.n.reload();
            Q.n.play();
            De ? R(a) : R(a, df)
        }),
        this.appendChild(d),
        a && (a = (new cf(I.resume,"iconResume.png")).a(800, 570),
        w(a, ["mousedown", "touchstart"], function() {
            var a = new F(b,c);
            Q.n.reload();
            Q.n.play();
            De ? R(a) : R(a, df)
        }),
        this.appendChild(a))) : (d = (new cf(I.home,"icon" + He + "Home.png")).a(100, 570),
        w(d, ["mousedown", "touchstart"], function() {
            var a = new Q(!1,He);
            Q.n.reload();
            Q.n.play();
            De ? R(a) : R(a, df)
        }),
        this.appendChild(d),
        a && (a = (new cf(I.resume,"iconResume.png")).a(800, 570),
        w(a, ["mousedown", "touchstart"], function() {
            var a = new F(b,c);
            Q.n.reload();
            Q.n.play();
            De ? R(a) : R(a, df)
        }),
        this.appendChild(a)));
        this.appendChild((new P).c(J + "sgLogo.png").b(109, 140).a(20, 20).d(0, 0))
    }
    s(gf, Ja);
    var Wf = {
        df: function(a) {
            scoresPopup = (new H).a(0, -600).b(450, 450).d(0, 0);
            popUpRect = (new Xe).c(J + "popupBlank.png").b(450, 450).a(480, 276);
            scoresPopup.appendChild(popUpRect);
            closeBtn = (new ef(I.close)).a(482, 410);
            w(closeBtn, ["mousedown", "touchstart"], function() {
                Q.n.play();
                Uf(closeBtn, a)
            });
            scoresPopup.appendChild(closeBtn);
            var b = M(L(K(new N, 38).g(I.scores), "#fff"), "futuraBold").a(0, -140);
            popUpRect.appendChild(b);
            b = M(L(K(new N, 18).g(I.name), "#fff"), "futuraBold").a(-100, -100);
            popUpRect.appendChild(b);
            b = M(L(K(new N, 18).g(I.highscore), "#fff"), "futuraBold").a(95, -100);
            popUpRect.appendChild(b);
            b = (new P).c("#fff").b(326, 3).a(0, -115);
            popUpRect.appendChild(b);
            b = (new P).c("#fff").b(326, 3).a(0, -85);
            popUpRect.appendChild(b);
            b = (new Pf).d(0, 0).b(315, 190).$b(1).a(320, 198);
            scoresText = (new H).a(0, 0);
            for (var c = ue(), d = 1; d <= Vf(c); d++) {
                var e = M(L(K(new N, 20).g(d), "#fff"), "futuraBold").a(10, d * 20).b(20, 20);
                scoresText.appendChild(e);
                e = M(af(L(K(new N, 20).g(c[d].name), "#fff"), "left"), "futuraBold").b(120, 20).a(100, d * 20);
                scoresText.appendChild(e);
                e = M(L(af(K(new N, 20).g(c[d].total_score), "left"), "#fff"), "futuraBold").b(120, 20).a(280, d * 20);
                scoresText.appendChild(e)
            }
            b.appendChild(scoresText);
            scoresPopup.appendChild(b);
            return scoresPopup
        }
    };
    s(Wf, Ja);
    function Xf(a) {
        if (typeof DOMParser != "undefined")
            return (new DOMParser).parseFromString(a, "application/xml");
        else if (typeof ActiveXObject != "undefined") {
            var b = new ActiveXObject("MSXML2.DOMDocument");
            if (b) {
                b.resolveExternals = !1;
                b.validateOnParse = !1;
                try {
                    b.setProperty("ProhibitDTD", !0),
                    b.setProperty("MaxXMLSize", 2048),
                    b.setProperty("MaxElementDepth", 256)
                } catch (c) {}
            }
            b.loadXML(a);
            return b
        }
        throw Error("Your browser does not support loading xml documents");
    }
    ;var Yf = function() {
        function a(a) {
            for (var d = {}, e = b(a, "key"), a = 0; a < e.length; a++) {
                var g;
                if (e[a].nextElementSibling != i)
                    g = e[a].nextElementSibling;
                else
                    for (g = e[a].nextSibling; g && g.nodeType != 1; )
                        g = g.nextSibling;
                d[e[a].firstChild.nodeValue] = g
            }
            return d
        }
        function b(a, b) {
            var e, g = [];
            for (e = 0; e < a.childNodes.length; e++)
                a.childNodes[e].nodeName == b && g.push(a.childNodes[e]);
            return g
        }
        return function(c) {
            var d = {}, c = Xf(c), c = b(b(c, "plist")[1], "dict")[0], c = a(c), c = a(c.frames), e;
            for (e in c) {
                var g = a(c[e]);
                g.fb = function(a) {
                    return parseFloat(g[a].firstChild.nodeValue)
                }
                ;
                var h = g.fb("originalWidth")
                  , m = g.fb("originalHeight")
                  , l = g.fb("width")
                  , q = g.fb("height");
                d[e] = [new Lc(g.fb("x"),g.fb("y"),l,q), new pb((h - l) / 2 + g.fb("offsetX"),(m - q) / 2 + g.fb("offsetY")), new Da(h,m), !1]
            }
            return d
        }
    }();
    function Zf(a, b, c, d, e) {
        Ef.call(this, a);
        ka(b) && (b = new Lc(b,c,d,e),
        c = new pb(0,0),
        d = new Da(b.width,b.height),
        e = !1);
        this.rf = b;
        this.Nb = c;
        this.Ya = d;
        this.Fg = e;
        a = this.rf;
        a = [this.na, a.width, a.height, a.left, a.top, this.Nb.x, this.Nb.y].join("_");
        p(this.wd[a]) ? (this.M = this.wd[a],
        this.M.be || w(this.M.Rc, "processed", function() {
            this.dispatchEvent(new Yb("processed"))
        }, !1, this)) : (this.M = {},
        this.M.be = !1,
        this.M.Rc = this,
        this.M.Mb = this.Tf(),
        this.wd[a] = this.M,
        this.Ff = this.md ? document.getCSSCanvasContext("2d", this.M.Mb, this.Ya.width, this.Ya.height) : $f(this),
        this.Tb() ? this.cf() : w(this, "load", this.cf, !1, this))
    }
    s(Zf, Ef);
    Zf.prototype.id = "frame";
    Zf.prototype.wd = {};
    Zf.prototype.md = la(document.getCSSCanvasContext);
    Zf.prototype.vc = function(a) {
        var b = a.t();
        b.width == 0 && b.height == 0 && a.b(this.Ya.width, this.Ya.height);
        Ef.prototype.vc.call(this, a);
        this.M && this.M.be || w(this, "processed", function() {
            z(a, 4)
        }, !1, this)
    }
    ;
    (function() {
        var a = "cvsbg_" + Math.round(Math.random() * 1E3) + "_", b = 0, c;
        Zf.prototype.Tf = function() {
            b++;
            return a + b
        }
        ;
        Zf.prototype.cf = function() {
            ag(this, this.Ff);
            if (!this.md) {
                var a = this.Ob.toDataURL("image/png")
                  , b = "." + this.M.Mb + "{background-image:url(" + a + ") !important}";
                if (c)
                    if (Ab)
                        c.cssText += b;
                    else {
                        var g = c
                          , h = i;
                        if (h < 0 || h == i)
                            h = (g.rules || g.cssRules).length;
                        if (g.insertRule)
                            g.insertRule(b, h);
                        else if (b = /^([^\{]+)\{([^\{]+)\}/.exec(b),
                        b.length == 3)
                            g.addRule(b[1], b[2], h);
                        else
                            throw Error("Your CSSRule appears to be ill-formatted.");
                    }
                else
                    sd(b),
                    c = document.styleSheets[document.styleSheets.length - 1];
                this.M.bg = ad("img");
                this.M.bg.src = a
            }
            this.M.be = !0;
            this.dispatchEvent(new Yb("processed"))
        }
    }
    )();
    Zf.prototype.Qe = function() {
        if (!this.tc)
            this.M.Rc && this.M.Rc.tc ? this.tc = this.M.Rc.tc : (this.Ob || ag(this, $f(this)),
            this.tc = this.Ob);
        return this.tc
    }
    ;
    function $f(a) {
        a.Ob = ad("canvas");
        var b = a.Ob.getContext("2d");
        a.Ob.width = a.Ya.width;
        a.Ob.height = a.Ya.height;
        return b
    }
    function ag(a, b) {
        var c = a.rf, d = c.width, e = c.height, g = c.left, c = c.top, h, m;
        g < 0 && (d += g,
        g = 0);
        c < 0 && (e += c,
        c = 0);
        d + g > a.J.width && (d = a.J.width - g);
        e + c > a.J.height && (e = a.J.height - c);
        a.Fg ? (b.rotate(-Math.PI * 0.5),
        b.translate(-a.Ya.height, 0),
        h = a.Ya.height - a.Nb.y - d,
        m = a.Nb.x) : (h = a.Nb.x,
        m = a.Nb.y);
        b.drawImage(a.J, g, c, d, e, h, m, d, e)
    }
    Zf.prototype.Eb = function(a, b) {
        if (this.md)
            a.style.background = "-webkit-canvas(" + this.M.Mb + ")";
        else if (this.M.Mb != b.vd)
            Qc(a, this.M.Mb),
            a.style.background = "",
            b.vd && Rc(a, b.vd),
            b.vd = this.M.Mb;
        Kf(this, a, b)
    }
    ;
    function bg(a, b, c) {
        this.J = new Ef(a);
        this.qg = (c || Yf)(b.data())
    }
    bg.prototype.m = function(a) {
        var b = this.qg[a];
        if (!b)
            throw "Frame " + a + " not found in the spritesheet";
        return new Zf(this.J.J,b[0],b[1],b[2],b[3])
    }
    ;
    var cg = {
        data: ba('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>frames</key><dict><key>helpExpert.png</key><dict><key>x</key><real>1075</real><key>y</key><real>95</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>helpJunior.png</key><dict><key>x</key><real>571</real><key>y</key><real>842</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>helpMaster.png</key><dict><key>x</key><real>252</real><key>y</key><real>462</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>helpStarter.png</key><dict><key>x</key><real>1394</real><key>y</key><real>190</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>moreExpert.png</key><dict><key>x</key><real>252</real><key>y</key><real>557</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>moreJunior.png</key><dict><key>x</key><real>571</real><key>y</key><real>747</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>moreMaster.png</key><dict><key>x</key><real>823</real><key>y</key><real>285</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>moreStarter.png</key><dict><key>x</key><real>0</real><key>y</key><real>816</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>scoresExpert.png</key><dict><key>x</key><real>252</real><key>y</key><real>367</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>scoresJunior.png</key><dict><key>x</key><real>252</real><key>y</key><real>652</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>scoresMaster.png</key><dict><key>x</key><real>1075</real><key>y</key><real>0</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>scoresStarter.png</key><dict><key>x</key><real>823</real><key>y</key><real>190</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>settingsExpert.png</key><dict><key>x</key><real>504</real><key>y</key><real>0</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>settingsJunior.png</key><dict><key>x</key><real>0</real><key>y</key><real>911</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>settingsMaster.png</key><dict><key>x</key><real>252</real><key>y</key><real>272</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>settingsStarter.png</key><dict><key>x</key><real>504</real><key>y</key><real>95</real><key>width</key><real>569</real><key>height</key><real>93</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>569</real><key>originalHeight</key><real>93</real></dict><key>sglExpert.png</key><dict><key>x</key><real>0</real><key>y</key><real>0</real><key>width</key><real>250</real><key>height</key><real>270</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>270</real></dict><key>sglJunior.png</key><dict><key>x</key><real>0</real><key>y</key><real>544</real><key>width</key><real>250</real><key>height</key><real>270</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>270</real></dict><key>sglMaster.png</key><dict><key>x</key><real>252</real><key>y</key><real>0</real><key>width</key><real>250</real><key>height</key><real>270</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>270</real></dict><key>sglStarter.png</key><dict><key>x</key><real>0</real><key>y</key><real>272</real><key>width</key><real>250</real><key>height</key><real>270</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>270</real></dict></dict><key>texture</key><dict><key>width</key><integer>2048</integer><key>height</key><integer>1024</integer></dict></dict></plist>')
    };
    var dg = {
        data: ba('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>frames</key><dict><key>levelIndicatorArrow.png</key><dict><key>x</key><real>456</real><key>y</key><real>0</real><key>width</key><real>22</real><key>height</key><real>84</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>22</real><key>originalHeight</key><real>84</real></dict><key>levelIndicatorExpert.png</key><dict><key>x</key><real>0</real><key>y</key><real>0</real><key>width</key><real>150</real><key>height</key><real>92</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>150</real><key>originalHeight</key><real>92</real></dict><key>levelIndicatorJunior.png</key><dict><key>x</key><real>304</real><key>y</key><real>0</real><key>width</key><real>150</real><key>height</key><real>92</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>150</real><key>originalHeight</key><real>92</real></dict><key>levelIndicatorMaster.png</key><dict><key>x</key><real>0</real><key>y</key><real>94</real><key>width</key><real>150</real><key>height</key><real>92</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>150</real><key>originalHeight</key><real>92</real></dict><key>levelIndicatorStarter.png</key><dict><key>x</key><real>152</real><key>y</key><real>0</real><key>width</key><real>150</real><key>height</key><real>92</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>150</real><key>originalHeight</key><real>92</real></dict></dict><key>texture</key><dict><key>width</key><integer>512</integer><key>height</key><integer>256</integer></dict></dict></plist>')
    };
    var eg = {
        data: ba('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>frames</key><dict><key>btnHomeScreenExpert.png</key><dict><key>x</key><real>456</real><key>y</key><real>362</real><key>width</key><real>281</real><key>height</key><real>72</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>281</real><key>originalHeight</key><real>72</real></dict><key>btnHomeScreenJunior.png</key><dict><key>x</key><real>739</real><key>y</key><real>436</real><key>width</key><real>281</real><key>height</key><real>72</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>281</real><key>originalHeight</key><real>72</real></dict><key>btnHomeScreenMaster.png</key><dict><key>x</key><real>739</real><key>y</key><real>362</real><key>width</key><real>281</real><key>height</key><real>72</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>281</real><key>originalHeight</key><real>72</real></dict><key>btnHomeScreenStarter.png</key><dict><key>x</key><real>456</real><key>y</key><real>436</real><key>width</key><real>281</real><key>height</key><real>72</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>281</real><key>originalHeight</key><real>72</real></dict><key>levelSelectIndicatorArrow.png</key><dict><key>x</key><real>0</real><key>y</key><real>0</real><key>width</key><real>454</real><key>height</key><real>455</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>454</real><key>originalHeight</key><real>455</real></dict><key>levelUnlockedIcon.png</key><dict><key>x</key><real>0</real><key>y</key><real>457</real><key>width</key><real>44</real><key>height</key><real>50</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>44</real><key>originalHeight</key><real>50</real></dict><key>selectLevelCircle.png</key><dict><key>x</key><real>456</real><key>y</key><real>0</real><key>width</key><real>360</real><key>height</key><real>360</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>360</real><key>originalHeight</key><real>360</real></dict></dict><key>texture</key><dict><key>width</key><integer>1024</integer><key>height</key><integer>512</integer></dict></dict></plist>')
    };
    var ig = {
        og: function(a, b) {
            var c = localStorage.getItem("av.numStars");
            Ie = new bg(sglSpriteImgs[1],eg);
            var d = (new H).a(0, -500).b(960, 600).d(0, 0);
            levelRotation = -75;
            btnHomeScreenStarter = (new H).b(281, 72).d(0.5, 0.5).a(480, 330);
            btnHomeScreenStarterImage = (new P).d(0.5, 0.5).b(281, 72).a(0, 0).c(Ie.m("btnHomeScreenStarter.png"));
            btnHomeScreenStarter.appendChild(btnHomeScreenStarterImage);
            btnHomeScreenStarter.K = "Starter";
            levelUnlockedIcon = (new P).c(Ie.m("levelUnlockedIcon.png")).b(35, 39).a(-93, 0).d(0.5, 0.5);
            btnHomeScreenStarter.appendChild(levelUnlockedIcon);
            w(btnHomeScreenStarter, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                Uf(btnHomeScreenStarter, Q.uc))
            });
            d.appendChild(btnHomeScreenStarter);
            btnHomeScreenJunior = (new H).b(281, 72).d(0.5, 0.5).a(480, 240);
            btnHomeScreenJuniorImage = (new P).d(0.5, 0.5).b(281, 72).a(0, 0).c(Ie.m("btnHomeScreenJunior.png"));
            btnHomeScreenJunior.appendChild(btnHomeScreenJuniorImage);
            btnHomeScreenJunior.K = "Junior";
            Je >= b[1] && (levelRotation = -105);
            levelUnlockedIcon = (new P).c(Ie.m("levelUnlockedIcon.png")).b(35, 39).a(-93, 0).d(0.5, 0.5);
            btnHomeScreenJunior.appendChild(levelUnlockedIcon);
            c != k && c != 0 ? w(btnHomeScreenJunior, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                Uf(btnHomeScreenJunior, Q.uc))
            }) : (D(btnHomeScreenJuniorImage, 0.25),
            D(levelUnlockedIcon, 0.25));
            d.appendChild(btnHomeScreenJunior);
            btnHomeScreenExpert = (new H).b(281, 72).d(0.5, 0.5).a(480, 240);
            btnHomeScreenExpertImage = (new P).d(0.5, 0.5).b(281, 72).a(0, 0).c(Ie.m("btnHomeScreenExpert.png"));
            btnHomeScreenExpert.appendChild(btnHomeScreenExpertImage);
            btnHomeScreenExpert.K = "Expert";
            Je >= b[2] && (levelRotation = -255);
            levelUnlockedIcon = (new P).c(Ie.m("levelUnlockedIcon.png")).b(35, 39).a(-47, 0).d(0.5, 0.5);
            btnHomeScreenExpert.appendChild(levelUnlockedIcon);
            c != k && c != 0 ? w(btnHomeScreenExpert, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                Uf(btnHomeScreenExpert, Q.uc))
            }) : (D(btnHomeScreenExpertImage, 0.25),
            D(levelUnlockedIcon, 0.25));
            d.appendChild(btnHomeScreenExpert);
            btnHomeScreenMaster = D((new H).b(281, 72).d(0.5, 0.5).a(480, 330), 0);
            btnHomeScreenMasterImage = (new P).d(0.5, 0.5).b(281, 72).a(0, 0).c(Ie.m("btnHomeScreenMaster.png"));
            btnHomeScreenMaster.appendChild(btnHomeScreenMasterImage);
            btnHomeScreenMaster.K = "Master";
            Je >= b[3] && (levelRotation = -285);
            levelUnlockedIcon = (new P).c(Ie.m("levelUnlockedIcon.png")).b(35, 39).a(-47, 0).d(0.5, 0.5);
            btnHomeScreenMaster.appendChild(levelUnlockedIcon);
            c != k && c != 0 ? w(btnHomeScreenMaster, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                Uf(btnHomeScreenMaster, Q.uc))
            }) : (D(btnHomeScreenMasterImage, 0.25),
            D(levelUnlockedIcon, 0.25));
            d.appendChild(btnHomeScreenMaster);
            selectLevelCircle = (new P).d(0.5, 0.5).b(330, 330).a(480, 280).c(Ie.m("selectLevelCircle.png"));
            d.appendChild(selectLevelCircle);
            levelSelectIndicatorArrow = (new P).d(0.5, 0.5).b(335, 335).a(478, 278).c(Ie.m("levelSelectIndicatorArrow.png"));
            d.appendChild(levelSelectIndicatorArrow);
            return d
        },
        lg: function(a, b) {
            Ke = new bg(sglSpriteImgs[1],cg);
            var c = (new H).a(0, -500).b(960, 600).d(0, 0);
            btnHomeScreenStarter = (new H).b(281, 72).d(0.5, 0.5).a(480, 290).l(0.5, 1);
            btnHomeScreenStarterImage = (new P).d(0.5, 0.5).b(441, 72).a(0, 0).c(Ke.m("scores" + b + ".png"));
            btnHomeScreenStarter.appendChild(btnHomeScreenStarterImage);
            btnHomeScreenStarter.K = "Starter";
            var d = M(D(L(K(new N, 34).g(I.scores).a(-154, -19), "#505354"), 0.7), "futuraBold").d(0, 0)
              , e = M(L(K(new N, 34).g(I.scores).a(-155, -21), "#fff"), "futuraBold").d(0, 0);
            btnHomeScreenStarter.appendChild(d);
            btnHomeScreenStarter.appendChild(e);
            w(btnHomeScreenStarter, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                fg(btnHomeScreenStarter, Q.Oc))
            });
            c.appendChild(btnHomeScreenStarter);
            btnHomeScreenJunior = (new H).b(281, 72).d(0.5, 0.5).a(480, 210).l(0.5, 1);
            btnHomeScreenJuniorImage = (new P).d(0.5, 0.5).b(441, 72).a(0, 0).c(Ke.m("settings" + b + ".png"));
            btnHomeScreenJunior.appendChild(btnHomeScreenJuniorImage);
            btnHomeScreenJunior.K = "Junior";
            d = M(D(L(K(new N, 34).g(I.settings).a(-154, -19), "#505354"), 0.7), "futuraBold").d(0, 0);
            e = M(L(K(new N, 34).g(I.settings).a(-155, -21), "#fff"), "futuraBold").d(0, 0);
            btnHomeScreenJunior.appendChild(d);
            btnHomeScreenJunior.appendChild(e);
            w(btnHomeScreenJunior, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                fg(btnHomeScreenJunior, Q.Hd))
            });
            c.appendChild(btnHomeScreenJunior);
            btnHomeScreenExpert = (new H).b(281, 72).d(0.5, 0.5).a(480, 210).l(0.5, 1);
            btnHomeScreenExpertImage = (new P).d(0.5, 0.5).b(441, 72).a(0, 0).c(Ke.m("help" + b + ".png"));
            btnHomeScreenExpert.appendChild(btnHomeScreenExpertImage);
            btnHomeScreenExpert.K = "Expert";
            d = M(D(L(K(new N, 34).g(I.help).a(-45, -19), "#505354").b(215, 25), 0.7), "futuraBold").d(0, 0);
            e = M(L(K(new N, 34).g(I.help).a(-44, -21), "#fff").b(215, 25), "futuraBold").d(0, 0);
            btnHomeScreenExpert.appendChild(d);
            btnHomeScreenExpert.appendChild(e);
            w(btnHomeScreenExpert, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (Q.n.reload(),
                Q.n.play(),
                Uf(btnHomeScreenExpert, Q.Vf))
            });
            c.appendChild(btnHomeScreenExpert);
            btnHomeScreenMaster = D((new H).b(281, 72).d(0.5, 0.5).a(480, 290), 0).l(0.5, 1);
            btnHomeScreenMasterImage = (new P).d(0.5, 0.5).b(441, 72).a(0, 0).c(Ke.m("more" + b + ".png"));
            btnHomeScreenMaster.appendChild(btnHomeScreenMasterImage);
            btnHomeScreenMaster.K = "Master";
            d = M(D(L(K(new N, 34).g(I.more).a(-59, -19), "#505354").b(215, 25), 0.7), "futuraBold").d(0, 0);
            e = M(L(K(new N, 34).g(I.more).a(-60, -21), "#fff").b(215, 25), "futuraBold").d(0, 0);
            btnHomeScreenMaster.appendChild(d);
            btnHomeScreenMaster.appendChild(e);
            w(btnHomeScreenMaster, ["mousedown", "touchstart"], function() {
                if (settingsPopupShowed == !1) {
                    Q.n.reload();
                    Q.n.play();
                    var a = (new U(1.25)).e(0.05);
                    G(btnHomeScreenMaster, a);
                    w(a, T, function() {
                        var a = (new U(1)).e(0.15);
                        G(btnHomeScreenMaster, a);
                        w(a, T, function() {
                            window.goToMoreGames(b)
                        })
                    })
                }
            });
            c.appendChild(btnHomeScreenMaster);
            selectLevelCircle = (new P).d(0.5, 0.5).a(480, 265).l(1.1).b(245, 290);
            c.appendChild(selectLevelCircle);
            d = (new P).d(0.5, 0.5).a(0, -2).c(J + "logo.png");
            selectLevelCircle.appendChild(d);
            d = (new P).d(0.5, 0.5).a(0, 0).c(Ke.m("sgl" + b + ".png")).l(1.1);
            selectLevelCircle.appendChild(d);
            selectLevelCircle.K = b;
            w(selectLevelCircle, ["mousedown", "touchstart"], function() {
                settingsPopupShowed == !1 && (settingsPopupShowed = !0,
                Q.n.reload(),
                Q.n.play(),
                Uf(selectLevelCircle, Q.uc))
            });
            levelBtnLayer = D(new H, 0);
            c.appendChild(levelBtnLayer);
            return c
        },
        mg: function(a, b, c, d, e) {
            Le = new bg(sglSpriteImgs[0],dg);
            a = (new H).a(d, e).d(0, 0);
            levelIndicatorImage = (new P).c(Le.m("levelIndicator" + b + ".png")).b(150, 93).a(0, 0);
            a.appendChild(levelIndicatorImage);
            levelIndicatorArrow = (new P).c(Le.m("levelIndicatorArrow.png")).b(22, 84).a(28, -2);
            a.appendChild(levelIndicatorArrow);
            levelIndicatorArrow.h = new Sf((new V(1)).e(1),(new gg(hg())).e(0.5));
            G(levelIndicatorArrow, levelIndicatorArrow.h);
            lbl = M(L(K(new N, 22).g(c).a(-38, 1), "#fff").b(45, 25), "futuraBold");
            a.appendChild(lbl);
            return a
        }
    };
    function hg() {
        numlevelsDifficultyStarter = Vf(jg.Starter);
        numlevelsDifficultyJunior = Vf(jg.Junior);
        numlevelsDifficultyExpert = Vf(jg.Expert);
        numlevelsDifficultyMaster = Vf(jg.Master);
        var a = 0
          , b = F.Xa
          , c = numlevelsDifficultyStarter;
        F.K == "Junior" ? (c = numlevelsDifficultyJunior,
        a = 90) : F.K == "Expert" ? (c = numlevelsDifficultyExpert,
        a = 180) : F.K == "Master" && (c = numlevelsDifficultyMaster,
        a = 270);
        completedPercentage = b / c;
        rotation = completedPercentage * 90 + a;
        return -rotation
    }
    s(ig, Ja);
    ig.ng = function() {
        var a = Me;
        F.Ic = 0;
        O.Db(chrono = function() {
            F.Yg()
        }
        , F, 1E3, 0);
        var b = (new H).a(-35, 10).d(0, 0)
          , c = (new P).c(a + "timeIndicator.png").a(140, 45);
        b.appendChild(c);
        F.hd = M(L(K(new N, 22).g("00:00").a(130, 44), "#0E384C").b(45, 25), "futura");
        b.appendChild(F.hd);
        var c = (new H).a(137, 81)
          , d = kg(F.Xa, F.K);
        if (lg(d.stars))
            if (d.stars == 1)
                var e = (new P).c(a + "star.png").a(-33, 0)
                  , g = (new P).c(a + "emptyStar.png").a(0, 0)
                  , h = (new P).c(a + "emptyStar.png").a(33, 0);
            else
                d.stars == 2 ? (e = (new P).c(a + "star.png").a(-33, 0),
                g = (new P).c(a + "star.png").a(0, 0),
                h = (new P).c(a + "emptyStar.png").a(33, 0)) : d.stars == 3 && (e = (new P).c(a + "star.png").a(-33, 0),
                g = (new P).c(a + "star.png").a(0, 0),
                h = (new P).c(a + "star.png").a(33, 0));
        else
            e = (new P).c(a + "emptyStar.png").a(-33, 0),
            g = (new P).c(a + "emptyStar.png").a(0, 0),
            h = (new P).c(a + "emptyStar.png").a(33, 0);
        c.appendChild(e);
        c.appendChild(g);
        c.appendChild(h);
        b.appendChild(c);
        return b
    }
    ;
    F.Yg = function() {
        if (F.P.f.y == 0) {
            F.Ic += 1;
            var a = F.Ic % 60
              , b = (F.Ic - a) / 60;
            b < 10 && (b = "0" + b);
            a < 10 && (a = "0" + a);
            F.hd.g(b + ":" + a)
        }
    }
    ;
    function mg() {
        kf.call(this)
    }
    s(mg, kf);
    mg.prototype.update = fa;
    function Sf(a) {
        kf.call(this);
        var b = mb(arguments);
        ha(a) && (b = a);
        this.C = b.length > 2 ? [b.shift(), new Sf(b)] : b;
        this.e(this.C[0].z + this.C[1].z)
    }
    s(Sf, kf);
    Sf.prototype.zb = function(a) {
        kf.prototype.zb.call(this, a);
        this.e(this.C[0].z + this.C[1].z);
        this.ac = this.C[0].z / this.z;
        this.Sa = -1
    }
    ;
    Sf.prototype.stop = function() {
        this.Sa && this.Sa != -1 && this.C[this.Sa].stop(this.Fb);
        kf.prototype.stop.apply(this, arguments)
    }
    ;
    Sf.prototype.nb = function(a, b) {
        if (this.$ == 0)
            return a;
        for (var c = b.length; --c >= 0; )
            of(this, b[c]);
        var d = c = 0;
        a >= this.ac ? (c = 1,
        d = this.ac == 1 ? 1 : (a - this.ac) / (1 - this.ac)) : (c = 0,
        d = this.ac != 0 ? a / this.ac : 1);
        if (this.Sa == -1 && c == 1)
            this.C[0].$ = 1,
            this.C[0].nb(1, b),
            this.C[0].stop();
        if (this.Sa != c)
            this.Sa != -1 && (this.C[this.Sa].nb(1, b),
            this.C[this.Sa].stop()),
            this.C[c].$ = 1;
        this.C[c].nb(d, b);
        this.Sa = c;
        return a
    }
    ;
    function ng(a) {
        kf.call(this);
        var b = mb(arguments);
        ha(a) && (b = a);
        b.length > 2 ? (this.Ub = b.shift(),
        this.cc = new ng(b)) : (this.Ub = b[0],
        this.cc = b[1]);
        var b = this.Ub.z
          , c = this.cc.z;
        this.e(Math.max(b, c));
        var d = new mg;
        if (b > c)
            this.cc = new Sf(this.cc,d.e(b - c));
        else if (b < c)
            this.Ub = new Sf(this.Ub,d.e(c - b))
    }
    s(ng, kf);
    ng.prototype.zb = function(a) {
        kf.prototype.zb.call(this, a);
        this.Ub.$ = 1;
        this.cc.$ = 1
    }
    ;
    ng.prototype.nb = function(a, b) {
        if (this.$ != 0) {
            for (var c = b.length; --c >= 0; )
                of(this, b[c]);
            this.Ub.nb(a, b);
            this.cc.nb(a, b);
            return a
        }
    }
    ;
    function og(a) {
        kf.call(this);
        this.jc = a
    }
    s(og, kf);
    og.prototype.scope = "rotate";
    og.prototype.Bb = function(a) {
        if (nf(this)) {
            var b = Oa(a) + this.jc;
            a.Ba[Na] = [b, this.z, this.bb, 0];
            z(a, Jd)
        }
        return {
            fe: Oa(a)
        }
    }
    ;
    og.prototype.update = function(a, b) {
        if (this.$ != 0) {
            var c = of(this, b);
            Nd(b, c.fe + this.jc * a)
        }
    }
    ;
    og.prototype.ga = function(a) {
        nf(this) && (a.ga(Na),
        z(a, Jd))
    }
    ;
    function Tf(a) {
        kf.call(this);
        this.hc = a;
        w(a, T, this.Wf, !1, this);
        this.wa = this.ge = this.ge = this.Ze = 0;
        this.e(a.z)
    }
    s(Tf, kf);
    n = Tf.prototype;
    n.zb = function(a) {
        kf.prototype.zb.call(this, a);
        this.e(this.hc.z)
    }
    ;
    n.play = function() {
        this.hc.play();
        this.wa = 1;
        this.dispatchEvent({
            type: "start"
        })
    }
    ;
    n.stop = function() {
        this.wa = 0;
        this.hc.stop();
        this.dispatchEvent({
            type: T
        })
    }
    ;
    n.Wf = function() {
        this.ge++;
        this.wa && (!this.Ze || this.ge < this.Ze) ? this.hc.play() : this.stop()
    }
    ;
    n.qb = function(a) {
        this.hc.qb(a);
        return this
    }
    ;
    function U(a, b) {
        kf.call(this);
        this.T = arguments.length == 1 && ka(a) ? new pb(a,a) : arguments.length == 2 ? new pb(arguments[0],arguments[1]) : a
    }
    s(U, kf);
    U.prototype.scope = "scale";
    U.prototype.Bb = function(a) {
        var b = a.T
          , c = new pb(this.T.x - b.x,this.T.y - b.y);
        nf(this) && (a.Ba[Ka] = [new pb(b.x + c.x,b.y + c.y), this.z, this.bb, 0],
        z(a, 2));
        return {
            xf: b,
            V: c
        }
    }
    ;
    U.prototype.update = function(a, b) {
        if (this.$ != 0) {
            var c = of(this, b);
            b.l(c.xf.x + c.V.x * a, c.xf.y + c.V.y * a)
        }
    }
    ;
    U.prototype.ga = function(a) {
        nf(this) && (a.ga(Ka),
        z(a, 2))
    }
    ;
    function V(a) {
        kf.call(this);
        this.ca = a
    }
    s(V, kf);
    V.prototype.scope = "fade";
    V.prototype.Bb = function(a) {
        var b = a.ca;
        nf(this) && (a.Ba[Ed] = [this.ca, this.z, this.bb, 0],
        z(a, Fd));
        return {
            Lg: b,
            V: this.ca - b
        }
    }
    ;
    V.prototype.update = function(a, b) {
        if (this.$ != 0) {
            var c = of(this, b);
            D(b, c.Lg + c.V * a)
        }
    }
    ;
    V.prototype.ga = function(a) {
        nf(this) && (a.ga(Ed),
        z(a, Fd))
    }
    ;
    function gg(a) {
        kf.call(this);
        this.jc = a
    }
    s(gg, kf);
    gg.prototype.scope = "rotate";
    gg.prototype.Bb = function(a) {
        var b = Oa(a);
        nf(this) && (a.Ba[Na] = [this.jc, this.z, this.bb, 0],
        z(a, Jd));
        return {
            fe: b,
            V: this.jc - b
        }
    }
    ;
    gg.prototype.update = function(a, b) {
        if (this.$ != 0) {
            var c = of(this, b);
            Nd(b, c.fe + c.V * a)
        }
    }
    ;
    gg.prototype.ga = function(a) {
        nf(this) && (a.ga(Na),
        z(a, Jd))
    }
    ;
    function pg(a, b) {
        H.call(this);
        this.qc = "lime-button";
        if (p(a))
            this.ma = a,
            this.appendChild(this.ma),
            this.Hc = -1,
            qg(this, rg);
        p(b) && sg(this, b);
        var c = this;
        w(this, ["mousedown", "touchstart", "touchmove"], function(a) {
            qg(c, tg);
            a.w("mousemove", function(a) {
                c.i(a) ? qg(c, tg) : qg(c, rg)
            });
            a.w("touchmove", function(a) {
                c.i(a) || (qg(c, rg),
                a.Bc())
            });
            a.w(["mouseup", "touchend"], function(a) {
                c.i(a) && c.dispatchEvent({
                    type: ug
                });
                qg(this, rg)
            })
        })
    }
    s(pg, H);
    var rg = 0
      , tg = 1
      , ug = "click";
    function sg(a, b) {
        a.Pa = b;
        a.appendChild(b);
        a.Hc = -1;
        qg(a, rg)
    }
    function qg(a, b) {
        if (b != a.Hc) {
            a.Hc == rg && b == tg && a.dispatchEvent({
                type: "down"
            });
            a.Hc == tg && b == rg && a.dispatchEvent({
                type: "up"
            });
            var c = a.ma;
            if (p(a.Pa))
                tg == b ? c = a.Pa : B(a.Pa, !0);
            c != a.ma && B(a.ma, !0);
            B(c, !1);
            a.Hc = b
        }
    }
    ;u.gc = {};
    v.gc = {};
    function Xe() {
        P.call(this);
        vg(this, 5)
    }
    s(Xe, P);
    Xe.prototype.id = "roundedrect";
    Xe.prototype.Va = [Ha(v.O, v.gc), Ha(u.O, u.gc)];
    function vg(a, b) {
        a.yh = !1;
        a.ce = b;
        return a
    }
    v.gc.R = function(a) {
        this.t();
        v.O.R.call(this, a);
        Bd(a, [this.ce * this.Wb, this.ce * this.Wb])
    }
    ;
    u.gc.R = function(a) {
        this.t();
        var b = this.m()
          , c = this.ce
          , d = b.left
          , e = b.top
          , g = b.right - b.left
          , b = b.bottom - b.top;
        a.save();
        a.beginPath();
        a.moveTo(d + c, e);
        a.lineTo(d + g - c, e);
        a.quadraticCurveTo(d + g, e, d + g, e + c);
        a.lineTo(d + g, e + b - c);
        a.quadraticCurveTo(d + g, e + b, d + g - c, e + b);
        a.lineTo(d + c, e + b);
        a.quadraticCurveTo(d, e + b, d, e + b - c);
        a.lineTo(d, e + c);
        a.quadraticCurveTo(d, e, d + c, e);
        a.closePath();
        a.clip();
        u.O.R.call(this, a);
        this.ea && (a.lineWidth *= 2,
        a.stroke());
        a.restore()
    }
    ;
    u.fc = {};
    v.fc = {};
    function N(a) {
        P.call(this);
        this.Wd = !1;
        z(this, 4);
        this.g(a);
        M(this, wg);
        K(this, 14);
        L(this, "#000");
        af(this, "center");
        this.Oe = "400";
        z(this, 8);
        a = [0, 0, 0, 0];
        p(i) && (a[1] = a[3] = i);
        p(i) && (a[2] = i);
        p(i) && (a[3] = i);
        this.ia = a;
        z(this, 8);
        this.eg = !1;
        this.$e = 1.15;
        this.B(k);
        this.c(255, 255, 255, 0)
    }
    s(N, P);
    N.prototype.id = "label";
    var wg = "Arial";
    N.prototype.Va = [Ha(v.O, v.fc), Ha(u.O, u.fc)];
    (function() {
        var a;
        N.prototype.measureText = function() {
            p(a) || (a = document.createElement("canvas").getContext("2d"));
            var b = xg(this) * this.wb;
            this.Wd && (b *= Ta(this.Ka).split("\n").length);
            a.font = this.wb + "px " + this.Dd;
            var c = a.measureText(this.Ka)
              , c = Cb ? c.width : c.width + 1;
            Gc && (c += 1);
            var d = this.ea ? this.ea.Wa : 0;
            return new Da(this.ia[1] + this.ia[3] + c + d * 2,this.ia[0] + this.ia[2] + b + d * 2)
        }
    }
    )();
    n = N.prototype;
    n.t = function() {
        var a = Dd.prototype.t.call(this);
        return !a || !a.width && !a.height ? this.measureText() : a
    }
    ;
    n.g = function(a) {
        this.Ka = a + "";
        z(this, 4);
        delete this.ke;
        return this
    }
    ;
    function M(a, b) {
        a.Dd = b;
        z(a, 8);
        return a
    }
    function K(a, b) {
        a.wb = b;
        z(a, 8);
        return a
    }
    function L(a, b) {
        a.Ne = b;
        z(a, 8);
        return a
    }
    function xg(a) {
        var b = Math.abs(a.ta.y) + a.ya * 2;
        return a.eg ? (a.$e + b) / a.wb : a.$e + b / a.wb
    }
    function af(a, b) {
        a.qe = b;
        z(a, 8);
        return a
    }
    n.B = function(a, b, c, d) {
        arguments.length == 1 && a === k ? (this.Ec = "#ccc",
        this.ya = 0,
        this.ed(0, 0)) : arguments.length == 2 ? (this.Ec = a,
        this.ya = b,
        this.ed(new pb(0,0))) : arguments.length == 3 ? (this.Ec = a,
        this.ya = b,
        this.ed(c)) : (this.Ec = a,
        this.ya = b,
        this.ed(c, d));
        z(this, 8);
        return this
    }
    ;
    n.ed = function(a, b) {
        this.ta = arguments.length == 2 ? new pb(arguments[0],arguments[1]) : a;
        z(this, 8)
    }
    ;
    n.update = function() {
        this.aa & 4 && delete this.Xe;
        Dd.prototype.update.apply(this, arguments)
    }
    ;
    v.fc.R = function(a) {
        v.O.R.call(this, a);
        var b = a.style;
        if (this.aa & 4)
            this.Wd ? a.innerHTML = Ua(this.Ka).replace(/\n/g, "<br/>") : jd(a, this.Ka);
        if (this.aa & 8)
            b.lineHeight = xg(this),
            b.padding = hb(this.ia, function(a) {
                return a * Xd(this)
            }, this).join("px ") + "px",
            b.color = this.Ne,
            b.fontFamily = this.Dd,
            b.fontSize = this.wb * Xd(this) + "px",
            b.fontWeight = this.Oe,
            b.textAlign = this.qe,
            b.textShadow = this.ya || this.ta.x || this.ta.y ? this.Ec + " " + this.ta.x + "px " + this.ta.y + "px " + this.ya + "px" : ""
    }
    ;
    u.fc.R = function(a) {
        u.O.R.call(this, a);
        var b = this.m()
          , c = -b.left - this.ia[3] + b.right - this.ia[1] + Math.abs(this.ta.x) + Math.abs(this.ya * 2)
          , d = 0;
        if (!this.ke) {
            var d = []
              , e = this.Ka.length
              , g = this.Ka.match(Bb ? /[\s\.]+/g : /[\s-\.]+/g)
              , h = 0;
            if (g)
                for (var m = 0; m < g.length; m++) {
                    var l = g[m]
                      , l = this.Ka.indexOf(l, h) + l.length;
                    d.push(this.Ka.substring(h, l));
                    h = l
                }
            h != e && d.push(this.Ka.substring(h, e));
            this.ke = d;
            d = 1
        }
        g = this.ea ? this.ea.Wa : 0;
        a.save();
        e = this.qe;
        e == "left" ? a.translate(b.left + this.ia[3] + g, b.top + this.ia[0] + g) : e == "right" ? a.translate(b.right - this.ia[1] - g, b.top + this.ia[0] + g) : e == "center" && a.translate((b.left + this.ia[3] + b.right - this.ia[1]) * 0.5, b.top + this.ia[0] + g);
        b = xg(this);
        a.fillStyle = this.Ne;
        a.font = this.Oe + " " + this.wb + "px/" + b + " " + this.Dd;
        a.textAlign = e;
        a.textBaseline = "top";
        if (this.ya || this.ta.x || this.ta.y)
            a.shadowColor = this.Ec,
            a.shadowOffsetX = this.ta.x,
            a.shadowOffsetY = this.ta.y,
            a.shadowBlur = this.ya;
        if (d || c != this.Xe) {
            d = [];
            e = "";
            g = this.ke;
            for (h = 0; h < g.length; h++) {
                m = 0;
                if (this.Wd && (l = g[h].match(/\n/g)))
                    m = l.length;
                e == "" ? e = g[h] : (l = a.measureText(Ta(e + g[h])),
                l.width > c ? (d.push(Ta(e)),
                m--,
                e = g[h]) : e += g[h]);
                for (l = 0; l < m; l++)
                    d.push(Ta(e)),
                    e = ""
            }
            d.push(e);
            this.Od = d;
            this.Xe = c
        }
        if (this.Od) {
            c = b * this.wb;
            b = (p(this.ya) ? Math.abs(this.ya) : 0) + (p(this.ta) ? Math.abs(this.ta.y) / 2 : 0);
            c = Cb ? Math.floor(c) : Math.round(c);
            for (d = 0; d < this.Od.length; d++)
                a.fillText(this.Od[d], 0, c * d + b - 0.5)
        }
        a.restore()
    }
    ;
    function yg() {
        this.mc = [];
        this.$b(0, 0, 0, 1)
    }
    s(yg, Bf);
    n = yg.prototype;
    n.id = "lineargradient";
    n.vc = function(a) {
        (zb || Ab) && Pd(a, u)
    }
    ;
    n.$b = function(a, b, c, d) {
        this.G = [a, b, c, d];
        return this
    }
    ;
    n.addColorStop = function(a, b) {
        var c = mb(arguments);
        c.shift();
        this.mc.push([a, Cf(c)]);
        return this
    }
    ;
    n.Nf = function(a) {
        return Cb ? "color-stop(" + a[0] + ", " + a[1].la + ")" : a[1].la + " " + a[0] * 100 * this.Dg + "%"
    }
    ;
    n.Eb = function(a, b) {
        var c, d = b.m();
        c = d.right - d.left;
        var e = d.bottom - d.top;
        if (!Cb) {
            var g = (this.G[2] - this.G[0]) * c
              , h = (this.G[1] - this.G[3]) * e
              , m = d.left + c * this.G[0]
              , l = d.top + e * this.G[1]
              , q = Math.atan2(h, g)
              , A = -h / g;
            A == Infinity && (A = Math.pow(10, 10));
            d = q > 0 && q < Math.PI / 2 ? [d.right, d.top] : q > 0 ? [d.left, d.top] : q > -Math.PI / 2 ? [d.right, d.bottom] : [d.left, d.bottom];
            d = (d[1] + 1 / A * d[0] - l + A * m) / (A + 1 / A);
            A = A * d + l - m * A;
            d -= m;
            A -= l;
            this.Dg = Math.sqrt((g * g + h * h) / (d * d + A * A))
        }
        g = hb(this.mc, this.Nf, this);
        c = Cb ? "-webkit-gradient(linear," + this.G[0] * 100 + "% " + this.G[1] * 100 + "%," + this.G[2] * 100 + "% " + this.G[3] * 100 + "%," + g.join(",") + ")" : "linear-gradient(" + this.G[0] * 100 + "% " + this.G[1] * 100 + "% " + Math.atan2((this.G[1] - this.G[3]) * e, (this.G[2] - this.G[0]) * c) + "rad," + g.join(",") + ")";
        Bb && (c = "-moz-" + c);
        a.style.background = c
    }
    ;
    n.Zb = function(a, b) {
        for (var c = this.G, d = b.m(), e = d.right - d.left, g = d.bottom - d.top, c = a.createLinearGradient(d.left + e * c[0], d.top + g * c[1], d.left + e * c[2], d.top + g * c[3]), d = 0; d < this.mc.length; d++)
            c.addColorStop(this.mc[d][0], this.mc[d][1].la);
        a.fillStyle = c
    }
    ;
    function zg(a) {
        pg.call(this, this.Sd(a), this.Sd(a));
        this.borderWidth = 2;
        this.g(a);
        this.Ua("#62be00")
    }
    s(zg, pg);
    n = zg.prototype;
    n.Sd = function(a) {
        var b = new Xe;
        b.hb = new Xe;
        b.label = K(L(M(af(new N(a), "center"), '"Trebuchet MS"'), "#010101"), 17);
        b.appendChild(b.hb);
        b.hb.appendChild(b.label);
        return b
    }
    ;
    n.Ua = function(a) {
        a = Cf(a);
        fb([this.ma, this.Pa], function(b) {
            var c;
            b == this.Pa ? (c = a.r(),
            c = Gf(c, 1, -0.2)) : c = a;
            b.c(c);
            var d = (new yg).$b(0, 0, 0, 1);
            d.addColorStop(0, Ff(c.r(), 0.13));
            d.addColorStop(0.5, Ff(c.r(), 0.05));
            d.addColorStop(0.52, c);
            d.addColorStop(1, c);
            b.hb.c(d)
        }, this);
        return this
    }
    ;
    n.g = function(a) {
        this.ma.label.g(a);
        this.Pa.label.g(a);
        return this
    }
    ;
    n.b = function(a, b) {
        if (this.ma) {
            this.ma.b.apply(this.ma, arguments);
            var c = this.ma.t();
            fb([this.ma, this.Pa], function(a) {
                a.b(c);
                var b = c.r();
                b.width -= this.borderWidth;
                b.height -= this.borderWidth;
                a.hb.b(b)
            }, this)
        }
        return this
    }
    ;
    n.t = function() {
        return this.ma.t()
    }
    ;
    function cf(a) {
        zg.call(this, a);
        this.borderWidth = 4;
        this.Ua("#1eb1d8")
    }
    s(cf, zg);
    function Ag(a, b, c, d) {
        var e = (new P).a(0, 0).b(104, 104)
          , g = (new H).a(0, 60);
        e.appendChild(g);
        if (lg(d.stars)) {
            if (d.stars > 0) {
                var h = (new P).c(Me + "star.png").a(-29, 8);
                g.appendChild(h)
            }
            d.stars > 1 && (h = (new P).c(Me + "star.png").a(0, 8),
            g.appendChild(h));
            d.stars > 2 && (d = (new P).c(Me + "star.png").a(29, 8),
            g.appendChild(d))
        } else
            B(g, !0);
        g = !1;
        Ne == 0 && a > 1 ? g = !0 : Je < c && (g = !0);
        Be.Gf && (g = !1);
        g ? (b = (new P).c(J + "bttnLocked.png").b(104, 104),
        b.l(1.1, 1.1),
        e.rg = c,
        e.gg = !0) : (b = (new P).c(J + "bttn" + b + ".png").b(104, 104),
        a = M(K(L(af(new N(a), "center"), "#fff"), 30).a(0, 4), "futuraBold").b(60, 40),
        b.appendChild(a),
        b.l(1.1, 1.1));
        e.appendChild(b);
        return e
    }
    cf = function(a, b) {
        var c = new P
          , d = a.length * 18
          , e = ed();
        e.setAttribute("class", "homeButton");
        e.setAttribute("style", "left: -" + (d + 70) / 2 + "px");
        e.innerHTML = a;
        if (b != k) {
            var g = (new P).c(Oe.m(b));
            b == "iconStarter.png" || b == "iconJunior.png" || b == "iconExpert.png" || b == "iconMaster.png" ? (g.a(-(d / 2) - 20, -4),
            e.setAttribute("style", "padding-left: 65px;left: -" + (d + 100) / 2 + "px")) : b == "iconStarterHome.png" || b == "iconJuniorHome.png" || b == "iconExpertHome.png" || b == "iconMasterHome.png" ? g.a(-(d / 2) - 10, -3) : g.a(-(d / 2) - 7, -4)
        }
        c.appendChild(e);
        b != k ? (c.appendChild(g),
        b == "iconHome.png" ? c.b(d + 100, 70) : c.b(d + 80, 70)) : (e.setAttribute("style", "padding-left: 20px;left: -" + d + "px"),
        c.b(d + 80, 70));
        return c
    }
    ;
    function Bg(a, b) {
        var c = new P
          , d = ed();
        d.setAttribute("class", "pauseButton");
        d.setAttribute("style", "left: -105px");
        d.innerHTML = a;
        c.appendChild(d);
        d = (new P).c(Oe.m(b));
        b == "iconHome.png" ? d.a(-78, -2).l(0.9) : d.a(-71, -1);
        c.appendChild(d);
        c.b(210, 55);
        return c
    }
    function ef(a) {
        var b = new P
          , c = a.length * 18
          , d = ed();
        d.setAttribute("class", "smallButton");
        d.setAttribute("style", "left: -" + (c + 10) / 2 + "px");
        d.innerHTML = a;
        b.appendChild(d);
        b.b(c, 40);
        return b
    }
    function Cg() {
        var a = Je
          , b = new P
          , c = ed();
        c.setAttribute("class", "scoreButton");
        c.setAttribute("style", "left: -100px");
        c.innerHTML = a;
        b.appendChild(c);
        a = (new P).c(Oe.m("trophy.png"));
        a.a(-60, -4);
        b.appendChild(a);
        a = (new P).c(Oe.m("star.png"));
        a.a(60, -4);
        b.appendChild(a);
        b.b(200, 70);
        return b
    }
    function Dg(a, b) {
        var c = new P
          , d = ed();
        d.setAttribute("class", "languageButton");
        d.setAttribute("style", "left: -37.5px");
        d.innerHTML = a;
        c.appendChild(d);
        d = (new P).c(Oe.m(b)).a(0, -1);
        c.appendChild(d);
        c.b(75, 55);
        return c
    }
    cf.prototype.Sd = function() {
        var a = vg((new Xe).c("#1B355F"), 10);
        a.hb = vg(new Xe, 10);
        a.label = K(L(M(af(new N, "center"), "showcard"), "#1B355F"), 20);
        a.appendChild(a.hb);
        a.hb.appendChild(a.label);
        return a
    }
    ;
    cf.prototype.Ua = function(a) {
        a = Cf(a);
        fb([this.ma, this.Pa], function(b) {
            var c = b == this.Pa ? Ff(a.r(), 0.1) : a
              , d = Ff(c.r(), 0.3)
              , e = (new yg).$b(0, 0, 0, 1);
            e.addColorStop(0, d);
            e.addColorStop(0.45, c);
            e.addColorStop(0.55, c);
            e.addColorStop(1, d);
            b.hb.c(e)
        }, this);
        return this
    }
    ;
    function df(a, b) {
        Mf.call(this, a, b)
    }
    s(df, Mf);
    df.prototype.start = function() {
        D(this.ra, 0);
        B(this.ra, !1);
        var a = qf((new V(0)).e(this.z));
        w(a, T, function() {
            this.jb && D(this.jb, 1)
        }, !1, this);
        this.jb && G(this.jb, a);
        a = (new V(1)).e(this.z);
        G(this.ra, a);
        w(a, T, this.finish, !1, this)
    }
    ;
    var jg = {
        Starter: {
            1: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece1: {
                    squarePos: 4,
                    rotation: 0
                },
                piece9: {
                    squarePos: 6,
                    rotation: 0
                },
                piece10: {
                    squarePos: 11,
                    rotation: 0
                },
                piece11: {
                    squarePos: 13,
                    rotation: 0
                }
            },
            2: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece7: {
                    squarePos: 16,
                    rotation: 180
                },
                piece9: {
                    squarePos: 13,
                    rotation: 0
                },
                piece10: {
                    squarePos: 9,
                    rotation: 0
                },
                piece11: {
                    squarePos: 18,
                    rotation: 0
                }
            },
            3: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece5: {
                    squarePos: 7,
                    rotation: 90
                },
                piece9: {
                    squarePos: 6,
                    rotation: 0
                },
                piece10: {
                    squarePos: 5,
                    rotation: 0
                },
                piece11: {
                    squarePos: 12,
                    rotation: 0
                }
            },
            4: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece6: {
                    squarePos: 12,
                    rotation: 90
                },
                piece9: {
                    squarePos: 16,
                    rotation: 0
                },
                piece10: {
                    squarePos: 9,
                    rotation: 0
                },
                piece11: {
                    squarePos: 14,
                    rotation: 0
                }
            }
        },
        Junior: {
            1: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece1: {
                    squarePos: 16,
                    rotation: 270
                },
                piece8: {
                    squarePos: 5,
                    rotation: 90
                },
                piece9: {
                    squarePos: 9,
                    rotation: 0
                },
                piece10: {
                    squarePos: 12,
                    rotation: 0
                }
            },
            2: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece5: {
                    squarePos: 16,
                    rotation: 90
                },
                piece8: {
                    squarePos: 11,
                    rotation: 180
                },
                piece9: {
                    squarePos: 2,
                    rotation: 0
                },
                piece10: {
                    squarePos: 5,
                    rotation: 0
                },
                piece11: {
                    squarePos: 18,
                    rotation: 0
                }
            },
            3: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece1: {
                    squarePos: 10,
                    rotation: 90
                },
                piece2: {
                    squarePos: 8,
                    rotation: 0
                },
                piece9: {
                    squarePos: 2,
                    rotation: 0
                },
                piece10: {
                    squarePos: 12,
                    rotation: 0
                },
                piece11: {
                    squarePos: 14,
                    rotation: 0
                }
            },
            4: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece7: {
                    squarePos: 18,
                    rotation: 180
                },
                piece8: {
                    squarePos: 12,
                    rotation: 270
                },
                piece3: {
                    squarePos: 24,
                    rotation: 90
                },
                piece9: {
                    squarePos: 16,
                    rotation: 0
                },
                piece10: {
                    squarePos: 21,
                    rotation: 0
                },
                piece11: {
                    squarePos: 9,
                    rotation: 0
                }
            }
        },
        Expert: {
            1: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece1: {
                    squarePos: 8,
                    rotation: 270
                },
                piece6: {
                    squarePos: 9,
                    rotation: 180
                },
                piece8: {
                    squarePos: 11,
                    rotation: 180
                },
                piece9: {
                    squarePos: 13,
                    rotation: 0
                },
                piece10: {
                    squarePos: 6,
                    rotation: 0
                }
            },
            2: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece1: {
                    squarePos: 0,
                    rotation: 0
                },
                piece6: {
                    squarePos: 5,
                    rotation: 180
                },
                piece7: {
                    squarePos: 4,
                    rotation: 0
                },
                piece9: {
                    squarePos: 9,
                    rotation: 0
                },
                piece10: {
                    squarePos: 2,
                    rotation: 0
                },
                piece11: {
                    squarePos: 23,
                    rotation: 0
                }
            },
            3: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece3: {
                    squarePos: 0,
                    rotation: 0
                },
                piece8: {
                    squarePos: 12,
                    rotation: 180
                },
                piece1: {
                    squarePos: 23,
                    rotation: 90
                },
                piece9: {
                    squarePos: 7,
                    rotation: 0
                },
                piece10: {
                    squarePos: 13,
                    rotation: 0
                },
                piece11: {
                    squarePos: 14,
                    rotation: 0
                }
            },
            4: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece3: {
                    squarePos: 14,
                    rotation: 90
                },
                piece1: {
                    squarePos: 8,
                    rotation: 90
                },
                piece4: {
                    squarePos: 11,
                    rotation: 90
                },
                piece9: {
                    squarePos: 20,
                    rotation: 0
                },
                piece10: {
                    squarePos: 10,
                    rotation: 0
                }
            }
        },
        Master: {
            1: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece6: {
                    squarePos: 5,
                    rotation: 180
                },
                piece8: {
                    squarePos: 15,
                    rotation: 180
                },
                piece1: {
                    squarePos: 21,
                    rotation: 90
                },
                piece9: {
                    squarePos: 18,
                    rotation: 0
                },
                piece10: {
                    squarePos: 9,
                    rotation: 0
                },
                piece11: {
                    squarePos: 17,
                    rotation: 0
                }
            },
            2: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece6: {
                    squarePos: 8,
                    rotation: 90
                },
                piece1: {
                    squarePos: 12,
                    rotation: 0
                },
                piece5: {
                    squarePos: 22,
                    rotation: 90
                },
                piece9: {
                    squarePos: 16,
                    rotation: 0
                },
                piece10: {
                    squarePos: 1,
                    rotation: 0
                },
                piece11: {
                    squarePos: 9,
                    rotation: 0
                }
            },
            3: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece8: {
                    squarePos: 7,
                    rotation: 90
                },
                piece1: {
                    squarePos: 22,
                    rotation: 90
                },
                piece5: {
                    squarePos: 14,
                    rotation: 90
                },
                piece9: {
                    squarePos: 2,
                    rotation: 0
                },
                piece10: {
                    squarePos: 1,
                    rotation: 0
                },
                piece11: {
                    squarePos: 16,
                    rotation: 0
                }
            },
            4: {
                rows: 7,
                cols: 7,
                boardSquareSize: 150,
                piece6: {
                    squarePos: 12,
                    rotation: 0
                },
                piece8: {
                    squarePos: 0,
                    rotation: 0
                },
                piece1: {
                    squarePos: 9,
                    rotation: 0
                },
                piece4: {
                    squarePos: 19,
                    rotation: 90
                },
                piece9: {
                    squarePos: 2,
                    rotation: 0
                },
                piece10: {
                    squarePos: 3,
                    rotation: 0
                },
                piece11: {
                    squarePos: 21,
                    rotation: 0
                }
            }
        }
    };
    function Eg() {
        Ja.call(this);
        this.k.style.cssText = "background:rgba(255,255,255,.8)"
    }
    s(Eg, Ja);
    function Fg(a) {
        this.pc = a;
        this.identifier = 0
    }
    Fg.prototype.w = function(a, b, c) {
        for (var a = ha(a) ? a : [a], d = 0; d < a.length; d++)
            this.pc.w(this, a[d], b);
        c && this.event.stopPropagation()
    }
    ;
    Fg.prototype.Bc = function(a) {
        var b = p(a)
          , c = ha(a) ? a : [a];
        if (a = this.pc.lb[this.identifier]) {
            var d = this
              , a = gb(a, function(a) {
                return !p(d.mb) || a[0] == d.mb && (!b || eb(c, a[1]) >= 0) ? (yc(a[0], a[1], a[2]),
                !1) : !0
            });
            a.length ? this.pc.lb[this.identifier] = a : delete this.pc.lb[this.identifier]
        }
    }
    ;
    Fg.prototype.r = function() {
        var a = new Fg(this.pc);
        Ia(a, this);
        return a
    }
    ;
    function Gg(a) {
        this.ub = a;
        this.ka = {};
        this.lb = {}
    }
    Gg.prototype.cd = function(a, b) {
        p(this.ka[b]) ? eb(this.ka[b], a) >= 0 || (this.ka[b].push(a),
        this.ka[b].sort(Ud)) : (this.ka[b] = [a],
        w(b.substring(0, 5) == "touch" && a != this.ub ? document : b.substring(0, 3) == "key" ? window : this.ub.k.parentNode, b, this, !1, this))
    }
    ;
    Gg.prototype.Bc = function(a, b) {
        p(this.ka[b]) && (jb(this.ka[b], a),
        this.ka[b].length || (yc(this.ub.k.parentNode, b, this, !1, this),
        delete this.ka[b]))
    }
    ;
    function de(a, b) {
        for (var c in a.ka) {
            var d = a.ka[c];
            eb(d, b) >= 0 && d.sort(Ud)
        }
    }
    Gg.prototype.w = function(a, b, c) {
        var d = a.identifier;
        p(this.lb[d]) || (this.lb[d] = []);
        this.lb[d].push([a.mb, b, c]);
        w(a.mb, b, fa)
    }
    ;
    Gg.prototype.handleEvent = function(a) {
        if (p(this.ka[a.type])) {
            for (var b = this.ka[a.type].slice(), c = !1, d = 0, e = 0; !e; ) {
                var g = new Fg(this);
                g.type = a.type;
                g.event = a;
                if (a.type.substring(0, 5) == "touch") {
                    var h = a.Ra.changedTouches[d];
                    g.Q = new t(h.pageX,h.pageY);
                    g.identifier = h.identifier;
                    d++;
                    d >= a.Ra.changedTouches.length && (e = 1)
                } else
                    g.Q = new t(a.clientX + document.body.scrollLeft + document.documentElement.scrollLeft,a.clientY + document.body.scrollTop + document.documentElement.scrollTop),
                    e = 1;
                if (p(this.lb[g.identifier])) {
                    for (var h = this.lb[g.identifier], m = 0; m < h.length; m++)
                        if (h[m][1] == a.type || ha(h[m][1]) && eb(h[m][1], a.type) >= 0) {
                            var l = h[m][0];
                            g.mb = l;
                            g.position = l.Ja(g.Q);
                            h[m][2].call(l, g);
                            c = !0
                        }
                    if (a.type == "touchend" || a.type == "touchcancel" || a.type == "mouseup" || a.type == "keyup")
                        delete g.mb,
                        g.Bc()
                } else
                    for (m = 0; m < b.length; m++)
                        if (l = b[m],
                        !((this.ub.H.length ? this.ub.H[this.ub.H.length - 1] : k) != l.Nc() && l != this.ub) && !l.Pc && l.Y)
                            if (g.mb = l,
                            l.i(g) || a.type.substring(0, 3) == "key")
                                if (g.mb = l,
                                l.dispatchEvent(g),
                                c = !0,
                                g.event.Ta)
                                    break
            }
            c && a.preventDefault()
        }
    }
    ;
    function Hg(a) {
        this.Hb = a || window;
        this.Sc = w(this.Hb, "resize", this.Xf, !1, this);
        this.U = $c(this.Hb || window);
        if (Cb && Gb || zb && this.Hb.self != this.Hb.top)
            this.kd = window.setInterval(ta(this.ze, this), Ig)
    }
    s(Hg, Ec);
    var Ig = 500;
    n = Hg.prototype;
    n.Sc = k;
    n.Hb = k;
    n.U = k;
    n.kd = k;
    n.t = function() {
        return this.U ? this.U.r() : k
    }
    ;
    n.ja = function() {
        Hg.kb.ja.call(this);
        if (this.Sc)
            zc(this.Sc),
            this.Sc = k;
        if (this.kd)
            window.clearInterval(this.kd),
            this.kd = k;
        this.U = this.Hb = k
    }
    ;
    n.Xf = function() {
        this.ze()
    }
    ;
    n.ze = function() {
        var a = $c(this.Hb || window);
        if (!(a == this.U || (!a || !this.U ? 0 : a.width == this.U.width && a.height == this.U.height)))
            this.U = a,
            this.dispatchEvent("resize")
    }
    ;
    function Jg(a, b, c) {
        Dd.call(this);
        this.Y = !0;
        this.d(0, 0);
        this.H = [];
        this.De = [];
        this.qc = "lime-director";
        Rd(this);
        a.appendChild(this.k);
        if (Cb && Db)
            this.Ce = document.createElement("div"),
            Qc(this.Ce, "lime-cover-below"),
            fd(this.Ce, this.k),
            this.Be = document.createElement("div"),
            Qc(this.Be, "lime-cover-above"),
            gd(this.Be, this.k);
        a.style.position != "absolute" && (a.style.position = "relative");
        a.style.overflow = "hidden";
        if (a == document.body) {
            sd("html,body{margin:0;padding:0;height:100%;}");
            var d = document.createElement("meta");
            d.name = "viewport";
            var e = "width=device-width,initial-scale=1.0,minimum-scale=1,maximum-scale=1.0,user-scalable=no";
            /android/i.test(navigator.userAgent) && (e += ",target-densityDpi=device-dpi");
            d.content = e;
            document.getElementsByTagName("head").item(0).appendChild(d);
            if (Db && !o.navigator.th) {
                var g = this;
                setTimeout(function() {
                    window.scrollTo(0, 0);
                    g.wc()
                }, 100)
            }
        }
        var h, a = qd(a);
        this.b(new Da(h = b || a.width || 400,c || a.height * h / a.width || 400));
        this.Ge && hd(this.Pf);
        this.dg = this.Ge = !1;
        O.Cf(this);
        this.dg ? (this.ae = new (this.oh || Eg),
        Kg(this, this.ae)) : this.ae && (Lg(this),
        delete this.ae);
        b = new Hg;
        w(b, "resize", this.wc, !1, this);
        w(o, "orientationchange", this.wc, !1, this);
        O.dd(this.bc, this);
        this.vb = new Gg(this);
        w(this, ["touchmove", "touchstart"], function(a) {
            a.event.preventDefault()
        }, !1, this);
        w(this, ["mouseup", "touchend", "mouseout", "touchcancel"], function() {}, !1);
        this.wc()
    }
    s(Jg, Dd);
    n = Jg.prototype;
    n.ba = function() {
        return this
    }
    ;
    n.Nc = ba(k);
    n.bc = function(a) {
        if (this.Ge && (this.Pe++,
        this.nd += a,
        this.nd > 100))
            this.Of = 1E3 * this.Pe / this.nd,
            jd(this.Pf, this.Of.toFixed(2)),
            this.nd = this.Pe = 0;
        Aa()
    }
    ;
    function R(a, b, c) {
        var d = Mg;
        a.b(d.t().r());
        var b = b || Mf
          , e = k;
        d.H.length && (e = d.H[d.H.length - 1]);
        for (var g = [], h = d.H.length; --h >= 0; )
            be(d.H[h]),
            g.push(d.H[h].k),
            d.H[h].v = k;
        d.H.length = 0;
        d.H.push(a);
        a.k.style.display = "none";
        d.k.appendChild(a.k);
        a.v = d;
        Zd(a);
        a = new b(e,a);
        xc(a, "end", function() {
            for (var a = g.length; --a >= 0; )
                hd(g[a]);
            g.length = 0
        }, !1, d);
        p(c) && a.e(c);
        a.start()
    }
    n.Gb = function() {
        this.aa &= -65
    }
    ;
    function Kg(a, b) {
        var c;
        b.b(a.t().r());
        if (p(i) && a.H.length)
            c = a.H[a.H.length - 1],
            c = new i(c,b),
            p(i) && c.e(i),
            b.k.style.display = "none";
        a.H.push(b);
        a.k.appendChild(b.k);
        b.v = a;
        Zd(b);
        c && c.start()
    }
    function Lg(a) {
        var b, c = a.H.length ? a.H[a.H.length - 1] : k;
        if (c !== k) {
            var d = function() {
                be(c);
                c.v = k;
                hd(c.k);
                this.H.pop();
                c = k
            };
            p(i) && a.H.length > 1 ? (b = new i(c,a.H[a.H.length - 2]),
            p(i) && b.e(i),
            xc(b, "end", d, !1, a)) : d.call(a);
            b && b.start()
        }
    }
    n.Ja = function(a) {
        a = a.r();
        a.x -= this.Lc.x + this.f.x;
        a.y -= this.Lc.y + this.f.y;
        a.x /= this.T.x;
        a.y /= this.T.y;
        return a
    }
    ;
    n.Uc = function(a) {
        a = a.r();
        a.x *= this.T.x;
        a.y *= this.T.y;
        a.x += this.Lc.x + this.f.x;
        a.y += this.Lc.y + this.f.y;
        return a
    }
    ;
    n.update = function() {
        Dd.prototype.update.call(this);
        for (var a = this.De.length; --a >= 0; )
            this.De[a].update()
    }
    ;
    n.wc = function() {
        var a = qd(this.k.parentNode);
        if (this.k.parentNode == document.body && (window.scrollTo(0, 0),
        ka(window.innerHeight)))
            a.height = window.innerHeight;
        var b;
        b = this.t().r();
        b = b.scale(b.width / b.height > a.width / a.height ? a.width / b.width : a.height / b.height);
        this.l(b.width / this.t().width);
        a.width / a.height < b.width / b.height ? this.a(0, (a.height - b.height) / 2) : this.a((a.width - b.width) / 2, 0);
        var c = this.k.parentNode, d, e = Vc(c), g = ld(c, "position"), h = Bb && e.getBoxObjectFor && !c.getBoundingClientRect && g == "absolute" && (d = e.getBoxObjectFor(c)) && (d.screenX < 0 || d.screenY < 0);
        b = new t(0,0);
        var m;
        d = e ? e.nodeType == 9 ? e : Vc(e) : document;
        if (m = Ab)
            if (m = !Rb())
                m = Tc(d),
                m = !Xc(m.Za);
        m = m ? d.body : d.documentElement;
        if (c != m)
            if (c.getBoundingClientRect)
                d = md(c),
                e = Tc(e).Za,
                c = !Cb && Xc(e) ? e.documentElement : e.body,
                e = e.parentWindow || e.defaultView,
                c = new t(e.pageXOffset || c.scrollLeft,e.pageYOffset || c.scrollTop),
                b.x = d.left + c.x,
                b.y = d.top + c.y;
            else if (e.getBoxObjectFor && !h)
                d = e.getBoxObjectFor(c),
                c = e.getBoxObjectFor(m),
                b.x = d.screenX - c.screenX,
                b.y = d.screenY - c.screenY;
            else {
                d = c;
                do {
                    b.x += d.offsetLeft;
                    b.y += d.offsetTop;
                    d != c && (b.x += d.clientLeft || 0,
                    b.y += d.clientTop || 0);
                    if (Cb && ld(d, "position") == "fixed") {
                        b.x += e.body.scrollLeft;
                        b.y += e.body.scrollTop;
                        break
                    }
                    d = d.offsetParent
                } while (d && d != c);
                if (zb || Cb && g == "absolute")
                    b.y -= e.body.offsetTop;
                for (d = c; (d = nd(d)) && d != e.body && d != m; )
                    if (b.x -= d.scrollLeft,
                    !zb || d.tagName != "TR")
                        b.y -= d.scrollTop
            }
        this.Lc = b;
        if (Db && this.k.parentNode == document.body) {
            if (this.lf)
                b = this.lf,
                hd(b.ownerNode || b.owningElement || b);
            this.lf = sd("html{height:" + (a.height + 120) + "px;overflow:hidden;}")
        }
    }
    ;
    n.i = function(a) {
        if (a && a.Q)
            a.position = this.Ja(a.Q);
        return !0
    }
    ;
    function Ng(a, b, c) {
        P.call(this);
        this.je = Math.round(a / 2);
        this.Wg = a - this.je;
        this.ie = Math.round(b / 2);
        this.Vg = b - this.ie;
        this.lh = 12.5;
        this.j = c / 2;
        this.va = this.je * c;
        this.ob = this.ie * c;
        this.rows = a;
        this.cols = b;
        this.b(this.va, this.ob).d(0, 0);
        this.za = [];
        for (b = a = 0; b < this.ie; b++) {
            for (var d = 0; d < this.je; d++) {
                var e = D((new P).d(0.5, 0.5).vf(1), 0.5).b(150, 150).a(d * c + c / 2, b * c + c / 2);
                B(e, !0);
                this.za[a] = e;
                this.appendChild(this.za[a]);
                a += 1
            }
            if (b < this.Vg)
                for (d = 0; d < this.Wg; d++)
                    e = D((new P).d(0.5, 0.5).vf(1), 0.5).b(150, 150).a(d * c + c, b * c + c),
                    B(e, !0),
                    this.za[a] = e,
                    this.appendChild(this.za[a]),
                    a += 1
        }
    }
    s(Ng, P);
    u.ec = {};
    v.ec = {};
    function W() {
        P.call(this)
    }
    s(W, P);
    W.prototype.id = "circle";
    W.prototype.Va = [Ha(v.O, v.ec), Ha(u.O, u.ec)];
    W.prototype.i = function(a) {
        var b = this.Ja(a.Q)
          , c = this.U
          , d = this.Jb
          , e = c.width * 0.5
          , g = c.height * 0.5
          , h = b.x - c.width * (0.5 - d.x)
          , c = b.y - c.height * (0.5 - d.y);
        return h * h / (e * e) + c * c / (g * g) < 1 ? (a.position = b,
        !0) : !1
    }
    ;
    v.ec.R = function(a) {
        var b = this.t();
        v.O.R.call(this, a);
        Bd(a, b.width * 0.5, b.height * 0.5)
    }
    ;
    u.ec.R = function(a) {
        this.t();
        var b = this.yb()
          , c = this.m()
          , d = (c.right - c.left) * 0.5
          , c = (c.bottom - c.top) * 0.5;
        a.save();
        a.save();
        a.scale(d, c);
        a.translate(1 - 2 * b.x, 1 - 2 * b.y);
        a.beginPath();
        a.arc(0, 0, 1, 0, 2 * Math.PI, !1);
        a.closePath();
        a.restore();
        a.clip();
        u.O.R.call(this, a);
        this.ea && (a.lineWidth *= 2,
        a.stroke());
        a.restore()
    }
    ;
    var Og;
    function Y(a) {
        a && O.X(a, F);
        Ja.call(this);
        groupIsMoving = !1;
        levelselectBackground = (new P).c(J + "bgLevelSelect.jpg").b(960, 600).a(0, 0).d(0, 0);
        this.appendChild(levelselectBackground);
        this.appendChild(M(L(K(new N, 23).g(I.helpTitle).a(480, 204), "#fff").b(905, 25), "futuraBold"));
        Y.gb = new H;
        var b = (new H).b(960, 600).d(0, 0).a(0, 0);
        b.kc = 1;
        Y.gb.appendChild(b);
        var c = (new P).c(J + "help1.jpg").a(120, 230).d(0, 0);
        b.appendChild(c);
        c = af(M(L(K(new N, 20).g(I.help1).a(425, 230), "#fff").b(400, 200), "futuraBold").d(0, 0), "left");
        b.appendChild(c);
        c = af(M(L(K(new N, 20).g(I.help1Sub1).a(425, 350), "#fff").b(400, 200), "futuraBold").d(0, 0), "left");
        b.appendChild(c);
        c = af(M(L(K(new N, 20).g(I.help1Sub2).a(425, 430), "#fff").b(400, 200), "futuraBold").d(0, 0), "left");
        b.appendChild(c);
        c = af(M(L(K(new N, 20).g(I.help1Sub3).a(425, 500), "#fff").b(400, 200), "futuraBold").d(0, 0), "left");
        b.appendChild(c);
        var d = (new H).b(960, 600).d(0, 0).a(960, 0);
        d.kc = 2;
        Y.gb.appendChild(d);
        c = (new P).c(J + "help2.jpg").a(120, 230).d(0, 0);
        d.appendChild(c);
        c = af(M(L(K(new N, 20).g(I.help2).a(425, 230), "#fff").b(320, 200), "futuraBold").d(0, 0), "left");
        d.appendChild(c);
        this.appendChild(Y.gb);
        Og = b;
        Y.Z = (new P).c(Me + "levelSelectArrow.png").b(47, 81).a(870, 245).d(0, 0);
        w(Y.Z, ["mousedown", "touchstart"], function() {
            groupIsMoving || (groupIsMoving = !0,
            Y.Fd())
        });
        this.appendChild(Y.Z);
        Y.S = Nd((new P).c(Me + "levelSelectArrow.png").b(47, 81).a(80, 323).d(0, 0), 180);
        w(Y.S, ["mousedown", "touchstart"], function() {
            groupIsMoving || (groupIsMoving = !0,
            Y.Gd())
        });
        this.appendChild(Y.S);
        B(Y.S, !0);
        if (a) {
            var e = (new cf(I.resume,"iconResume.png")).a(800, 530);
            w(e, ["mousedown", "touchstart"], f = function(a) {
                e.l(1.1);
                a.w(["mouseup", "touchend"], function() {
                    e.l(1);
                    var a = new F(F.K,F.Xa);
                    R(a)
                })
            }
            );
            this.appendChild(e)
        }
        He == "all" ? (a = (new cf(I.home,"iconHome.png")).a(190, 530),
        w(a, ["mousedown", "touchstart"], function() {
            var a = new Q;
            De ? R(a) : R(a, df)
        })) : (a = (new cf(I.home,"icon" + He + ".png")).a(190, 530),
        w(a, ["mousedown", "touchstart"], function() {
            var a = new Q(!1,He);
            De ? R(a) : R(a, df)
        }));
        this.appendChild(a)
    }
    Y.Fd = function() {
        B(Y.Z, !0);
        B(Y.S, !0);
        Og = E(Y.gb, Og.kc);
        moveToNext = (new Lf(-960,0)).e(0.8);
        G(Y.gb, moveToNext);
        w(moveToNext, T, function() {
            groupIsMoving = !1;
            Og.kc < $d(Y.gb) && B(Y.Z, !1);
            B(Y.S, !1)
        })
    }
    ;
    Y.Gd = function() {
        B(Y.Z, !0);
        B(Y.S, !0);
        Og = E(Y.gb, Og.kc - 2);
        moveToPrev = (new Lf(960,0)).e(0.8);
        G(Y.gb, moveToPrev);
        w(moveToPrev, T, function() {
            groupIsMoving = !1;
            Og.kc > 1 && B(Y.S, !1);
            B(Y.Z, !1)
        })
    }
    ;
    s(Y, Ja);
    var Pg = {
        data: ba('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>frames</key><dict><key>block.png</key><dict><key>x</key><real>533</real><key>y</key><real>355</real><key>width</key><real>100</real><key>height</key><real>100</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>100</real><key>originalHeight</key><real>100</real></dict><key>piece1.png</key><dict><key>x</key><real>533</real><key>y</key><real>252</real><key>width</key><real>250</real><key>height</key><real>101</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>101</real></dict><key>piece2.png</key><dict><key>x</key><real>606</real><key>y</key><real>103</real><key>width</key><real>250</real><key>height</key><real>101</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>101</real></dict><key>piece3.png</key><dict><key>x</key><real>606</real><key>y</key><real>0</real><key>width</key><real>401</real><key>height</key><real>101</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>401</real><key>originalHeight</key><real>101</real></dict><key>piece4.png</key><dict><key>x</key><real>177</real><key>y</key><real>0</real><key>width</key><real>175</real><key>height</key><real>325</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>175</real><key>originalHeight</key><real>325</real></dict><key>piece5.png</key><dict><key>x</key><real>177</real><key>y</key><real>327</real><key>width</key><real>175</real><key>height</key><real>175</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>175</real><key>originalHeight</key><real>175</real></dict><key>piece6.png</key><dict><key>x</key><real>354</real><key>y</key><real>0</real><key>width</key><real>250</real><key>height</key><real>250</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>250</real><key>originalHeight</key><real>250</real></dict><key>piece7.png</key><dict><key>x</key><real>0</real><key>y</key><real>0</real><key>width</key><real>175</real><key>height</key><real>325</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>175</real><key>originalHeight</key><real>325</real></dict><key>piece8.png</key><dict><key>x</key><real>354</real><key>y</key><real>252</real><key>width</key><real>177</real><key>height</key><real>250</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>177</real><key>originalHeight</key><real>250</real></dict><key>virus.png</key><dict><key>x</key><real>0</real><key>y</key><real>327</real><key>width</key><real>175</real><key>height</key><real>175</real><key>offsetX</key><real>0</real><key>offsetY</key><real>0</real><key>originalWidth</key><real>175</real><key>originalHeight</key><real>175</real></dict></dict><key>texture</key><dict><key>width</key><integer>1024</integer><key>height</key><integer>512</integer></dict></dict></plist>')
    };
    var Mg, Qg, Rg;
    function Sg(a, b, c, d) {
        this.target = d || a.mb;
        this.Qa = [];
        this.qa = -1;
        this.y = this.x = 0;
        if (!b)
            b = this.target.Uc(new t(0,0)),
            this.x = a.Q.x - b.x,
            this.y = a.Q.y - b.y;
        a.w(["touchmove", "mousemove"], ta(this.Vd, this));
        a.w(["touchend", "touchcancel", "mouseup"], ta(this.Eg, this));
        this.Ag = c || k;
        this.dispatchEvent(new Yb(Tg))
    }
    s(Sg, Ec);
    var Tg = "start";
    Sg.prototype.ja = function() {
        Sg.kb.ja.call(this);
        this.Qa = this.target = this.Ra = k
    }
    ;
    Sg.prototype.Vd = function(a) {
        a = a.Q.r();
        a.x -= this.x;
        a.y -= this.y;
        var a = this.target.getParent().Ja(a)
          , b = this.Ag;
        objPos = this.target.f;
        var c;
        if (this.target.direction == "topleft")
            a.y = this.target.ab - (this.target.$a - a.x),
            c = objPos.x - a.x;
        else if (this.target.direction == "bottomleft")
            a.y = this.target.ab - (a.x - this.target.$a),
            c = a.x - objPos.x;
        else if (this.target.direction == "topright")
            a.y = this.target.$a - a.x + this.target.ab,
            c = objPos.x - a.x;
        else if (this.target.direction == "bottomright")
            a.y = a.x - this.target.$a + this.target.ab,
            c = a.x - objPos.x;
        if (Ug(b, a) && this.target.direction != "unknown") {
            this.target.a(a);
            this.dispatchEvent(new Yb("move"));
            c = -1;
            for (var d = Mc(this.target.m()), a = [], b = 0; b < this.Qa.length; b++) {
                var e = this.Qa[b];
                if (!la(e.Ef) || e.Ef(this.target)) {
                    var g = e.m()
                      , h = Hd(e, new t(g.left,g.top), this.target)
                      , e = Hd(e, new t(g.right,g.bottom), this.target)
                      , h = Mc(new Ca(Math.min(h.y, e.y),Math.max(h.x, e.x),Math.max(h.y, e.y),Math.min(e.x, h.x)));
                    (e = Nc(d, h)) && a.push([e.width * e.height / (h.width * h.height), b])
                }
            }
            a.length && (a = a.sort(function(a, b) {
                return b[0] - a[0]
            }),
            c = a[0][1]);
            if (c != this.qa)
                this.qa != -1 && la(this.Qa[this.qa].Te) && this.Qa[this.qa].Te(),
                this.qa = c,
                this.qa != -1 && la(this.Qa[this.qa].wf) && this.Qa[this.qa].wf(),
                c = new Yb("change"),
                c.ic = this.qa != -1 ? this.Qa[this.qa] : k,
                this.dispatchEvent(c)
        } else if (this.target.direction != "unknown")
            if (dragPiecesArray.length == 1) {
                for (c = 0; c < $d(F.q); c++)
                    if (E(F.q, c).type != "block" && !(eb(dragPiecesArray, E(F.q, c)) >= 0) && (d = E(F.q, c),
                    D(d, 1),
                    Vg(this.target, d, this.target.direction))) {
                        dragPiecesArray.push(d);
                        Wg(d);
                        Xg(this.target);
                        for (a = 0; a < $d(F.q); a++)
                            if (E(F.q, a).type != "block" && !(eb(dragPiecesArray, E(F.q, a)) >= 0) && (b = E(F.q, a),
                            Vg(d, b, this.target.direction))) {
                                dragPiecesArray.push(b);
                                Wg(b);
                                Xg(this.target);
                                for (h = 0; h < $d(F.q); h++)
                                    E(F.q, h).type != "block" && !(eb(dragPiecesArray, E(F.q, h)) >= 0) && (e = E(F.q, h),
                                    Vg(b, e, this.target.direction) && (dragPiecesArray.push(e),
                                    Wg(e),
                                    Xg(this.target)))
                            }
                    }
                Rg = k;
                Rg = Yg()
            } else if (dragPiecesArray.length > 1) {
                for (e = h = b = 0; e < dragPiecesArray.length; e++)
                    if (dragPiecesArray[e].id != this.target.id)
                        g = dragPiecesArray[e].f,
                        this.target.direction == "topleft" ? d = new t(g.x - c,g.y - c) : this.target.direction == "topright" ? d = new t(g.x - c,g.y + c) : this.target.direction == "bottomleft" ? d = new t(g.x + c,g.y - c) : this.target.direction == "bottomright" && (d = new t(g.x + c,g.y + c)),
                        dragPiecesArray[e].Sg = d,
                        b += d.x,
                        h += d.y;
                b = (a.x + b) / dragPiecesArray.length;
                h = (a.y + h) / dragPiecesArray.length;
                if (Ug(Rg, new t(b,h))) {
                    this.target.a(a);
                    for (c = 0; c < dragPiecesArray.length; c++)
                        dragPiecesArray[c].id != this.target.id && dragPiecesArray[c].a(dragPiecesArray[c].Sg)
                }
            }
    }
    ;
    function Xg(a) {
        var b = Zg(a);
        a.$a = a.f.x + b.x;
        a.ab = a.f.y + b.y
    }
    function Wg(a) {
        a.$a = a.f.x;
        a.ab = a.f.y
    }
    Sg.prototype.Eg = function() {
        if (this.qa != -1) {
            var a = new Yb("drop");
            a.ic = this.Qa[this.qa];
            la(a.ic.wf) && a.ic.Te();
            this.dispatchEvent(a);
            if (!a.Ta) {
                var b = Hd(a.ic.getParent(), a.ic.f, this.target.getParent())
                  , b = qf((new S(b)).e(0.5));
                G(this.target, b);
                la(a.sg) && w(b, T, a.sg, !1, this.target)
            }
        } else
            this.dispatchEvent(new Yb("cancel"));
        this.dispatchEvent(new Yb("end"));
        O.Bf(this.Oa, this)
    }
    ;
    function Ug(a, b) {
        var c = a.G
          , d = c.length
          , e = !1;
        if (d > 2) {
            var g, h;
            for (g = 0,
            h = d - 1; g < d; h = g++)
                c[g].y > b.y != c[h].y > b.y && b.x < (c[h].x - c[g].x) * (b.y - c[g].y) / (c[h].y - c[g].y) + c[g].x && (e = !e)
        }
        return e
    }
    function Vg(a, b, c) {
        for (var d = 0; d < $d(a); d++)
            if (E(a, d).u)
                for (var e = Sa(a, new t(E(a, d).f.x,E(a, d).f.y)), g = 0; g < $d(b); g++)
                    if (E(b, g).u) {
                        var h = Sa(b, new t(E(b, g).f.x,E(b, g).f.y));
                        if (c == "topleft") {
                            if (e.x - h.x > 0 && e.x - h.x < F.p / 1.7 && e.y - h.y > 0 && e.y - h.y < F.p / 1.7)
                                return !0
                        } else if (c == "topright") {
                            if (h.x - e.x > 0 && h.x - e.x < F.p / 1.7 && e.y - h.y > 0 && e.y - h.y < F.p / 1.7)
                                return !0
                        } else if (c == "bottomleft") {
                            if (e.x - h.x > 0 && e.x - h.x < F.p / 1.7 && h.y - e.y > 0 && h.y - e.y < F.p / 1.7)
                                return !0
                        } else if (c == "bottomright" && h.x - e.x > 0 && h.x - e.x < F.p / 1.7 && h.y - e.y > 0 && h.y - e.y < F.p / 1.7)
                            return !0
                    }
        return !1
    }
    ;u.le = {};
    function $g(a) {
        P.call(this);
        this.Jg.apply(this, arguments)
    }
    s($g, P);
    n = $g.prototype;
    n.id = "polygon";
    n.Va = [Ha(u.O, u.le)];
    n.Jg = function(a) {
        this.G = [];
        this.pe.apply(this, arguments);
        return this
    }
    ;
    n.pe = function(a) {
        a = mb(arguments);
        if (a.length) {
            if (a[0]instanceof t)
                fb(a, function(a) {
                    ah(this, a)
                }, this);
            else
                for (var b = 1; b < a.length; b += 2)
                    ah(this, new t(a[b - 1],a[b]));
            return this
        }
    }
    ;
    function ah(a, b) {
        a.G.length ? (a.Wc = Math.min(b.x, a.Wc),
        a.Xc = Math.min(b.y, a.Xc),
        a.Td = Math.max(b.x, a.Td),
        a.Ud = Math.max(b.y, a.Ud)) : (a.Wc = a.Td = b.x,
        a.Xc = a.Ud = b.y);
        a.G.push(b)
    }
    n.t = function() {
        return new Da(this.Td - this.Wc,this.Ud - this.Xc)
    }
    ;
    n.yb = function() {
        var a = this.t();
        return new pb(-this.Wc / a.width,-this.Xc / a.height)
    }
    ;
    n.i = function(a) {
        var b = this.G
          , c = b.length
          , a = this.Ja(a.Q)
          , d = !1;
        if (c > 2) {
            var e, g;
            for (e = 0,
            g = c - 1; e < c; g = e++)
                b[e].y > a.y != b[g].y > a.y && a.x < (b[g].x - b[e].x) * (a.y - b[e].y) / (b[g].y - b[e].y) + b[e].x && (d = !d)
        }
        return d
    }
    ;
    u.le.R = function(a) {
        this.t();
        var b = this.Qb
          , c = this.G;
        if (c.length > 2) {
            a.save();
            a.beginPath();
            a.moveTo(c[0].x, c[0].y);
            for (var d = 1; d < c.length; d++)
                a.lineTo(c[d].x, c[d].y);
            a.closePath();
            if (b)
                a.fillStyle = b.la;
            a.clip();
            u.O.R.call(this, a);
            this.ea && (a.lineWidth *= 2,
            a.stroke());
            a.restore()
        }
    }
    ;
    function bh(a) {
        switch (Number(a)) {
        case 1:
            return "topleft";
        case 2:
            return "top";
        case 3:
            return "topright";
        case 4:
            return "right";
        case 5:
            return "bottomright";
        case 6:
            return "bottom";
        case 7:
            return "bottomleft";
        case 8:
            return "left";
        default:
            return "unknown"
        }
    }
    function We(a) {
        if (F.Bd == !1) {
            F.Bd = !0;
            ce(a.target);
            F.pf.reload();
            F.pf.play();
            a.target.direction = "unknown";
            a.target.wg = !0;
            dragPiecesArray = [];
            dragPiecesArray.push(a.target);
            var b = k
              , b = Yg();
            new Sg(a,!1,b);
            D(a.target, 1);
            b = a.target.f;
            a.target.$a = b.x;
            a.target.ab = b.y;
            var c = a.Q.x
              , d = a.Q.y;
            a.w(["mousemove", "touchmove"], function(b) {
                a.target.wg = !1;
                if (Math.sqrt(Math.pow(b.Q.x - c, 2) + Math.pow(b.Q.y - d, 2)) > 5) {
                    var g = Math.atan2(b.Q.x - c, b.Q.y - d) / Math.PI + 1
                      , h = 0;
                    0.375 < g && g < 0.625 && (h = 8);
                    0.625 < g && g < 0.875 && (h = 7);
                    0.875 < g && g < 1.125 && (h = 6);
                    1.125 < g && g < 1.375 && (h = 5);
                    1.375 < g && g < 1.625 && (h = 4);
                    1.625 < g && g < 1.875 && (h = 3);
                    if (1.875 < g || g < 0.125)
                        h = 2;
                    0.125 < g && g < 0.375 && (h = 1);
                    c = b.Q.x;
                    d = b.Q.y
                }
                if (a.target.direction == "unknown") {
                    if (h == 1 || h == 3 || h == 5 || h == 7)
                        a.target.direction = bh(h)
                } else if (a.target.direction != bh(h) && (h == 1 || h == 3 || h == 5 || h == 7)) {
                    b = dragPiecesArray;
                    h = b[0];
                    g = Zg(h);
                    h.a(h.f.x + g.x, h.f.y + g.y);
                    isNaN(h.f.x) && (h.id == "puzzlePiece7" ? h.a(35, 111) : h.id == "puzzlePiece4" && h.a(111, 35));
                    for (var g = h.f.x - h.$a, h = h.f.y - h.ab, m = 1; m < b.length; m++)
                        b[m].a(b[m].$a + g, b[m].ab + h);
                    dragPiecesArray = [];
                    dragPiecesArray.push(a.target);
                    a.target.direction = "unknown";
                    b = document.createEvent("MouseEvents");
                    b.initMouseEvent("mouseup", !0, !0, window, 0, 0, 0, 500, 100, !1, !1, !1, !1, 0, k);
                    document.getElementById("gameContent").dispatchEvent(b)
                }
            });
            a.w(["mouseup", "touchend"], function() {
                F.qf.reload();
                F.qf.play();
                F.Bd = !1;
                if (a.target.direction != "unknown") {
                    F.jf += 1;
                    for (var b = 0; b < dragPiecesArray.length; b++) {
                        var c = Zg(dragPiecesArray[b]);
                        if (c == -100) {
                            if (dragPiecesArray[b].id == "puzzlePiece7")
                                dragPiecesArray[b].Pb = (new S(35,111)).e(0.0010);
                            else if (dragPiecesArray[b].id == "puzzlePiece4")
                                dragPiecesArray[b].Pb = (new S(111,35)).e(0.0010);
                            G(dragPiecesArray[b], dragPiecesArray[b].Pb)
                        } else
                            F.complete || dragPiecesArray[b].a(dragPiecesArray[b].f.x + c.x, dragPiecesArray[b].f.y + c.y)
                    }
                }
            });
            a.event.stopPropagation()
        }
    }
    function Zg(a) {
        var b = F.D
          , c = C(a).left
          , d = C(a).top;
        if ((a.id == "puzzlePiece7" || a.id == "puzzlePiece4") && c < -20 && d < -20)
            c = -100;
        else {
            C(a);
            C(a);
            C(a);
            C(a);
            var c = new t(a.uh,a.vh)
              , e = ch(a)
              , c = C(e).top
              , g = C(e).bottom
              , d = C(e).left
              , e = C(e).right
              , g = new t(e,g)
              , c = Sa(a, new t(d,c))
              , h = Sa(a, g);
            c.x > h.x ? (d = h.x,
            g = c.x) : (d = c.x,
            g = h.x);
            c.y > h.y ? (e = h.y,
            c = c.y) : (e = c.y,
            c = h.y);
            c = objectBox = new Ca(e,g,c,d);
            d = 0;
            g = F.p * 3;
            e = ch(a);
            e = Sa(a, new t(e.f.x,snapCircle.f.y));
            for (h = 0; h < b.za.length; h++) {
                var m = c
                  , l = b.za[h]
                  , q = m.left <= C(l).left && m.right >= C(l).left
                  , A = m.left >= C(l).left && m.left <= C(l).right
                  , r = m.top <= C(l).top && m.bottom >= C(l).top
                  , m = m.top >= C(l).top && m.top <= C(l).bottom;
                if ((q || A) && (r || m))
                    q = e.x - b.za[h].f.x,
                    A = e.y - b.za[h].f.y,
                    q < 0 && (q *= -1),
                    A < 0 && (A *= -1),
                    q += A,
                    q < g && (g = q,
                    d = h)
            }
            a.W = d;
            if ((d == 0 && Oa(a) == 0 || d == 4 && Oa(a) == 180) && a.id == "virus")
                F.complete = !0,
                dh(a);
            c = new t(b.za[d].f.x - e.x,b.za[d].f.y - e.y)
        }
        return c
    }
    function ch(a) {
        for (var b = 0; b < $d(a); b++)
            if (E(a, b).Ca)
                return snapCircle = E(a, b)
    }
    function Yg() {
        for (var a = dragPiecesArray, b = F.D.va + F.p, c = F.D.va, d = F.D.va, e = F.D.va, g = 0, h = 0, m = 0; m < a.length; m++) {
            var l = a[m];
            g += l.f.x;
            h += l.f.y;
            for (var q = 0; q < $d(l); q++)
                if (E(l, q).u) {
                    var A = E(l, q)
                      , r = new t(A.f.x,A.f.y)
                      , r = Sa(l, r);
                    r.x > r.y ? b > r.y - F.p / 2 && (b = l.id == "puzzlePiece4" && Oa(l) == 90 && (l.W == 20 || l.W == 16 || l.W == 12 || l.W == 8 || l.W == 4 || l.W == 0) ? l.f.x - (C(l).bottom - C(l).top) / 2 : r.y - F.p / 2) : b > r.x - F.p / 2 && (b = l.id == "virus" && (l.W == 20 || l.W == 16 || l.W == 12 || l.W == 8 || l.W == 4) ? l.f.x : (l.id == "puzzlePiece7" && Oa(l) == 0 || l.id == "puzzlePiece4" && Oa(l) == 90) && (l.W == 20 || l.W == 16 || l.W == 12 || l.W == 8 || l.W == 4 || l.W == 0) ? l.f.x - (C(l).right - C(l).left) / 5 : r.x - F.p / 2);
                    F.D.va - r.x > r.y ? c > r.y - F.p / 2 && (c = r.y - F.p / 2) : c > F.D.va - r.x - F.p / 2 && (c = F.D.va - r.x - F.p / 2);
                    r.x > F.D.ob - r.y ? d > F.D.ob - r.y - F.p / 2 && (d = F.D.ob - r.y - F.p / 2) : d > r.x - F.p / 2 && (d = r.x - F.p / 2);
                    F.D.va - r.x > F.D.ob - r.y ? e > F.D.ob - r.y - F.p / 2 && (e = F.D.ob - r.y - F.p / 2) : e > F.D.va - r.x - F.p / 2 && (e = F.D.va - r.x - F.p / 2)
                }
            for (q = 0; q < $d(l); q++)
                if (E(l, q).u)
                    for (var A = E(l, q), X = 0; X < $d(F.q); X++)
                        if (!(eb(a, E(F.q, X)) >= 0))
                            for (var ca = E(F.q, X), cc = 0; cc < $d(ca); cc++)
                                if (E(ca, cc).u) {
                                    var wa = E(ca, cc)
                                      , r = new t(A.f.x,A.f.y)
                                      , r = Sa(l, r)
                                      , wa = Sa(ca, new t(wa.f.x,wa.f.y));
                                    if (r.x > wa.x) {
                                        var ra = r.x - wa.x;
                                        r.y > wa.y ? r.y - ra >= wa.y - 10 && r.y - ra <= wa.y + 10 && b > ra - F.p / 2 && (b = ra - F.p / 2) : r.y + ra >= wa.y - 10 && r.y + ra <= wa.y + 10 && d > ra - F.p / 2 && (d = ra - F.p / 2)
                                    } else
                                        ra = wa.x - r.x,
                                        r.y > wa.y ? r.y - ra >= wa.y - 10 && r.y - ra <= wa.y + 10 && c > ra - F.p / 2 && (c = ra - F.p / 2) : r.y + ra >= wa.y - 10 && r.y + ra <= wa.y + 10 && e > ra - F.p / 2 && (e = ra - F.p / 2)
                                }
        }
        g /= a.length;
        h /= a.length;
        return D((new $g).pe(g - b - 10, h - b - 10, g + c + 10, h - c - 10, g + e + 10, h + e + 10, g - d - 10, h + d + 10).c(100, 100, 100), 0.6)
    }
    function lg(a) {
        return typeof a == "undefined" ? !1 : !0
    }
    function dh(a) {
        F.Cc.play();
        F.Da.stop();
        F.Ae.play();
        var b = mf((new S(-2E3,-2E3)).e(2), rf);
        G(a, b);
        b = new ng(mf((new U(0,0)).e(1), rf),(new og(720)).e(1));
        G(F.rd, b);
        for (var c = 0; c < $d(F.q); c++)
            a = E(F.q, c),
            a.id != "virus" && B(a, !0);
        w(b, T, function() {
            B(F.rd, !0);
            if (F.Ye)
                var a = I["final challenge"]
                  , b = I["challenge completed"];
            else
                a = I["congratulations!"],
                b = I["challenge completed"];
            a = new Ve(a,b,440,440,F.Ye);
            F.q.appendChild(a)
        })
    }
    ;function Z() {
        H.call(this);
        snapAreaInvisible = !0;
        Pe = new bg(gameSpriteImgs[0],Pg)
    }
    s(Z, H);
    Z.j = 100;
    function eh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(300, 150), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece1";
        puzzleImg1 = (new P).c(Pe.m("piece1.png")).a(0, 0);
        touchArea1 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-75, 0), 0.5).c(100, 200, 0);
        touchArea1.type = "touchArea";
        touchArea1.Ca = !0;
        touchArea1.u = !0;
        touchArea2 = D(B((new W).b(Z.j, Z.j), !0).a(75, 0), 0.5).c(100, 200, 0);
        touchArea2.type = "touchArea";
        touchArea2.u = !0;
        touchArea3 = D(B((new P).b(70, 65), !0).a(0, 0), 0.5).c(100, 200, 0);
        touchArea3.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea1);
        a.appendChild(touchArea2);
        a.appendChild(touchArea3);
        a.i = function(a) {
            return touchArea1.i(a) || touchArea2.i(a) || touchArea3.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function fh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(300, 150), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece2";
        puzzleImg1 = (new P).c(Pe.m("piece2.png")).a(0, 0);
        touchArea4 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-75, 0), 0.5).c(100, 200, 0);
        touchArea4.type = "touchArea";
        touchArea4.Ca = !0;
        touchArea4.u = !0;
        touchArea5 = D(B((new W).b(Z.j, Z.j), !0).a(75, 0), 0.5).c(100, 200, 0);
        touchArea5.type = "touchArea";
        touchArea5.u = !0;
        touchArea6 = D(B((new P).b(70, 65), !0).a(0, 0), 0.5).c(100, 200, 0);
        touchArea6.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea4);
        a.appendChild(touchArea5);
        a.appendChild(touchArea6);
        a.i = function(a) {
            return touchArea4.i(a) || touchArea5.i(a) || touchArea6.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function gh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(450, 150), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece3";
        puzzleImg1 = (new P).c(Pe.m("piece3.png")).a(0, 0);
        touchArea7 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-150, 0), 0.5).c(100, 200, 0);
        touchArea7.type = "touchArea";
        touchArea7.Ca = !0;
        touchArea7.u = !0;
        touchArea8 = D(B((new W).b(Z.j, Z.j), !0).a(0, 0), 0.5).c(100, 200, 0);
        touchArea8.type = "touchArea";
        touchArea8.u = !0;
        touchArea9 = D(B((new W).b(Z.j, Z.j), !0).a(150, 0), 0.5).c(100, 200, 0);
        touchArea9.type = "touchArea";
        touchArea9.u = !0;
        touchArea10 = D(B((new P).b(70, 65), !0).a(-75, 0), 0.5).c(100, 200, 0);
        touchArea10.type = "touchArea";
        touchArea11 = D(B((new P).b(70, 65), !0).a(75, 0), 0.5).c(100, 200, 0);
        touchArea11.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea7);
        a.appendChild(touchArea8);
        a.appendChild(touchArea9);
        a.appendChild(touchArea10);
        a.appendChild(touchArea11);
        a.i = function(a) {
            return touchArea7.i(a) || touchArea8.i(a) || touchArea9.i(a) | touchArea10.i(a) | touchArea11.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function hh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(225, 375), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece4";
        puzzleImg1 = (new P).c(Pe.m("piece4.png")).a(0, 0);
        touchArea12 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(37, -112), 0.5).c(100, 200, 100);
        touchArea12.type = "touchArea";
        touchArea12.Ca = !0;
        touchArea12.u = !0;
        touchArea13 = D(B((new W).b(Z.j, Z.j), !0).a(-37, -37), 0.5).c(100, 200, 0);
        touchArea13.type = "touchArea";
        touchArea13.u = !0;
        touchArea14 = D(B((new W).b(Z.j, Z.j), !0).a(-37, 112), 0.5).c(100, 200, 0);
        touchArea14.type = "touchArea";
        touchArea14.u = !0;
        touchArea15 = Nd(D(B((new P).b(80, 100), !0).a(0, -75), 0.5).c(100, 200, 0), 45);
        touchArea15.type = "touchArea";
        touchArea16 = D(B((new P).b(60, 70), !0).a(-37, 40), 0.5).c(100, 200, 0);
        touchArea16.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea12);
        a.appendChild(touchArea13);
        a.appendChild(touchArea14);
        a.appendChild(touchArea15);
        a.appendChild(touchArea16);
        a.i = function(a) {
            return touchArea12.i(a) || touchArea13.i(a) || touchArea14.i(a) | touchArea15.i(a) | touchArea16.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We);
        Zg(a)
    }
    function ih(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(225, 225), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece5";
        puzzleImg1 = (new P).c(Pe.m("piece5.png")).a(0, 0);
        touchArea17 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-37, -37), 0.5).c(100, 200, 0);
        touchArea17.type = "touchArea";
        touchArea17.Ca = !0;
        touchArea17.u = !0;
        touchArea18 = D(B((new W).b(Z.j, Z.j), !0).a(37, 37), 0.5).c(100, 200, 0);
        touchArea18.type = "touchArea";
        touchArea18.u = !0;
        touchArea19 = Nd(D(B((new P).b(Z.j, Z.j), !0).a(0, 0), 0.5).c(100, 200, 0), -45);
        touchArea19.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea17);
        a.appendChild(touchArea18);
        a.appendChild(touchArea19);
        a.i = function(a) {
            return touchArea17.i(a) || touchArea18.i(a) || touchArea19.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function jh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(300, 300), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece6";
        puzzleImg1 = (new P).c(Pe.m("piece6.png")).a(0, 0);
        touchArea20 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(75, 75), 0.5).c(100, 200, 0);
        touchArea20.type = "touchArea";
        touchArea20.Ca = !0;
        touchArea20.u = !0;
        touchArea21 = D(B((new W).b(Z.j, Z.j), !0).a(75, -75), 0.5).c(100, 200, 0);
        touchArea21.type = "touchArea";
        touchArea21.u = !0;
        touchArea22 = D(B((new W).b(Z.j, Z.j), !0).a(-75, 75), 0.5).c(100, 200, 0);
        touchArea22.type = "touchArea";
        touchArea22.u = !0;
        touchArea23 = D(B((new P).b(60, 70), !0).a(75, 0), 0.5).c(100, 200, 0);
        touchArea23.type = "touchArea";
        touchArea24 = D(B((new P).b(70, 60), !0).a(0, 75), 0.5).c(100, 200, 0);
        touchArea24.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea20);
        a.appendChild(touchArea21);
        a.appendChild(touchArea22);
        a.appendChild(touchArea23);
        a.appendChild(touchArea24);
        a.i = function(a) {
            return touchArea20.i(a) || touchArea21.i(a) || touchArea22.i(a) | touchArea23.i(a) | touchArea24.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function kh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(225, 375), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece7";
        puzzleImg1 = (new P).c(Pe.m("piece7.png")).a(0, 0);
        touchArea25 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-37, -112), 0.5).c(100, 200, 0);
        touchArea25.type = "touchArea";
        touchArea25.Ca = !0;
        touchArea25.u = !0;
        touchArea26 = D(B((new W).b(Z.j, Z.j), !0).a(37, -37), 0.5).c(100, 200, 0);
        touchArea26.type = "touchArea";
        touchArea26.u = !0;
        touchArea27 = D(B((new W).b(Z.j, Z.j), !0).a(37, 112), 0.5).c(100, 200, 0);
        touchArea27.type = "touchArea";
        touchArea27.u = !0;
        touchArea28 = Nd(D(B((new P).b(100, 80), !0).a(0, -75), 0.5).c(100, 200, 0), 45);
        touchArea28.type = "touchArea";
        touchArea29 = D(B((new P).b(60, 70), !0).a(37, 37), 0.5).c(100, 200, 0);
        touchArea29.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea25);
        a.appendChild(touchArea26);
        a.appendChild(touchArea27);
        a.appendChild(touchArea28);
        a.appendChild(touchArea29);
        a.i = function(a) {
            return touchArea25.i(a) || touchArea26.i(a) || touchArea27.i(a) | touchArea28.i(a) | touchArea29.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We);
        Zg(a)
    }
    function lh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(225, 300), a);
        a.type = "puzzlePiece";
        a.id = "puzzlePiece8";
        puzzleImg1 = (new P).c(Pe.m("piece8.png")).a(0, 0);
        touchArea30 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-37, -75), 0.5).c(100, 200, 0);
        touchArea30.id = "touchArea30";
        touchArea30.type = "touchArea";
        touchArea30.Ca = !0;
        touchArea30.u = !0;
        touchArea31 = D(B((new W).b(Z.j, Z.j), !0).a(-37, 75), 0.5).c(100, 200, 0);
        touchArea31.type = "touchArea";
        touchArea31.u = !0;
        touchArea31.id = "touchArea31";
        touchArea32 = D(B((new W).b(Z.j, Z.j), !0).a(40, 0), 0.5).c(100, 200, 0);
        touchArea32.type = "touchArea";
        touchArea32.u = !0;
        touchArea32.id = "touchArea32";
        touchArea33 = Nd(D(B((new P).b(105, 80), !0).a(-2, -37), 0.5).c(100, 200, 0), 45);
        touchArea33.type = "touchArea";
        touchArea34 = Nd(D(B((new P).b(80, 105), !0).a(-3, 40), 0.5).c(100, 200, 0), 45);
        touchArea34.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea30);
        a.appendChild(touchArea31);
        a.appendChild(touchArea32);
        a.appendChild(touchArea33);
        a.appendChild(touchArea34);
        a.i = function(a) {
            return touchArea30.i(a) || touchArea31.i(a) || touchArea32.i(a) | touchArea33.i(a) | touchArea34.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function mh(a) {
        var b = F.q
          , a = Nd((new P).a(x, y).b(225, 225), a);
        a.type = "puzzlePiece";
        a.id = "virus";
        puzzleImg1 = (new P).c(Pe.m("virus.png")).a(0, 0);
        touchArea35 = D(B((new W).b(Z.j, Z.j), snapAreaInvisible).a(-37, -37), 0.5).c(100, 200, 100);
        touchArea35.type = "touchArea";
        touchArea35.id = "touchArea35";
        touchArea35.Ca = !0;
        touchArea35.u = !0;
        touchArea36 = D(B((new W).b(Z.j, Z.j), !0).a(37, 37), 0.5).c(100, 200, 0);
        touchArea36.type = "touchArea";
        touchArea36.id = "touchArea36";
        touchArea36.u = !0;
        touchArea37 = Nd(D(B((new P).b(Z.j, Z.j), !0).a(0, 0), 0.5).c(100, 200, 0), -45);
        touchArea37.type = "touchArea";
        a.appendChild(puzzleImg1);
        a.appendChild(touchArea35);
        a.appendChild(touchArea36);
        a.appendChild(touchArea37);
        a.i = function(a) {
            return touchArea35.i(a) || touchArea36.i(a) || touchArea37.i(a) ? !0 : !1
        }
        ;
        b.appendChild(a);
        w(a, ["mousedown", "touchstart"], We)
    }
    function nh() {
        var a = F.q
          , b = (new P).a(x, y).b(150, 150);
        b.type = "block";
        b.id = "block";
        puzzleImg1 = (new P).c(Pe.m("block.png")).a(0, 0);
        touchArea38 = D(B((new W).b(Z.j, Z.j), !0).a(0, 0), 0.5).c(100, 200, 0);
        touchArea38.type = "touchArea";
        touchArea38.id = "touchArea36";
        touchArea38.Ca = !0;
        touchArea38.u = !0;
        b.appendChild(puzzleImg1);
        b.appendChild(touchArea38);
        b.i = ba(!1);
        a.appendChild(b)
    }
    function oh() {
        var a = F.q
          , b = (new P).a(x, y).b(150, 150);
        b.type = "block";
        b.id = "block";
        puzzleImg1 = (new P).c(Pe.m("block.png")).a(0, 0);
        touchArea39 = D(B((new W).b(Z.j, Z.j), !0).a(0, 0), 0.5).c(100, 200, 0);
        touchArea39.type = "touchArea";
        touchArea39.id = "touchArea36";
        touchArea39.Ca = !0;
        touchArea39.u = !0;
        b.appendChild(puzzleImg1);
        b.appendChild(touchArea39);
        b.i = ba(!1);
        a.appendChild(b)
    }
    ;function F(a, b) {
        Q.eb.stop();
        Ja.call(this);
        F.rows = jg[a][b].rows;
        F.cols = jg[a][b].cols;
        var c = parseInt(b) + 1
          , d = a;
        if (Ne == 0 && !Be.Gf)
            switch (c = 1,
            a) {
            case "Starter":
                d = "Junior";
                break;
            case "Junior":
                d = "Expert";
                break;
            case "Expert":
                d = "Master";
                break;
            case "Master":
                d = "END"
            }
        else if (Vf(jg[a]) < c)
            switch (c = 1,
            a) {
            case "Starter":
                d = "Junior";
                break;
            case "Junior":
                d = "Expert";
                break;
            case "Expert":
                d = "Master";
                break;
            case "Master":
                d = "END"
            }
        F.next = c;
        F.Xd = d;
        F.Ye = F.Xd == "END" ? !0 : !1;
        F.p = jg[a][b].boardSquareSize;
        F.Xa = b;
        F.K = a;
        playBackground = (new P).c(J + "backgroundPlay.jpg").b(960, 600).a(0, 0).d(0, 0);
        this.appendChild(playBackground);
        F.rd = (new P).c(J + "backgroundPlayBoard.png").b(ph, qh).a(ph / 2, qh / 2).d(0.5, 0.5);
        this.appendChild(F.rd);
        F.jf = 0;
        rh(this, jg[a][b], a, b);
        F.complete = !1;
        F.Bd = !1;
        F.Bg = (new H).a(0, 0).b(960, 600).d(0, 0);
        this.appendChild(F.Bg);
        sh(this);
        F.Da.wa || (F.Da.reload(),
        F.Da.play())
    }
    s(F, Ja);
    function rh(a, b, c, d) {
        F.D = (new Ng(F.rows,F.cols,F.p)).a(180, 0);
        F.P = (new H).a(0, 0);
        F.q = new Z;
        board = F.D;
        for (var e = 1; e < 12; e++)
            try {
                b["piece" + e].squarePos == -1 ? e == 7 ? (x = -2,
                y = -1) : e == 4 && (x = -1,
                y = -2) : (pos = board.za[b["piece" + e].squarePos].f,
                x = pos.x,
                y = pos.y);
                switch (e) {
                case 1:
                    eh(b["piece" + e].rotation);
                    break;
                case 2:
                    fh(b["piece" + e].rotation);
                    break;
                case 3:
                    gh(b["piece" + e].rotation);
                    break;
                case 4:
                    hh(b["piece" + e].rotation);
                    break;
                case 5:
                    ih(b["piece" + e].rotation);
                    break;
                case 6:
                    jh(b["piece" + e].rotation);
                    break;
                case 7:
                    kh(b["piece" + e].rotation);
                    break;
                case 8:
                    lh(b["piece" + e].rotation);
                    break;
                case 9:
                    mh(b["piece" + e].rotation);
                    virus = th("virus");
                    pos = uh(virus);
                    virus.a(pos.x, pos.y);
                    break;
                case 10:
                    nh();
                    break;
                case 11:
                    oh()
                }
                e < 9 && (piece = th("puzzlePiece" + e),
                pos = uh(piece),
                piece.a(pos.x, pos.y))
            } catch (g) {}
        F.D.appendChild(F.q);
        a.appendChild(F.D);
        a.appendChild(F.P);
        var h = (new P).a(884, 556).c(Me + "btnPause.png").d(0.5, 0.5);
        F.Ma = !1;
        w(h, ["mousedown", "touchstart"], function(a) {
            F.$f || (h.l(1.1),
            F.mf.reload(),
            F.mf.play(),
            a.w(["mouseup", "touchend"], function() {
                h.l(1);
                if (!F.Qf)
                    if (F.P.f.y == 0 && !F.Ma)
                        F.Ma = !0,
                        moveToPause = (new Lf(0,-600)).e(0.8),
                        G(F.P, moveToPause),
                        G(F.D, moveToPause),
                        w(moveToPause, T, function() {
                            F.Ma = !1
                        });
                    else if (F.P.f.y == -600 && !F.Ma)
                        F.startTime = new Date,
                        F.Ma = !0,
                        moveToGame = (new Lf(0,600)).e(0.8),
                        G(F.P, moveToGame),
                        G(F.D, moveToGame),
                        w(moveToGame, T, function() {
                            F.Ma = !1
                        })
            }))
        });
        a.appendChild(h);
        var m = (new P).a(80, 556).c(Me + "btnReset.png").d(0.5, 0.5);
        a.appendChild(m);
        w(m, ["mousedown", "touchstart"], function(a) {
            F.P.f.y == 0 && !F.$f && (m.l(1.1),
            F.tf.reload(),
            F.tf.play(),
            a.w(["mouseup", "touchend"], function() {
                m.l(1);
                if (!F.Qf) {
                    O.X(chrono, F);
                    var a = new F(F.K,F.Xa);
                    R(a);
                    F.Ic = 0;
                    F.hd.g("00:00")
                }
            }))
        });
        vh(c, d);
        b = ig.ng();
        a.appendChild(b);
        b.l(0.8);
        b = ig.mg(Me, F.K, F.Xa, 882, 53);
        a.appendChild(b);
        b.l(0.75)
    }
    function th(a) {
        for (j = 0; j < $d(F.q); j++)
            if (E(F.q, j).id == a)
                return E(F.q, j)
    }
    function uh(a) {
        yOffset = xOffset = 0;
        var b = ch(a);
        xOffset = b.f.x;
        yOffset = b.f.y;
        if ((a.id == "puzzlePiece1" || a.id == "puzzlePiece2") && (Oa(a) == 90 || Oa(a) == 270))
            xOffset = 0,
            yOffset = -(C(a).right - C(a).left) / 2;
        if (a.id == "puzzlePiece3" && (Oa(a) == 90 || Oa(a) == 270))
            xOffset = 0,
            yOffset = -F.p;
        if (a.id == "puzzlePiece4" && (Oa(a) == 90 || Oa(a) == 270))
            xOffset = -F.p * 0.75,
            yOffset = +F.p / 4;
        if (a.id == "puzzlePiece7" && (Oa(a) == 90 || Oa(a) == 270))
            xOffset = -F.p * 0.75,
            yOffset = -F.p / 4;
        if (a.id == "puzzlePiece8" && (Oa(a) == 90 || Oa(a) == 270))
            xOffset = -F.p / 2,
            yOffset = -F.p / 4;
        Oa(a) == 0 ? (x = a.f.x - xOffset,
        y = a.f.y - yOffset) : Oa(a) == 90 ? (x = a.f.x - xOffset,
        y = a.f.y + yOffset) : Oa(a) == 180 ? (x = a.f.x + xOffset,
        y = a.f.y + yOffset) : Oa(a) == 270 && (x = a.f.x + xOffset,
        y = a.f.y - yOffset);
        return {
            x: x,
            y: y
        }
    }
    function vh(a, b) {
        var c = (new P).c(J + "popupPause.png").b(560, 560).a(480, 900);
        F.P.appendChild(c);
        resumebtn = (new Bg(I.resume,"iconResume.png")).a(480, 740);
        w(resumebtn, ["mousedown", "touchstart"], function(a) {
            resumebtn.l(1.1);
            F.Cc.play();
            a.w(["mouseup", "touchend"], function() {
                resumebtn.l(1);
                if (!F.Ma)
                    F.Ma = !0,
                    moveToGame = (new Lf(0,600)).e(0.8),
                    G(F.P, moveToGame),
                    G(F.D, moveToGame),
                    w(moveToGame, T, function() {
                        F.Ma = !1
                    })
            })
        });
        F.P.appendChild(resumebtn);
        if (He == "all") {
            var d = (new Bg(I.home,"iconHome.png")).a(480, 820);
            w(d, ["mousedown", "touchstart"], function(a) {
                d.l(1.1);
                a.w(["mouseup", "touchend"], function() {
                    O.X(chrono, F);
                    var a = new Q;
                    De ? R(a) : R(a, df, 0.5)
                })
            });
            F.P.appendChild(d)
        } else {
            var e = (new P).c(Me + "buttons/iconStarter.png").a(380, 820);
            F.P.appendChild(e);
            w(e, ["mousedown", "touchstart"], function(a) {
                He = "Starter";
                e.l(1.1);
                a.w(["mouseup", "touchend"], function() {
                    O.X(chrono, F);
                    var a = new Q(!1,"Starter");
                    De ? R(a) : R(a, df, 0.5)
                })
            });
            var g = (new P).c(Me + "buttons/iconJunior.png").a(450, 820);
            F.P.appendChild(g);
            w(g, ["mousedown", "touchstart"], function(a) {
                g.l(1.1);
                He = "Junior";
                a.w(["mouseup", "touchend"], function() {
                    O.X(chrono, F);
                    var a = new Q(!1,"Junior");
                    De ? R(a) : R(a, df, 0.5)
                })
            });
            var h = (new P).c(Me + "buttons/iconExpert.png").a(520, 820);
            F.P.appendChild(h);
            w(h, ["mousedown", "touchstart"], function(a) {
                He = "Expert";
                h.l(1.1);
                a.w(["mouseup", "touchend"], function() {
                    O.X(chrono, F);
                    var a = new Q(!1,"Expert");
                    De ? R(a) : R(a, df, 0.5)
                })
            });
            var m = (new P).c(Me + "buttons/iconMaster.png").a(590, 820);
            F.P.appendChild(m);
            w(m, ["mousedown", "touchstart"], function(a) {
                m.l(1.1);
                He = "Master";
                a.w(["mouseup", "touchend"], function() {
                    O.X(chrono, F);
                    var a = new Q(!1,"Master");
                    De ? R(a) : R(a, df, 0.5)
                })
            })
        }
        soundOnIcon = (new Bg(I.sound.replace(":", ""),"iconSoundOn.png")).a(480, 900);
        w(soundOnIcon, ["mousedown", "touchstart"], function() {
            F.Cc.play();
            fg(soundOnIcon, F.Lb)
        });
        F.P.appendChild(soundOnIcon);
        soundOffIcon = (new Bg(I.sound.replace(":", ""),"iconSoundOff.png")).a(480, 900);
        w(soundOffIcon, ["mousedown", "touchstart"], function() {
            F.Cc.play();
            fg(soundOffIcon, F.Lb)
        });
        F.P.appendChild(soundOffIcon);
        Qe ? (D(soundOnIcon, 1),
        D(soundOffIcon, 0)) : (D(soundOnIcon, 0),
        D(soundOffIcon, 1));
        helpbtn = (new Bg(I.help,"iconHelp.png")).a(480, 980);
        w(helpbtn, ["mousedown", "touchstart"], function(a) {
            helpbtn.l(1.1);
            F.Cc.play();
            a.w(["mouseup", "touchend"], function() {
                helpbtn.l(1);
                O.X(chrono, F);
                var a = new Y(!0);
                R(a)
            })
        });
        F.P.appendChild(helpbtn);
        moreBtn = (new Bg(I.more,"iconMore.png")).a(480, 1060);
        w(moreBtn, ["mousedown", "touchstart"], function(c) {
            moreBtn.l(1.1);
            c.w(["mouseup", "touchend"], function() {
                O.X(chrono, F);
                moreBtn.l(1);
                var c = new gf(!0,a,b);
                R(c)
            })
        });
        F.P.appendChild(moreBtn)
    }
    F.Lb = function() {
        Qe ? (localStorage.setItem("av.soundSetting", !1),
        F.Da.stop(),
        Qe = !1,
        D(soundOnIcon, 0),
        D(soundOffIcon, 1)) : (localStorage.setItem("av.soundSetting", !0),
        Qe = !0,
        F.Da.reload(),
        F.Da.play(),
        D(soundOnIcon, 1),
        D(soundOffIcon, 0))
    }
    ;
    function sh(a) {
        if (localStorage.getItem("av.1stTime") == k && Re == k) {
            try {
                localStorage.setItem("av.1stTime", !1),
                Re = !1
            } catch (b) {
                Re = !1
            }
            F.o = (new P).c(J + "popupBlank.png").a(480, 480).d(0.5, 0.5).b(580, 580);
            F.o.Zf = M(L(K((new N(I.gameRules)).b(320, 120), 40).a(0, -150), "#fff"), "futuraBold").d(0.5, 0.5);
            F.o.appendChild(F.o.Zf);
            F.o.cg = M(L(K((new N(I["this is the first time..."])).b(460, 300), 20).a(0, 0), "#fff"), "futura").d(0.5, 0.5);
            F.o.appendChild(F.o.cg);
            F.o.Ng = af(M(L(K((new N(I.step1)).b(440, 350), 24).a(0, 70), "#fff"), "futuraBold"), "left");
            F.o.appendChild(F.o.Ng);
            F.o.Mg = af(M(L(K((new N(I["step1..."])).b(440, 350), 20).a(0, 100), "#fff"), "futura"), "left");
            F.o.appendChild(F.o.Mg);
            F.o.Pg = af(M(L(K((new N(I.step2)).b(440, 350), 24).a(0, 210), "#fff"), "futuraBold"), "left");
            F.o.appendChild(F.o.Pg);
            F.o.Og = af(M(L(K((new N(I["step2..."])).b(440, 350), 20).a(0, 240), "#fff"), "futura"), "left");
            F.o.appendChild(F.o.Og);
            F.o.$c = ef(I["continue"]).a(140, 195);
            w(F.o.$c, ["mousedown", "touchstart"], f = function(a) {
                F.o.$c.l(1.1);
                a.w(["mouseup", "touchend"], function() {
                    F.o.$c.l(1);
                    F.o.Pb = (new S(480,-300)).e(1);
                    G(F.o, F.o.Pb)
                })
            }
            );
            F.o.appendChild(F.o.$c);
            F.o.Yc = ef(I["more info"]).a(-85, 195);
            w(F.o.Yc, ["mousedown", "touchstart"], f = function(a) {
                F.o.Yc.l(1.1);
                a.w(["mouseup", "touchend"], function() {
                    O.X(chrono, F);
                    F.o.Yc.l(1);
                    var a = new Y(!0);
                    R(a)
                })
            }
            );
            F.o.appendChild(F.o.Yc);
            D(F.o, 0);
            F.o.Lf = (new V(1)).e(0.3);
            G(F.o, F.o.Lf);
            F.o.a(480, -300);
            a.appendChild(F.o);
            De ? F.o.a(480, 300) : (F.o.Pb = (new S(480,300)).e(1),
            G(F.o, F.o.Pb))
        }
    }
    ;function $(a) {
        function b() {
            var a = (new S(ph / 2,782)).e(0.5);
            G($.sa, a)
        }
        Ja.call(this);
        scoresPopupShowed = $.ye = !1;
        Q.eb.wa || (lg(F.Da) && F.Da.stop(),
        Q.eb.reload(),
        Q.eb.play());
        if (a == "Expert" || a == "Master") {
            numLevels = 0;
            var c = K(L(M(new N, "futuraBold"), "#fff"), 24).b(400, -160).B("rgba(0,0,0,0.4)", 2, 2, 2);
            c.a(650, 115);
            a == "Expert" && c.g("Do you want to become a real SmartGames expert? Buy the original game now!");
            a == "Master" && c.g("Do you want to become a real SmartGames master? Buy the original game now!");
            var d = (new P).c(J + "add2Cart.png").b(222, 59).a(650, 340).d(0.5, 0.5);
            w(d, ["mousedown", "touchstart"], function() {
                window.location.href = window.getcartLink()
            });
            levelselectBackground = (new P).c(J + "bgAdverGame.jpg").b(960, 600).a(0, 0).d(0, 0);
            moreBtn = (new cf(I.more,"iconMore.png")).a(830, 550);
            w(moreBtn, ["mouseup", "touchend"], function() {
                $.n.play();
                $.Ed()
            });
            var e = 0;
            a == "Expert" ? e = -1650 : a == "Master" && (e = -1735);
            var g = (new P).c(Ie.m("selectLevelCircle.png")).d(0.5, 0.5).a(650, 120).l(0.4)
              , h = (new P).c(Ie.m("levelSelectIndicatorArrow.png")).d(0.5, 0.496).a(650, 119).l(0.4)
              , e = (new og(e + -15)).e(1.25);
            G(h, e)
        } else
            numLevels = Vf(jg[a]),
            c = new N,
            levelselectBackground = (new P).c(J + "bgLevelSelect.jpg").b(960, 600).a(0, 0).d(0, 0);
        this.appendChild(levelselectBackground);
        this.appendChild(c);
        lg(d) && (this.appendChild(d),
        this.appendChild(moreBtn),
        this.appendChild(g),
        this.appendChild(h));
        btnsPerPage = 10;
        numLevels < btnsPerPage && (btnsPerPage = numLevels);
        $.Kc = (new H).a(120, 330);
        this.appendChild($.Kc);
        col = row = 0;
        $.Yd = Math.round(numLevels / btnsPerPage) == 0 ? 1 : Math.ceil(numLevels / btnsPerPage);
        $.Ha = 1;
        levelsInGroup = 0;
        var m = 1
          , l = Vf(jg[a]);
        l > btnsPerPage && (l = $.Ha * btnsPerPage);
        wh(m, l, $.Ha, a);
        $.Re = 1;
        $.Z = (new P).c(Me + "levelSelectArrow.png").b(47, 81).a(885, 265).d(0, 0);
        w($.Z, ["mousedown", "touchstart"], function() {
            $.Sb.reload();
            $.Sb.play();
            m = previousEnd;
            l = m + (btnsPerPage - 1);
            l > numLevels && (l = numLevels);
            $.Re < $.Ha + 1 && wh(m, l, $.Ha + 1, a);
            $.Fd()
        });
        a != "Expert" && a != "Master" && this.appendChild($.Z);
        $.Yd == 1 && B($.Z, !0);
        $.S = Nd((new P).c(Me + "levelSelectArrow.png").b(47, 81).a(70, 353).d(0, 0), 180);
        w($.S, ["mousedown", "touchstart"], function() {
            $.Sb.reload();
            $.Sb.play();
            $.Gd()
        });
        this.appendChild($.S);
        B($.S, !0);
        He == "all" ? a != "Expert" && a != "Master" && (c = (new cf(I.home,"iconHome.png")).a(190, 530),
        w(c, ["mousedown", "touchstart"], function() {
            $.Sb.play();
            var a = new Q;
            De ? R(a) : R(a, df)
        }),
        this.appendChild(c)) : a != "Expert" && a != "Master" && (c = (new cf(I.home,"icon" + He + ".png")).a(190, 530),
        w(c, ["mousedown", "touchstart"], function() {
            $.Sb.play();
            var a = new Q(!1,He);
            De ? R(a) : R(a, df)
        }),
        this.appendChild(c));
        a != "Expert" && a != "Master" && (btnScoresSelect = (new Cg).a(788, 530),
        this.appendChild(btnScoresSelect));
        $.sa = (new P).a(ph / 2, 782).c(100, 100, 100);
        popUpRect = (new P).c(J + "popupBlank.png").a(0, 120);
        $.sa.appendChild(popUpRect);
        textLabel = K(L(M(new N, "futura"), "#fff"), 16).b(470, 50);
        textLabel.a(0, -80);
        $.sa.appendChild(textLabel);
        var q = (new ef(I.close)).a(0, 245);
        w(q, ["mousedown", "touchstart"], function() {
            Q.n.play();
            fg(q, b)
        });
        $.sa.appendChild(q);
        c = (new ef(I.register)).a(25, 175);
        $.sa.appendChild(c);
        w(c, ["mousedown", "touchstart"], function() {
            Q.n.play();
            window.goToRegister()
        });
        this.appendChild($.sa);
        groupIsMoving = !1;
        scoresPopup = Wf.df($.Oc);
        this.appendChild(scoresPopup)
    }
    s($, Ja);
    $.Uf = function(a, b) {
        if (!groupIsMoving) {
            var c = new F(a,b);
            De ? R(c) : R(c, df, 0.5)
        }
    }
    ;
    $.Ed = function() {
        var a = new gf(!1);
        De ? R(a) : R(a, df, 0.5)
    }
    ;
    $.Oc = function() {
        scoresPopupShowed == !1 ? O.Db(function() {
            scoresPopup.h = (new S(0,85)).e(0.3);
            G(scoresPopup, scoresPopup.h);
            scoresPopupShowed = !0
        }, this, 0, 1) : (scoresPopup.h = (new S(0,-600)).e(0.3),
        G(scoresPopup, scoresPopup.h),
        scoresPopupShowed = !1)
    }
    ;
    function wh(a, b, c, d) {
        for (; a <= b; a++)
            levelsInGroup == btnsPerPage && (row = col = levelsInGroup = 0),
            minStarsChallenge = jg[d][a].minStars,
            locked = jg[d][a].locked,
            btn = new Ag(a,d,minStarsChallenge,kg(a, d)),
            btn.a(col * 185 + 70 + (c - 1) * 960, row * 140 - 40).l(1.5),
            btn.K = d,
            btn.Xa = a,
            btn.gg ? w(btn, ["mousedown", "touchstart"], function(a) {
                scoresPopupShowed || xh(a.target.rg)
            }) : w(btn, ["mousedown", "touchstart"], function(a) {
                if (!scoresPopupShowed && !$.ye)
                    $.ye = !0,
                    $.n.play(),
                    yh(a.target, function() {
                        $.Uf(a.target.K, a.target.Xa)
                    })
            }),
            col += 1,
            levelsInGroup += 1,
            col == 5 && (col = 0,
            row += 1),
            $.Kc.appendChild(btn);
        previousEnd = a;
        $.Re += 1
    }
    $.Fd = function() {
        $.Ha < $.Yd && !groupIsMoving && (groupIsMoving = !0,
        moveToNext = (new Lf(-960,0)).e(0.8),
        G($.Kc, moveToNext),
        fade = (new V(0.2)).e(0.4),
        G($.Z, fade),
        G($.S, fade),
        w(moveToNext, T, function() {
            groupIsMoving = !1;
            fadeBack = (new V(1)).e(0.3);
            G($.Z, fadeBack);
            G($.S, fadeBack);
            w(fadeBack, T, function() {
                B($.S, !1)
            })
        }),
        $.Ha += 1);
        $.Ha == $.Yd && B($.Z, !0)
    }
    ;
    $.Gd = function() {
        if ($.Ha > 1 && !groupIsMoving)
            groupIsMoving = $.S.gh = !0,
            moveToPrev = (new Lf(960,0)).e(0.8),
            G($.Kc, moveToPrev),
            fade = (new V(0.2)).e(0.4),
            G($.S, fade),
            G($.Z, fade),
            w(moveToPrev, T, function() {
                groupIsMoving = !1;
                fadeBack = (new V(1)).e(0.3);
                G($.S, fadeBack);
                G($.Z, fadeBack);
                w(fadeBack, T, function() {
                    B($.Z, !1)
                })
            }),
            $.Ha -= 1;
        $.Ha == 1 && B($.S, !0)
    }
    ;
    function xh(a) {
        try {
            O.X(slide, this)
        } catch (b) {}
        Ne == 0 ? ($.sa.l(0.9),
        K(E($.sa, 1).g(I["Register sgl"]), 24).a(0, 70).b(300, 200),
        slideOutPopUp = (new S(ph / 2,190)).e(0.5),
        G($.sa, slideOutPopUp)) : (E($.sa, 1).g(a + " " + I["stars needed"]),
        slideOutPopUp = (new S(ph / 2,662)).e(0.5),
        G($.sa, slideOutPopUp),
        O.Db(slide = function() {
            slideBackPopUp = (new S(ph / 2,782)).e(0.5);
            G($.sa, slideBackPopUp)
        }
        , this, 2E3))
    }
    function Vf(a) {
        var b = 0, c;
        for (c in a)
            a.hasOwnProperty(c) && b++;
        return b
    }
    function lg(a) {
        return typeof a == "undefined" ? !1 : !0
    }
    ;var Ch = {
        pg: function(a, b) {
            var c = (new H).a(0, -600).b(450, 450).d(0, 0)
              , d = (new Xe).c(J + "popupBlank.png").b(430, 430).a(480, 276);
            c.appendChild(d);
            d = M(L(K(new N, 25).g(I.settings), "#fff"), "futuraBold").a(480, 140).b(300, 40);
            c.appendChild(d);
            var e = (new cf(I.close)).a(498, 405);
            w(e, ["mousedown", "touchstart"], function() {
                Q.n.play();
                Uf(e, Q.Hd)
            });
            e.l(0.7);
            c.appendChild(e);
            soundOnIcon = (new cf(I.sound.replace(":", ""),"iconSoundOn.png")).a(470, 190).l(0.75);
            w(soundOnIcon, ["mousedown", "touchstart"], function() {
                Q.n.play();
                zh(soundOnIcon)
            });
            c.appendChild(soundOnIcon);
            soundOnIcon.l(0.65);
            soundOffIcon = (new cf(I.sound.replace(":", ""),"iconSoundOff.png")).a(470, 190).l(0.75);
            w(soundOffIcon, ["mousedown", "touchstart"], function() {
                Q.n.play();
                zh(soundOffIcon)
            });
            c.appendChild(soundOffIcon);
            soundOffIcon.l(0.65);
            Qe ? (Q.eb.play(),
            D(soundOnIcon, 1),
            D(soundOffIcon, 0),
            D(b, 1),
            D(a, 0)) : (D(soundOnIcon, 0),
            D(soundOffIcon, 1),
            D(b, 0),
            D(a, 1));
            for (var d = Object.keys(Ah), g = 0, h = 0, m = 0; m < d.length; m++) {
                var l = d[m]
                  , q = (new Dg(l.toUpperCase(),"icon" + l.toUpperCase() + ".jpg")).a(338 + h * 122, 270 + g * 60).l(0.8);
                q.language = l;
                w(q, ["mousedown", "touchstart"], function(a) {
                    Bh(a.target)
                });
                c.appendChild(q);
                h < 2 ? h += 1 : (h = 0,
                g += 1)
            }
            return c
        }
    };
    s(Ch, Ja);
    var Dh = {
        data: ba('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict><key>frames</key><dict><key>iconCZ.jpg</key><dict><key>x</key><real>350</real><key>y</key><real>137</real><key>width</key><real>39</real><key>height</key><real>26</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>39</real><key>originalHeight</key><real>26</real></dict><key>iconDE.jpg</key><dict><key>x</key><real>348</real><key>y</key><real>168</real><key>width</key><real>40</real><key>height</key><real>24</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>40</real><key>originalHeight</key><real>24</real></dict><key>iconEN.jpg</key><dict><key>x</key><real>283</real><key>y</key><real>205</real><key>width</key><real>39</real><key>height</key><real>24</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>39</real><key>originalHeight</key><real>24</real></dict><key>iconES.jpg</key><dict><key>x</key><real>241</real><key>y</key><real>180</real><key>width</key><real>40</real><key>height</key><real>29</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>40</real><key>originalHeight</key><real>29</real></dict><key>iconExpert.png</key><dict><key>x</key><real>70</real><key>y</key><real>0</real><key>width</key><real>68</real><key>height</key><real>68</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconExpertHome.png</key><dict><key>x</key><real>136</real><key>y</key><real>70</real><key>width</key><real>65</real><key>height</key><real>65</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>67</real><key>originalHeight</key><real>67</real></dict><key>iconFR.jpg</key><dict><key>x</key><real>348</real><key>y</key><real>194</real><key>width</key><real>40</real><key>height</key><real>24</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>40</real><key>originalHeight</key><real>24</real></dict><key>iconHelp.png</key><dict><key>x</key><real>241</real><key>y</key><real>137</real><key>width</key><real>30</real><key>height</key><real>41</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>30</real><key>originalHeight</key><real>41</real></dict><key>iconHome.png</key><dict><key>x</key><real>280</real><key>y</key><real>0</real><key>width</key><real>67</real><key>height</key><real>67</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>67</real><key>originalHeight</key><real>67</real></dict><key>iconJunior.png</key><dict><key>x</key><real>140</real><key>y</key><real>0</real><key>width</key><real>68</real><key>height</key><real>68</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconJuniorHome.png</key><dict><key>x</key><real>0</real><key>y</key><real>138</real><key>width</key><real>65</real><key>height</key><real>65</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>67</real><key>originalHeight</key><real>67</real></dict><key>iconMaster.png</key><dict><key>x</key><real>210</real><key>y</key><real>0</real><key>width</key><real>68</real><key>height</key><real>68</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconMasterHome.png</key><dict><key>x</key><real>203</real><key>y</key><real>70</real><key>width</key><real>65</real><key>height</key><real>65</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>67</real><key>originalHeight</key><real>67</real></dict><key>iconMore.png</key><dict><key>x</key><real>67</real><key>y</key><real>185</real><key>width</key><real>44</real><key>height</key><real>44</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>44</real><key>originalHeight</key><real>44</real></dict><key>iconNL.jpg</key><dict><key>x</key><real>152</real><key>y</key><real>204</real><key>width</key><real>40</real><key>height</key><real>25</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>40</real><key>originalHeight</key><real>25</real></dict><key>iconNextExpert.png</key><dict><key>x</key><real>0</real><key>y</key><real>70</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconNextJunior.png</key><dict><key>x</key><real>68</real><key>y</key><real>70</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconNextMaster.png</key><dict><key>x</key><real>349</real><key>y</key><real>0</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconNextStarter.png</key><dict><key>x</key><real>280</real><key>y</key><real>69</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconRO.jpg</key><dict><key>x</key><real>39</real><key>y</key><real>231</real><key>width</key><real>40</real><key>height</key><real>25</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>40</real><key>originalHeight</key><real>25</real></dict><key>iconRU.jpg</key><dict><key>x</key><real>308</real><key>y</key><real>137</real><key>width</key><real>40</real><key>height</key><real>29</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>40</real><key>originalHeight</key><real>29</real></dict><key>iconReplayExpert.png</key><dict><key>x</key><real>416</real><key>y</key><real>68</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconReplayJunior.png</key><dict><key>x</key><real>416</real><key>y</key><real>136</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconReplayMaster.png</key><dict><key>x</key><real>348</real><key>y</key><real>69</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconReplayStarter.png</key><dict><key>x</key><real>417</real><key>y</key><real>0</real><key>width</key><real>66</real><key>height</key><real>66</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconResume.png</key><dict><key>x</key><real>273</real><key>y</key><real>137</real><key>width</key><real>33</real><key>height</key><real>36</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>33</real><key>originalHeight</key><real>36</real></dict><key>iconScore.png</key><dict><key>x</key><real>0</real><key>y</key><real>205</real><key>width</key><real>37</real><key>height</key><real>46</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>37</real><key>originalHeight</key><real>46</real></dict><key>iconSettings.png</key><dict><key>x</key><real>308</real><key>y</key><real>168</real><key>width</key><real>38</real><key>height</key><real>35</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>38</real><key>originalHeight</key><real>35</real></dict><key>iconSoundOff.png</key><dict><key>x</key><real>203</real><key>y</key><real>184</real><key>width</key><real>29</real><key>height</key><real>35</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>29</real><key>originalHeight</key><real>35</real></dict><key>iconSoundOn.png</key><dict><key>x</key><real>67</real><key>y</key><real>138</real><key>width</key><real>51</real><key>height</key><real>45</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>51</real><key>originalHeight</key><real>45</real></dict><key>iconStarter.png</key><dict><key>x</key><real>0</real><key>y</key><real>0</real><key>width</key><real>68</real><key>height</key><real>68</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>68</real><key>originalHeight</key><real>68</real></dict><key>iconStarterHome.png</key><dict><key>x</key><real>136</real><key>y</key><real>137</real><key>width</key><real>65</real><key>height</key><real>65</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>67</real><key>originalHeight</key><real>67</real></dict><key>star.png</key><dict><key>x</key><real>113</real><key>y</key><real>204</real><key>width</key><real>37</real><key>height</key><real>35</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>39</real><key>originalHeight</key><real>37</real></dict><key>trophy.png</key><dict><key>x</key><real>203</real><key>y</key><real>137</real><key>width</key><real>36</real><key>height</key><real>45</real><key>offsetX</key><real>0</real><key>offsetY</key><real>-0</real><key>originalWidth</key><real>38</real><key>originalHeight</key><real>47</real></dict></dict><key>texture</key><dict><key>width</key><integer>512</integer><key>height</key><integer>256</integer></dict></dict></plist>')
    };
    function Q(a, b) {
        Oe = new bg(sglSpriteImgs[2],Dh);
        Ja.call(this);
        scoresPopupShowed = settingsPopupShowed = popupShown = !1;
        minStarsArray = [0, 0, 0, 0];
        this.appendChild((new P).c(J + "bgHomeScreen.jpg").b(960, 600).a(0, 0).d(0, 0));
        levelSelectorHomeScreen = b == k ? ig.og(Me, minStarsArray) : ig.lg(Me, b);
        this.appendChild(levelSelectorHomeScreen);
        settingsBtn = (new cf(I.settings,"iconSettings.png")).a(460, 755);
        w(settingsBtn, ["mousedown", "touchstart"], function() {
            Uf(settingsBtn, Q.Hd)
        });
        this.appendChild(settingsBtn);
        helpBtn = (new cf(I.help,"iconHelp.png")).a(460, 755);
        w(helpBtn, ["mousedown", "touchstart"], function(a) {
            helpBtn.l(1.1);
            Q.n.play();
            a.w(["mouseup", "touchend"], function() {
                helpBtn.l(1);
                var a = new Y;
                R(a)
            })
        });
        this.appendChild(helpBtn);
        moreBtn = (new cf(I.more,"iconMore.png")).a(460, 755);
        w(moreBtn, ["mouseup", "touchend"], function() {
            Q.n.play();
            Q.Ed()
        });
        this.appendChild(moreBtn);
        soundOnbtn = (new P).c(Me + "btnSpeakerOn.png").b(60, 50).a(40, 30).d(0.5, 0.5);
        w(soundOnbtn, ["mousedown", "touchstart"], function() {
            Q.n.play();
            Uf(soundOnbtn, Q.Lb)
        });
        this.appendChild(soundOnbtn);
        soundOffbtn = (new P).c(Me + "btnSpeakerOff.png").b(60, 50).a(40, 30).d(0.5, 0.5);
        w(soundOffbtn, ["mousedown", "touchstart"], function() {
            Q.n.play();
            Uf(soundOffbtn, Q.Lb)
        });
        this.appendChild(soundOffbtn);
        settingsPopup = Ch.pg(soundOffbtn, soundOnbtn);
        this.appendChild(settingsPopup);
        scoresPopup = Wf.df(Q.Oc);
        this.appendChild(scoresPopup);
        a ? (smartWaveUp = (new P).c(Me + "smartWaveUp.png").b(960, 341).a(0, 0).d(0, 0),
        this.appendChild(smartWaveUp),
        smartWaveDown = (new P).c(Me + "smartWaveDown.png").b(960, 340).a(0, 260).d(0, 0),
        this.appendChild(smartWaveDown),
        moveSmartWaveUp = (new S(0,-400)).e(1),
        moveSmartWaveDown = (new S(0,1E3)).e(1.4),
        G(smartWaveUp, moveSmartWaveUp),
        G(smartWaveDown, moveSmartWaveDown),
        w(moveSmartWaveUp, T, function() {
            Eh()
        })) : Eh()
    }
    function Eh() {
        De ? (settingsBtn.a(190, 530),
        helpBtn.a(490, 530),
        moreBtn.a(788, 530),
        D(levelSelectorHomeScreen, 1),
        levelSelectorHomeScreen.a(0, 20),
        D(btnHomeScreenStarter, 1),
        btnHomeScreenStarter.a(260, 330),
        D(btnHomeScreenJunior, 1),
        btnHomeScreenJunior.a(260, 240),
        D(btnHomeScreenExpert, 1),
        btnHomeScreenExpert.a(700, 240),
        D(btnHomeScreenMaster, 1),
        btnHomeScreenMaster.a(700, 330)) : He == "all" ? (settingsBtn.moveTo = (new S(190,530)).e(0.3),
        G(settingsBtn, settingsBtn.moveTo),
        helpBtn.moveTo = (new S(490,530)).e(0.3),
        G(helpBtn, helpBtn.moveTo),
        moreBtn.moveTo = (new S(788,530)).e(0.3),
        G(moreBtn, moreBtn.moveTo),
        levelSelectorHomeScreen.h = new Sf((new V(1)).e(0.25),(new S(0,20)).e(0.6)),
        G(levelSelectorHomeScreen, levelSelectorHomeScreen.h),
        w(levelSelectorHomeScreen.h, T, function() {
            btnHomeScreenStarter.h = new Sf((new V(1)).e(0.01),(new S(260,330)).e(0.35));
            G(btnHomeScreenStarter, btnHomeScreenStarter.h);
            btnHomeScreenJunior.h = new Sf((new V(1)).e(0.15),(new S(260,240)).e(0.35));
            G(btnHomeScreenJunior, btnHomeScreenJunior.h);
            btnHomeScreenExpert.h = new Sf((new V(1)).e(0.3),(new S(700,240)).e(0.35));
            G(btnHomeScreenExpert, btnHomeScreenExpert.h);
            btnHomeScreenMaster.h = new Sf((new V(1)).e(0.45),(new S(700,330)).e(0.35));
            G(btnHomeScreenMaster, btnHomeScreenMaster.h);
            w(btnHomeScreenMaster.h, T, function() {
                levelSelectIndicatorArrow.h = (new gg(levelRotation)).e(0.5);
                G(levelSelectIndicatorArrow, levelSelectIndicatorArrow.h)
            })
        })) : (levelSelectorHomeScreen.h = new Sf((new V(1)).e(0.25),(new S(0,60)).e(0.6)),
        G(levelSelectorHomeScreen, levelSelectorHomeScreen.h),
        w(levelSelectorHomeScreen.h, T, function() {
            btnHomeScreenStarter.h = new Sf((new V(1)).e(0.01),new ng((new U(1)).e(0.35),(new S(330,290)).e(0.35)));
            G(btnHomeScreenStarter, btnHomeScreenStarter.h);
            btnHomeScreenJunior.h = new Sf((new V(1)).e(0.15),new ng((new U(1)).e(0.35),(new S(330,210)).e(0.35)));
            G(btnHomeScreenJunior, btnHomeScreenJunior.h);
            btnHomeScreenExpert.h = new Sf((new V(1)).e(0.3),new ng((new U(1)).e(0.35),(new S(630,210)).e(0.35)));
            G(btnHomeScreenExpert, btnHomeScreenExpert.h);
            btnHomeScreenMaster.h = new Sf((new V(1)).e(0.45),new ng((new U(1)).e(0.35),(new S(630,290)).e(0.35)));
            G(btnHomeScreenMaster, btnHomeScreenMaster.h);
            levelBtnLayer.Cd = (new V(1)).e(1);
            G(levelBtnLayer, levelBtnLayer.Cd)
        }))
    }
    Q.uc = function(a) {
        a = new $(a);
        De ? R(a) : R(a, df, 0.5)
    }
    ;
    Q.Hd = function() {
        settingsPopupShowed == !1 ? (Fh(),
        O.Db(function() {
            settingsPopup.h = (new S(0,85)).e(0.3);
            G(settingsPopup, settingsPopup.h);
            settingsPopupShowed = !0
        }, this, 1200, 1)) : (Eh(),
        settingsPopup.h = (new S(0,-600)).e(0.3),
        G(settingsPopup, settingsPopup.h),
        settingsPopupShowed = !1)
    }
    ;
    Q.Oc = function() {
        scoresPopupShowed == !1 ? (Fh(),
        O.Db(function() {
            scoresPopup.h = (new S(0,85)).e(0.3);
            G(scoresPopup, scoresPopup.h);
            scoresPopupShowed = !0
        }, this, 1200, 1)) : (Eh(),
        scoresPopup.h = (new S(0,-600)).e(0.3),
        G(scoresPopup, scoresPopup.h),
        scoresPopupShowed = !1)
    }
    ;
    Q.Vf = function() {
        var a = new Y(!1);
        De ? R(a) : R(a, df, 0.5)
    }
    ;
    Q.Ed = function() {
        var a = new gf(!1);
        De ? R(a) : R(a, df, 0.5)
    }
    ;
    Q.Lb = function() {
        Qe ? (localStorage.setItem("av.soundSetting", !1),
        Q.eb.stop(),
        Qe = !1,
        D(soundOnIcon, 0),
        D(soundOnbtn, 0),
        D(soundOffIcon, 1),
        D(soundOffbtn, 1)) : (localStorage.setItem("av.soundSetting", !0),
        Qe = !0,
        Q.eb.reload(),
        Q.eb.play(),
        D(soundOnIcon, 1),
        D(soundOnbtn, 1),
        D(soundOffIcon, 0),
        D(soundOffbtn, 0))
    }
    ;
    Q.Df = function(a) {
        Gh(a);
        a = new Q(!1);
        R(a)
    }
    ;
    function Fh() {
        He == "all" ? (settingsBtn.moveTo = (new S(460,755)).e(0.3),
        G(settingsBtn, settingsBtn.moveTo),
        helpBtn.moveTo = (new S(460,755)).e(0.3),
        G(helpBtn, helpBtn.moveTo),
        moreBtn.moveTo = (new S(460,755)).e(0.3),
        G(moreBtn, moreBtn.moveTo),
        btnHomeScreenStarter.h = (new S(480,330)).e(0.35),
        G(btnHomeScreenStarter, btnHomeScreenStarter.h),
        btnHomeScreenJunior.h = (new S(480,240)).e(0.35),
        G(btnHomeScreenJunior, btnHomeScreenJunior.h),
        btnHomeScreenExpert.h = (new S(480,240)).e(0.35),
        G(btnHomeScreenExpert, btnHomeScreenExpert.h),
        btnHomeScreenMaster.h = (new S(480,330)).e(0.35),
        G(btnHomeScreenMaster, btnHomeScreenMaster.h),
        w(btnHomeScreenMaster.h, T, function() {
            levelSelectorHomeScreen.h = new Sf((new S(0,-500)).e(0.6),(new V(0)).e(0.25));
            G(levelSelectorHomeScreen, levelSelectorHomeScreen.h);
            Nd(levelSelectIndicatorArrow, 0)
        })) : (levelBtnLayer.Cd = (new V(0)).e(0.5),
        G(levelBtnLayer, levelBtnLayer.Cd),
        btnHomeScreenStarter.h = new ng((new U(0.5,1)).e(0.35),(new S(480,290)).e(0.35)),
        G(btnHomeScreenStarter, btnHomeScreenStarter.h),
        btnHomeScreenJunior.h = new ng((new U(0.5,1)).e(0.35),(new S(480,210)).e(0.35)),
        G(btnHomeScreenJunior, btnHomeScreenJunior.h),
        btnHomeScreenExpert.h = new ng((new U(0.5,1)).e(0.35),(new S(480,210)).e(0.35)),
        G(btnHomeScreenExpert, btnHomeScreenExpert.h),
        btnHomeScreenMaster.h = new ng((new U(0.5,1)).e(0.35),(new S(480,290)).e(0.35)),
        G(btnHomeScreenMaster, btnHomeScreenMaster.h),
        w(btnHomeScreenMaster.h, T, function() {
            levelSelectorHomeScreen.h = new Sf((new S(0,-500)).e(0.6),(new V(0)).e(0.25));
            G(levelSelectorHomeScreen, levelSelectorHomeScreen.h)
        }))
    }
    s(Q, Ja);
    function Hh(a) {
        Ja.call(this);
        loadingIcon = (new P).c(Me + "sun.png").a(480, 230);
        this.appendChild(loadingIcon);
        sglLogo = (new P).c(Me + "sglLogo.png").a(480, 250);
        this.appendChild(sglLogo);
        lbl = M(L(K(new N, 40).g(I.loading).a(480, 470), "#fff"), "futuraBold").b(960, 40);
        this.appendChild(lbl);
        Hh.Ue = M(L(K(new N, 40).a(480, 530), "#fff").b(), "futuraBold").g("0%");
        this.appendChild(Hh.Ue);
        Ih(a);
        Se = !0
    }
    var Jh = []
      , Kh = []
      , Lh = 0;
    function Ih(a) {
        var b = ["spritesheets/levelIndicator.png", "spritesheets/homeScreenLevelIndicator.png", "spritesheets/sglButtonsBart.png"];
        sglSpriteImgs = [];
        for (var c = 0; c < b.length; c++)
            Jh[c] = new Image,
            Jh[c].crossOrigin = "Anonymous",
            Jh[c].src = Te + b[c],
            Jh[c].complete = !1,
            sglSpriteImgs.push(Jh[c]);
        var d = ["spritesheets/avPuzzlePieces.png"];
        gameSpriteImgs = [];
        for (c = 0; c < d.length; c++)
            Jh[c + b.length] = new Image,
            Jh[c + b.length].crossOrigin = "Anonymous",
            Jh[c + b.length].src = Ue + d[c],
            Jh[c + b.length].complete = !1,
            gameSpriteImgs.push(Jh[c + b.length]);
        for (var e = "backgroundPlay.jpg,backgroundPlayBoard.png,bgHomeScreen.jpg,bgLevelSelect.jpg,bttnExpert.png,bttnJunior.png,bttnLocked.png,bttnMaster.png,bttnStarter.png,help1.jpg,help2.jpg,popupBlank.png,popupLevel.png,popupPause.png,bgAdverGame.jpg,add2Cart.png,3piggies.png,stripeArrow.png,banner.png,levelSelectArrowBg.png,levelSelectArrow.png,bannerBottom.jpg".split(","), c = 0; c < e.length; c++)
            Jh[c + b.length + d.length] = new Image,
            Jh[c + b.length + d.length].src = J + e[c];
        for (var g = "btnPause.png,btnReset.png,btnSpeakerOff.png,btnSpeakerOn.png,emptyStar.png,levelSelectArrow.png,loading.gif,sglLogo.png,star.png,sun.png,timeIndicator.png".split(","), c = 0; c < g.length; c++)
            Jh[c + e.length + b.length + d.length] = new Image,
            Jh[c + e.length + b.length + d.length].src = Me + g[c];
        for (c = 0; c < Jh.length; c++)
            Kh[c] = !1;
        Q.eb = new Mh(J + "sounds/home/antivirusTheme.mp3",!0,0);
        Q.n = new Mh(J + "sounds/home/btnPlay.mp3",!1,1);
        $.Sb = new Mh(J + "sounds/levelSelect/btnHome.mp3",!1,2);
        $.n = new Mh(J + "sounds/levelSelect/btnPlay2.mp3",!1,3);
        F.pf = new Mh(J + "sounds/level/drag.mp3",!1,4);
        F.qf = new Mh(J + "sounds/level/drag.mp3",!1,5);
        F.mf = new Mh(J + "sounds/level/btnPause.mp3",!1,6);
        F.tf = new Mh(J + "sounds/level/btnReset.mp3",!1,7);
        F.Cc = new Mh(J + "sounds/level/btnResume.mp3",!1,8);
        if (!lg(F.Ae))
            F.Ae = new Mh(J + "sounds/level/congrats.mp3",!1,9);
        if (!lg(F.Da))
            F.Da = new Mh(J + "sounds/level/backgroundSound.mp3",!0,10);
        var h = this, m;
        O.Db(f = function() {
            rotateLogo = (new og(15)).e(0.0010);
            G(loadingIcon, rotateLogo);
            if (Lh == Jh.length && Se)
                O.X(f, h),
                a != k ? (He = a,
                m = new Q(!0,a)) : (He = "all",
                m = new Q(!1)),
                R(m);
            else
                for (var b = 0; b <= Jh.length; b++)
                    Kh[b] == !1 && Jh[b].complete && (Kh[b] = !0,
                    percentage = Math.round(Lh / Jh.length * 100),
                    Hh.Ue.g(percentage + "%"),
                    Lh++)
        }
        , h, 10)
    }
    s(Hh, Ja);
    function Nh() {
        if (localStorage.getItem("av.scoreDataJSON") == k) {
            var a = {
                Starter: {},
                Junior: {},
                Expert: {},
                Master: {}
            };
            try {
                localStorage.setItem("av.scoreDataJSON", we(a)),
                localStorage.setItem("av.numStars", 0),
                te = we(a),
                Je = 0
            } catch (b) {}
        }
        te = localStorage.getItem("av.scoreDataJSON");
        Je = localStorage.getItem("av.numStars");
        return se()
    }
    function kg(a, b) {
        scoreDataJSON = Nh();
        try {
            return lg(scoreDataJSON[b][a]) ? scoreDataJSON[b][a] : 0
        } catch (c) {
            return 0
        }
    }
    function $e(a, b) {
        var c = F.Xa
          , d = F.K
          , e = F.jf;
        try {
            scoreDataJSON = Nh();
            playStars = Ze(a, d);
            if (lg(scoreDataJSON[d][c])) {
                if (scoreDataJSON[d][c].minNumMovesPlayed > e && (scoreDataJSON[d][c].minNumMovesPlayed = e),
                scoreDataJSON[d][c].fastestTime > a && (scoreDataJSON[d][c].fastestTime = a),
                scoreDataJSON[d][c].highestScore < b && (scoreDataJSON[d][c].highestScore = b),
                scoreDataJSON[d][c].stars < playStars) {
                    var g = parseInt(Je) - parseInt(scoreDataJSON[d][c].stars) + parseInt(playStars);
                    Je = g;
                    localStorage.setItem("av.numStars", g);
                    scoreDataJSON[d][c].stars = playStars
                }
            } else
                scoreDataJSON[d][c] = {
                    highestScore: b,
                    fastestTime: a,
                    minNumMovesPlayed: e,
                    stars: playStars
                },
                g = parseInt(Je) + parseInt(playStars),
                localStorage.setItem("av.numStars", g),
                Je = g;
            te = we(scoreDataJSON);
            localStorage.setItem("av.scoreDataJSON", we(scoreDataJSON))
        } catch (h) {}
    }
    function Ye(a) {
        var b = F.K, c;
        b == "Starter" ? c = 90 : b == "Junior" ? c = 180 : b == "Expert" ? c = 360 : b == "Master" && (c = 600);
        playScore = 0;
        maxPoints = 1E5;
        playScore = Math.floor(maxPoints - a * (1E3 - c));
        playScore < 0 && (playScore = 0);
        return playScore
    }
    function Ze(a, b) {
        var c, d;
        b == "Starter" ? (c = 50,
        d = 60) : b == "Junior" ? (c = 90,
        d = 120) : b == "Expert" ? (c = 240,
        d = 300) : b == "Master" && (c = 540,
        d = 600);
        return a < c ? 3 : a < d ? 2 : 1
    }
    ;var Ah = {
        en: {
            play: "Play",
            settings: "Settings",
            scores: "Scores",
            more: "More",
            "how to play": "Tutorial",
            close: "Close",
            sound: "Sound:",
            language: "Language:",
            "select level": "Select Level",
            "select challenge": "Select Challenge",
            "stars needed": "stars needed to unlock this level.",
            "very good": "Very good!",
            "well done!": "Well done!",
            "congratulations!": "Congratulations!",
            challenge: "Challenge",
            "completed.": "completed.",
            "moves:": "Moves:",
            "score:": "Score:",
            "time:": "Time:",
            "stars:": "Stars:",
            "play next": "Play next",
            "challenge completed": "You have completed the challenge.",
            resume: "Resume",
            "select challenge": "Select Challenge",
            help: "Tutorial",
            hello: "Hello",
            "this is the first time...": "First-time player? Here are some quick instructions.",
            "continue": "Continue",
            "Challenge locked in lite version. Get our app to play this challenge.": "Challenge locked in lite version. Get our app to play this challenge.",
            "final challenge": "Final challenge",
            name: "Name",
            highscore: "Highscore",
            "Register sgl": "Register now for free on SmartGamesLive to play this challenge! Save your highscores, play all challenges, play all games, and have more fun!",
            step1: "Step 1",
            step2: "Step 2",
            "more info": "More Info",
            home: "Home",
            register: "Register now!",
            gameRules: "Game rules",
            "Rate challenge": "Feel free to rate this challenge:",
            "Rate challenge for next": "Rate to play the next challenge:",
            "Register sgl popup": "Register now for free on SmartGamesLive to save your highscores, play all challenges, play all games, and have more fun!",
            "Rate challenge for next game": "Rate to play the next game:",
            boring: "boring",
            amazing: "amazing",
            helpTitle: "Put your body and mind to work and get rid of the red virus!",
            help1: "1.  Move the colored game pieces around as indicated so you can maneuver the virus (the red game piece) to the exit:",
            help1Sub1: "- Game pieces can only slide diagonally. You can't rotate them.",
            help1Sub2: "- When needed, you can move pieces together as a group.",
            help1Sub3: "- White game pieces are stationary.",
            help2: "2. You have solved the puzzle when you can force the red virus through the exit and off the game board.  Have fun!",
            "step1...": "Move the game pieces around, so you can maneuver the virus (the red game piece) to the exit.",
            "step2...": "You have found the solution when you can force the red virus completely through the opening and off the game board.",
            loading: "Loading AntiVirus"
        },
        nl: {
            play: "Speel",
            settings: "Opties",
            scores: "Scores",
            "how to play": "Tutorial",
            more: "Meer",
            close: "Sluit",
            sound: "Geluid:",
            language: "Taal:",
            "select level": "Selecteer Level",
            "select challenge": "Selecteer Opdracht",
            "stars needed": "sterren nodig om de volgende opdracht te kunnen spelen.",
            "very good": "Heel goed!",
            "well done!": "Goed gedaan!",
            "congratulations!": "Proficiat!",
            challenge: "Opdracht",
            "completed.": "opgelost.",
            "moves:": "Bewegingen:",
            "score:": "Score:",
            "time:": "Tijd:",
            "stars:": "Sterren:",
            "play next": "Volgende",
            "challenge completed": "Opdracht volbracht.",
            resume: "Spelen",
            "select challenge": "Kies opdracht",
            help: "Tutorial",
            hello: "Hallo",
            "this is the first time...": "Dit lijkt de eerste keer te zijn dat je dit spel speelt. Hieronder de spelregels.",
            "continue": "Ga verder",
            "final challenge": "Laatste opdracht",
            "Get all 96": "Alle 96 opdrachten via de app store:",
            "get app": "Je hebt de laatste opdracht van Titanic Online opgelost. Wil je graag meer? Ga nu naar de App Store en download alle 96 opdrachten.",
            name: "Naam",
            highscore: "Highscore",
            "Register sgl": "Registreer je nu gratis op SmartGamesLive om deze opdracht te spelen. Bewaar je scores, speel alle opdrachten en spellen!",
            step1: "Stap 1",
            step2: "Stap 2",
            "step1...": "Verschuif de spelstukken diagonaal, zodat je het virus (het rode spelstuk) naar de opening in het spelbord kan schuiven.",
            "step2...": "Je hebt de juiste oplossing gevonden, wanneer je het rode virus door de opening van het spelbord naar buiten kan schuiven.",
            "more info": "Meer Info",
            home: "Home",
            register: "Registreer nu!",
            helpTitle: "Het 'Bio-Logisch' denkspel!",
            help1: "1. Verschuif alle puzzelstukken, zodat je het virus (het rode puzzelstuk) via opening linksboven kan verwijderen:",
            help1Sub1: "- Puzzelstukken kan je enkel diagonaal verplaatsen. Je kan ze niet draaien.",
            help1Sub2: "- Soms moet je verschillende puzzelstukken in groep verplaatsen",
            help1Sub3: "- De witte puzzelstukken kan je NIET verplaatsen.",
            help2: "2. Je hebt de juiste oplossing gevonden wanneer je het rode puzzelstuk naar buiten kan schuiven. Veel plezier!",
            gameRules: "Spelregels",
            "Rate challenge": "Feel free to rate this challenge:",
            "Rate challenge for next": "Geef een score om verder te gaan:",
            "Register sgl popup": "Registreer je nu gratis op SmartGamesLive om alle opdrachten en spellen te spelen alsook je scores te bewaren!",
            "Rate challenge for next game": "Geef een score om verder te gaan:",
            boring: "saai",
            amazing: "geweldig",
            loading: "AntiVirus opstarten"
        },
        fr: {
            play: "Jouer",
            settings: "R\u00e9glages",
            scores: "R\u00e9sultats",
            "how to play": "Tutoriel",
            more: "Extra",
            close: "Fermer",
            sound: "Son:",
            language: "Langue:",
            "select level": "Choisir un niveau",
            "select challenge": "Choisir un d\u00e9fi",
            "stars needed": "Nombre d\u2019Etoiles n\u00e9cessaire pour acc\u00e9der au niveau sup\u00e9rieur.",
            "very good": "Tr\u00e8s bien!",
            "well done!": "Bien Jou\u00e9!",
            "congratulations!": "F\u00e9licitations!",
            challenge: "D\u00e9fi",
            "completed.": "Termin\u00e9",
            "moves:": "D\u00e9placements:",
            "score:": "R\u00e9sultat:",
            "time:": "Chronom\u00e8tre:",
            "stars:": "Etoiles:",
            "play next": "Nouveau d\u00e9fi",
            "challenge completed": "D\u00e9fi termin\u00e9.",
            resume: "Reprendre",
            "select challenge": "Choisir un d\u00e9fi",
            help: "Tutoriel",
            hello: "Bonjour",
            "this is the first time...": "Pour votre premi\u00e8re partie, consultez d\u2019abord le tutoriel.",
            "continue": "Continuez",
            "final challenge": "Dernier d\u00e9fi",
            name: "Nom",
            highscore: "Meilleur score",
            "Register sgl": "Inscrivez-vous gratuitement sur SmartGamesLive pour jouer \u00e0 ce d\u00e9fi! Enregistrez vos meilleurs scores, acc\u00e9dez \u00e0 tous les jeux et tous leurs d\u00e9fis, pour un plaisir sans fin !!",
            step1: "Etape 1",
            step2: "Etape 2",
            "step1...": "D\u00e9placez vos pi\u00e8ces \u00e0 l\u2019int\u00e9rieur du plan de jeu comme bon vous semble afin de faire sortir le virus (la pi\u00e8ce rouge).",
            "step2...": "Le d\u00e9fi est r\u00e9solu lorsque la pi\u00e8ce rouge (le virus) est sortie du plan de jeu par la seule ouverture possible.",
            "more info": "Savoir plus",
            home: "Accueil",
            register: "S'inscrire!",
            helpTitle: "Mobilisez vos anticorps pour vous d\u00e9barrasser d'un dangereux virus!",
            help1: "1. Faites circuler les pi\u00e8ces colori\u00e9es comme indiqu\u00e9 pour man\u0153uvrer le virus (la pi\u00e8ce rouge) vers la sortie\u00a0:",
            help1Sub1: "- Les pi\u00e8ces peuvent uniquement \u00eatre gliss\u00e9es en diagonale. Vous ne pouvez pas les faire tourner.",
            help1Sub2: "- Si n\u00e9cessaire, vous pouvez d\u00e9placer plusieurs pi\u00e8ces en une seule fois.",
            help1Sub3: "- Les pi\u00e8ces blanches sont fixes.",
            help2: "2. Vous avez r\u00e9solu le puzzle lorsque vous pouvez forcer le virus vers la sortie et l\u2019expulser du plateau de jeu. Amusez-vous bien!",
            gameRules: "R\u00e8gles du jeu",
            "Rate challenge": "Evaluez ce d\u00e9fi en lui donnant une note:",
            "Rate challenge for next": "Note pour passer au d\u00e9fi suivant:",
            "Register sgl popup": "Inscrivez-vous gratuitement sur SmartGamesLive pour enregistrez vos meilleurs scores, acc\u00e9dez \u00e0 tous les d\u00e9fis, pour un plaisir sans fin !",
            "Rate challenge for next game": "Note pour passer au jeu suivant:",
            boring: "ennuyeux",
            amazing: "soufflant",
            loading: "Chargement du AntiVirus"
        },
        es: {
            play: "Jugar",
            settings: "Ajustes",
            scores: "Puntajes",
            more: "Otros",
            help: "Tutorial",
            close: "Cerrar",
            sound: "Sonido:",
            language: "Idioma:",
            "select level": "Seleccionar nivel",
            "select challenge": "Seleccionar puzle",
            "stars needed": "estrellas necesarias para completar este nivel.",
            "very good": "\u00a1Muy bien!",
            "well done!": "\u00a1Bien hecho!",
            "congratulations!": "\u00a1Enhorabuena!",
            challenge: "Reto",
            "completed.": "completado.",
            "moves:": "Movimiento:",
            "score:": "Puntuaci\u00f3n:",
            "time:": "Tiempo:",
            "stars:": "Estrellas:",
            "play next": "Jugar siguiente",
            "challenge completed": "Has completado el reto.",
            resume: "Volver",
            hello: "Hola",
            "this is the first time...": "\u00bfEs la primera vez que juegas? Te damos un par de instrucciones breves.",
            "continue": "Continuar",
            "final challenge": "\u00daltimo reto",
            name: "Nombre",
            highscore: "M\u00e1xima puntuaci\u00f3n",
            "Register sgl": "\u00a1Reg\u00edstrate ahora gratuitamente en SmartGamesLive para jugar a este reto! \u00a1Guarda tus puntuaciones m\u00e1ximas, juega a todos los juegos y retos y divi\u00e9rtete!",
            "Register sgl popup": "Reg\u00edstrate ahora gratuitamente en SmartGamesLive para guardar tus puntuaciones m\u00e1ximas, juegar a todos los juegos!",
            step1: "Paso 1",
            step2: "Paso 2",
            "more info": "M\u00e1s info",
            home: "Inicio",
            register: "\u00a1Reg\u00edstrate!",
            gameRules: "Normas del juego",
            "Rate challenge": "Punt\u00faa este reto:",
            "Rate challenge for next": "Puntuaci\u00f3n para jugar el siguiente reto:",
            "Rate challenge for next game": "Puntuaci\u00f3n para jugar al siguiente juego:",
            boring: "aburrido",
            amazing: "incre\u00edble",
            helpTitle: "\u00a1Pon a trabajar tu cuerpo y mente y l\u00edbrate del virus rojo!",
            help1: "1. Mueve las piezas de colores seg\u00fan se indica para poder mover el virus (la pieza roja) hasta la salida:",
            help1Sub1: "- Las piezas del juego s\u00f3lo se deslizan de forma diagonal. No se pueden girar.",
            help1Sub2: "- Si lo necesitas, podr\u00e1s mover las piezas en grupo.",
            help1Sub3: "- Las piezas blancas est\u00e1n fijas.",
            help2: "2. Habr\u00e1s solucionado el puzle cuando consigas obligar al virus rojo a irse del tablero por la salida. \u00a1Divi\u00e9rtete!",
            "step1...": "Mueve las piezas para poder mover el virus (la pieza roja) hasta la salida.",
            "step2...": "Habr\u00e1s solucionado el puzle cuando consigas obligar al virus rojo a irse del tablero por la apertura.",
            loading: "Cargando AntiVirus"
        },
        ru: {
            play: "\u0418\u0433\u0440\u0430\u0442\u044c",
            settings: "\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438",
            scores: "\u041e\u0447\u043a\u0438",
            more: "\u0415\u0449\u0451",
            "how to play": "\u041a\u0430\u043a \u0438\u0433\u0440\u0430\u0442\u044c, \u041e\u0411\u0423\u0427\u0415\u041d\u0418\u0415",
            close: "\u0417\u0430\u043a\u0440\u044b\u0442\u044c",
            sound: "\u0417\u0432\u0443\u043a:",
            language: "\u042f\u0437\u044b\u043a:",
            "select level": "\u0412\u044b\u0431\u043e\u0440 \u0443\u0440\u043e\u0432\u043d\u044f",
            "select challenge": "\u0412\u044b\u0431\u043e\u0440 \u0437\u0430\u0434\u0430\u043d\u0438\u044f",
            "stars needed": "\u0427\u0442\u043e\u0431\u044b \u0440\u0430\u0437\u0431\u043b\u043e\u043a\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u044d\u0442\u043e\u0442 \u0443\u0440\u043e\u0432\u0435\u043d\u044c, \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b \u0437\u0432\u0451\u0437\u0434\u044b. ",
            "very good": "\u041e\u0447\u0435\u043d\u044c \u0445\u043e\u0440\u043e\u0448\u043e!",
            "well done!": "\u041c\u043e\u043b\u043e\u0434\u0435\u0446!",
            "congratulations!": "\u041f\u043e\u0437\u0434\u0440\u0430\u0432\u043b\u044f\u0435\u043c!",
            challenge: "\u0417\u0430\u0434\u0430\u043d\u0438\u0435",
            "completed.": "\u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e.",
            "moves:": "\u0412\u0438\u0434\u0435\u043e:",
            "score:": "\u041e\u0447\u043a\u0438:",
            "time:": "\u0412\u0440\u0435\u043c\u044f:",
            "stars:": "\u0417\u0432\u0451\u0437\u0434\u044b:",
            "play next": "\u0418\u0433\u0440\u0430\u0442\u044c \u0434\u0430\u043b\u044c\u0448\u0435",
            "challenge completed": "\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e.",
            resume: "\u0418\u0442\u043e\u0433\u0438",
            help: "\u041f\u043e\u043c\u043e\u0449\u044c",
            hello: "\u041f\u0440\u0438\u0432\u0435\u0442\u0441\u0442\u0432\u0443\u0435\u043c",
            "this is the first time...": "\u0418\u0433\u0440\u0430\u0435\u0442\u0435 \u0432 \u043f\u0435\u0440\u0432\u044b\u0439 \u0440\u0430\u0437? \u0417\u0434\u0435\u0441\u044c \u043d\u0435\u0441\u043a\u043e\u043b\u044c\u043a\u043e \u043f\u0440\u043e\u0441\u0442\u044b\u0445 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u0439.",
            "continue": "\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c",
            "final challenge": "\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0435\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435",
            name: "\u0418\u043c\u044f",
            highscore: "\u0420\u0435\u043a\u043e\u0440\u0434",
            "Register sgl": "\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u0443\u0439\u0442\u0435\u0441\u044c \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e \u0441\u0435\u0439\u0447\u0430\u0441 \u043d\u0430 SmartGamesLive! \u0421\u043e\u0445\u0440\u0430\u043d\u044f\u0439\u0442\u0435 \u0441\u0432\u043e\u0438 \u0440\u0435\u043a\u043e\u0440\u0434\u044b! \u0418\u0433\u0440\u0430\u0439\u0442\u0435 \u0432 \u0443\u0434\u043e\u0432\u043e\u043b\u044c\u0441\u0442\u0432\u0438\u0435!  ",
            step1: "\u0428\u0430\u0433 1",
            step2: "\u0428\u0430\u0433 2",
            home: "\u0414\u043e\u043c\u043e\u0439",
            register: "\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f \u0441\u0435\u0439\u0447\u0430\u0441!",
            gameRules: "\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b",
            "Rate challenge": "\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435:",
            "Rate challenge for next": "\u041e\u0446\u0435\u043d\u0438\u0442\u0435 \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0435 \u0437\u0430\u0434\u0430\u043d\u0438\u0435:",
            "Rate challenge for next game": "\u041e\u0446\u0435\u043d\u0438\u0442\u0435  \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0443\u044e \u0438\u0433\u0440\u0443:",
            boring: "\u0421\u043a\u0443\u0447\u043d\u043e",
            amazing: "\u0418\u0437\u0443\u043c\u0438\u0442\u0435\u043b\u044c\u043d\u043e",
            "Register sgl popup": "Register now for free on SmartGamesLive to save your highscores, play all challenges, play all games, and have more fun!",
            "more info": "\u0411\u043e\u043b\u044c\u0448\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438",
            helpTitle: "\u00ab\u0412\u0438\u0440\u0443\u0441\u00bb \u0432\u0442\u043e\u0440\u0433\u0441\u044f \u0432 \u0412\u0430\u0448\u0443 \u0441\u0438\u0441\u0442\u0435\u043c\u0443, \u0438\u0437\u0431\u0430\u0432\u044c\u0442\u0435\u0441\u044c \u043e\u0442 \u043a\u0440\u0430\u0441\u043d\u043e\u0433\u043e \u0447\u0443\u0436\u0430\u043a\u0430!",
            help1: "1. \u041f\u0435\u0440\u0435\u0434\u0432\u0438\u0433\u0430\u0439\u0442\u0435 \u0446\u0432\u0435\u0442\u043d\u044b\u0435 \u0434\u0435\u0442\u0430\u043b\u0438, \u0441 \u0446\u0435\u043b\u044c\u044e  \u0441\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u00ab\u0432\u0438\u0440\u0443\u0441\u00bb (\u043a\u0440\u0430\u0441\u043d\u0443\u044e \u0434\u0435\u0442\u0430\u043b\u044c) \u043a \u0432\u044b\u0445\u043e\u0434\u0443:",
            help1Sub1: "- \u0414\u0435\u0442\u0430\u043b\u0438 \u043f\u0435\u0440\u0435\u043c\u0435\u0449\u0430\u044e\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u043f\u043e \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u044f\u043c. \u0412\u044b \u043d\u0435 \u043c\u043e\u0436\u0435\u0442\u0435 \u0438\u0445 \u0432\u0440\u0430\u0449\u0430\u0442\u044c.",
            help1Sub2: "- \u041f\u0440\u0438 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e\u0441\u0442\u0438 \u0412\u044b \u043c\u043e\u0436\u0435\u0442\u0435 \u043f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432\u043c\u0435\u0441\u0442\u0435  \u0433\u0440\u0443\u043f\u043f\u0443 \u0434\u0435\u0442\u0430\u043b\u0435\u0439.",
            help1Sub3: "- \u0411\u0435\u043b\u044b\u0435 \u0434\u0435\u0442\u0430\u043b\u0438 \u2013 \u0441\u0442\u0430\u0446\u0438\u043e\u043d\u0430\u0440\u043d\u044b.",
            help2: "2. \u0412\u044b \u0441\u043f\u0440\u0430\u0432\u0438\u043b\u0438\u0441\u044c \u0441 \u0437\u0430\u0434\u0430\u043d\u0438\u0435\u043c, \u0435\u0441\u043b\u0438 \u0441\u043c\u043e\u0433\u043b\u0438 \u0432\u044b\u0442\u0435\u0441\u043d\u0438\u0442\u044c \u00ab\u0432\u0438\u0440\u0443\u0441\u00bb \u0437\u0430 \u043f\u0440\u0435\u0434\u0435\u043b\u044b \u0438\u0433\u0440\u043e\u0432\u043e\u0433\u043e \u043f\u043e\u043b\u044f. \u0423\u0434\u0430\u0447\u0438!",
            "step1...": "\u041f\u0435\u0440\u0435\u0434\u0432\u0438\u0433\u0430\u0439\u0442\u0435 \u0446\u0432\u0435\u0442\u043d\u044b\u0435 \u0434\u0435\u0442\u0430\u043b\u0438, \u0441 \u0446\u0435\u043b\u044c\u044e  \u0441\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u00ab\u0432\u0438\u0440\u0443\u0441\u00bb (\u043a\u0440\u0430\u0441\u043d\u0443\u044e \u0434\u0435\u0442\u0430\u043b\u044c) \u043a \u0432\u044b\u0445\u043e\u0434\u0443.",
            "step2...": "\u0412\u044b \u0441\u043f\u0440\u0430\u0432\u0438\u043b\u0438\u0441\u044c \u0441 \u0437\u0430\u0434\u0430\u043d\u0438\u0435\u043c, \u0435\u0441\u043b\u0438 \u0441\u043c\u043e\u0433\u043b\u0438 \u0432\u044b\u0442\u0435\u0441\u043d\u0438\u0442\u044c \u00ab\u0432\u0438\u0440\u0443\u0441\u00bb \u0447\u0435\u0440\u0435\u0437 \u043e\u0442\u0432\u0435\u0440\u0441\u0442\u0438\u0435  \u043d\u0430 \u0438\u0433\u0440\u043e\u0432\u043e\u043c \u043f\u043e\u043b\u0435.",
            loading: "\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u00ab\u0410\u043d\u0442\u0438\u0432\u0438\u0440\u0443\u0441\u00bb"
        }
    };
    function Gh(a) {
        a = a.split("-");
        Ce = a[0];
        I = Ah[a[0]]
    }
    function fg(a, b) {
        var c = (new U(1.25)).e(0.05);
        G(a, c);
        w(c, T, function() {
            var c = (new U(1)).e(0.15);
            G(a, c);
            w(c, T, function() {
                b()
            })
        })
    }
    function yh(a, b) {
        var c = (new U(1.75)).e(0.05);
        G(a, c);
        w(c, T, function() {
            var c = (new U(1.5)).e(0.05);
            G(a, c);
            w(c, T, function() {
                b()
            })
        })
    }
    function zh(a) {
        var b = Q.Lb
          , c = (new U(0.8)).e(0.05);
        G(a, c);
        w(c, T, function() {
            var c = (new U(0.6)).e(0.15);
            G(a, c);
            w(c, T, function() {
                b()
            })
        })
    }
    function Uf(a, b) {
        var c = (new U(1.25)).e(0.05);
        G(a, c);
        w(c, T, function() {
            var c = (new U(1)).e(0.15);
            G(a, c);
            w(c, T, function() {
                b(a.K)
            })
        })
    }
    function Bh(a) {
        var b = Q.Df
          , c = (new U(1)).e(0.05);
        G(a, c);
        w(c, T, function() {
            var c = (new U(0.7)).e(0.15);
            G(a, c);
            w(c, T, function() {
                b(a.language)
            })
        })
    }
    function bf() {
        var a = "futura"
          , a = "futuraBold";
        Ce == "cz" && (a = "Tahoma");
        return a
    }
    ;function Mh(a, b, c) {
        if (Qg == "web")
            if (a && la(a.data) && (a = a.data()),
            this.wa = this.Tc = !1,
            Fc)
                this.I = k;
            else {
                this.I = document.createElement("audio");
                this.I.ph = !0;
                this.I.loop = b;
                if ((Bb || zb) && /\.mp3$/.test(a))
                    a = a.replace(/\.mp3$/, ".ogg"),
                    b && this.I.addEventListener("ended", function() {
                        this.currentTime = 0.1;
                        this.play()
                    }, !0);
                this.I.src = a;
                this.I.load();
                this.Pd = setInterval(ta(this.fg, this), 10);
                this.Tc = !1
            }
        else if (Qg == "desktop")
            this.I = Titanium.ah.dh("app://" + a),
            b && this.I.sh(!0);
        else if (Qg == "mobile")
            this.I = c,
            Ti.ld.fireEvent("app:fromWebView", {
                message: "load_audio",
                url: a,
                kh: b,
                element: this.I
            }),
            this.wa = !1
    }
    n = Mh.prototype;
    n.fg = function() {
        if (this.I.readyState > 2)
            this.Tc = !0,
            clearTimeout(this.Pd);
        this.I.error && clearTimeout(this.Pd);
        if (Fc && this.I.readyState == 0)
            this.Tc = !0,
            clearTimeout(this.Pd)
    }
    ;
    n.Tb = aa("Tc");
    n.play = function() {
        if (Qe == !0)
            Qg == "mobile" ? Ti.ld.fireEvent("app:fromWebView", {
                message: "play_audio",
                element: this.I
            }) : this.I != k && this.I.play(),
            this.wa = !0
    }
    ;
    n.stop = function() {
        if (Qg == "mobile")
            Ti.ld.fireEvent("app:fromWebView", {
                message: "stop_audio",
                element: this.I
            }),
            this.wa = !1;
        else if (this.I != k && this.wa)
            this.I.pause(),
            this.wa = !1
    }
    ;
    n.reload = function() {
        if (Qe == !0)
            if (Qg == "web") {
                if (!Fc && this.Tb())
                    this.I.currentTime = 0.1
            } else
                Qg == "desktop" ? this.I.reload() : Qg == "mobile" && Ti.ld.fireEvent("app:fromWebView", {
                    message: "reload_audio",
                    element: this.I
                })
    }
    ;
    var J = "./assets/game/"
      , ph = 960
      , qh = 600;
    da("antivirus.start", function(a, b, c, d, e, g, h, m, l, q) {
        if (Fc && c == "web")
            Qe = !1;
        else if (localStorage.getItem("av.soundSetting") == k) {
            Qe = !0;
            try {
                localStorage.setItem("av.soundSetting", !0)
            } catch (A) {}
        } else
            Qe = localStorage.getItem("av.soundSetting") == "true" ? !0 : !1;
        b != k && (J = b);
        Me = m != k ? m : "../game-assets/";
        Ue = l != k ? l : J;
        Te = q != k ? q : Me;
        Mg = a == "gameContent" ? new Jg(document.getElementById("gameContent"),ph,qh) : new Jg(document.body,ph,qh);
        Qg = c;
        d == k && (d = "en");
        Gh(d);
        navigator.userAgent.toLowerCase().indexOf("android") != -1 ? (De = !0,
        Qe = !1) : De = !1;
        Ne = e;
        a = new Hh(h);
        R(a)
    });
    resizeGame = function() {
        Mg.wc()
    }
    ;
    da("resizeGame", resizeGame);
    switchLevel = function(a) {
        He = a;
        window.changeLevel(He);
        scene = new Q(!1,a);
        R(scene);
        try {
            lg(chrono) && O.X(chrono, F)
        } catch (b) {}
    }
    ;
    da("switchLevel", switchLevel);
}
)();
