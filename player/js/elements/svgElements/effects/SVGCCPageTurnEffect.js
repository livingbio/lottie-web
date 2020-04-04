function setupAnimation() {
    const tl = anime.timeline({
        delay: 1000,
        endDelay: 1500,
        loop: true,
        easing: 'cubicBezier(0.25, 0.1, 0.25, 1.0)'
    })
    const animations = [
        ...setupPageFlip(),
        ...setupPageFade(),
        ...setupShowDay()
    ]
    for (let animation of animations) {
        tl.add(animation, 0)
    }
    return tl
}

function setupPageFlip({
    backColor = 'white',
    paperTransparency = 0,
    fromAngle: a0 = Math.PI / 12,
    toAngle: a1 = Math.PI / 4,
    duration = 1000
} = {}) {
    const box = document.querySelector('.front').getBBox()
    const {
        width: w,
        height: h
    } = box
    const dx = (h + w * Math.tan(a0)) / (Math.tan(a1) - Math.tan(a0))
    const dy = dx * Math.tan(a1) - h
    const x = box.x - dx
    const y = box.y - dy
    const origin = `${x} ${y}`
    const maskAttrs = [
        ['x', x],
        ['y', y],
        ['width', dx + w + dy + h],
        ['height', w + h],
        ['transform-origin', origin]
    ]
    const mask = document.querySelector('.mask')
    for (let [k, v] of maskAttrs) {
        mask.setAttribute(k, v)
    }

    const back = document.querySelector('.back')
    back.setAttribute('transform-origin', origin)

    const flood = document.querySelector('#flood > feFlood')
    flood.setAttribute('flood-color', backColor)
    flood.setAttribute('flood-opacity', 1 - paperTransparency)

    return [{
            targets: mask,
            rotate: [`${a0}rad`, `${a1}rad`],
            duration
        },
        {
            targets: back,
            rotate: [`${2 * a0}rad`, `${2 * a1}rad`],
            scaleY: [-1, -1],
            duration
        }
    ]
}

function setupPageFade(duration = 1000) {
    return [{
        targets: '.page',
        opacity: [1, 0],
        duration
    }]
}

function setupShowDay(duration = 1000) {
    const easing = 'steps(1)'
    return [{
            targets: '.act-1',
            opacity: [1, 0],
            duration,
            easing
        },
        {
            targets: '.act-2',
            opacity: [0, 1],
            duration,
            easing
        }
    ]
}

function SVGCCPageTurnEffect(filter, filterManager, elem) {
    // filter: A empty SVG filter DOM element

    // filterManger: GroupEffect
    // filterManager.data: the related node in data.json
    // filterManager.effectElements: the related options
    // filterManager.container: SVGCompElement
    // filterManager.dynamicProperties: Animated Property
    // filterManager._mdf

    // elem = sfilterManager.container

    // filterManager.container.globalData

    this.filter = filter
    this.filterManager = filterManager
    this.elem = elem
    this.initialized = false
}

SVGCCPageTurnEffect.prototype.initialize = function () {
    if (this.initialized == false && this.elem.baseElement.ownerSVGElement) {
        // 1. move element to defs
        var svg = SVG(this.elem.baseElement.ownerSVGElement)
        var root = SVG(this.elem.baseElement.parentNode)

        var page = SVG(this.elem.baseElement).id('page')
        svg.defs().add(this.elem.baseElement)
        var mask = svg.mask().id('mask').add(svg.rect().fill('white').addClass('mask'))
        svg.defs().add(mask)
        svg.defs().add(SVG(`<filter id="flood">
        <feFlood
          flood-color="white"
          flood-opacity="0.8"
          result="flood"
        />
        <feComposite
          in="flood"
          in2="SourceGraphic"
          operator="in"
          result="back"
        />
        <feBlend
          in="back"
          in2="SourceGraphic"
        />
      </filter>`))

        var g = root.group()
        this.elem.baseElement = g.node

        g.addClass('page').maskWith(mask)
        g.add(svg.group().addClass('front').add(svg.use(page).addClass('content')))
        g.add(svg.group().addClass('back').add(svg.use(page).addClass('content')))
        g.add(SVG(`<g class="mask-helper">
        <filter id="invert-alpha">
          <feColorMatrix
            type="matrix"
            values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 -1 1"
          />
        </filter>
        <g filter="url(#invert-alpha)">
          <rect
            width="100%"
            height="100%"
            fill="rgba(255, 0, 0, 0.5)"
          />
          <rect
            mask="url(#mask)"
            width="100%"
            height="100%"
            fill="rgba(0, 0, 0, 1)"
          />
        </g>
      </g>`))
        // this.elem

        timeline = setupAnimation()
        this.initialized = true
    }
}

SVGCCPageTurnEffect.prototype.renderFrame = function (forceRender) {
    if (!this.initialized) {
        this.initialize();
    }

};