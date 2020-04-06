/*global anime, createElementID*/
// ref: https://github.com/livingbio/fitgames/issues/2#issuecomment-607055180

function setupPageFlip({
    box,
    back,
    mask,
    feFlood,
}, {
    backColor = 'white',
    paperTransparency = 0,
    fromAngle: a0 = Math.PI / 12,
    toAngle: a1 = Math.PI / 4,
} = {}) {
    const {
        width: w,
        height: h,
    } = box;
    const dx = (h + w * Math.tan(a0)) / (Math.tan(a1) - Math.tan(a0));
    const dy = dx * Math.tan(a1) - h;
    const x = box.x - dx;
    const y = box.y - dy;
    const origin = `${x} ${y}`;
    const maskAttrs = [
        ['x', x],
        ['y', y],
        ['width', dx + w + dy + h],
        ['height', w + h],
        ['transform-origin', origin],
    ];
    maskAttrs.forEach(([k, v]) => mask.setAttribute(k, v));

    back.setAttribute('transform-origin', origin);

    feFlood.setAttribute('flood-color', backColor);
    feFlood.setAttribute('flood-opacity', 1 - paperTransparency);

    return [{
        targets: mask,
        rotate: [`${a0}rad`, `${a1}rad`],
    },
    {
        targets: back,
        rotate: [`${2 * a0}rad`, `${2 * a1}rad`],
        scaleY: [-1, -1],
    }];
}

function setupAnimation(elements, {
    duration = 1000,
    ...options
} = {}) {
    const tl = anime.timeline({
        autoplay: false,
        duration,
        easing: 'cubicBezier(0.25, 0.1, 0.25, 1.0)',
    });
    setupPageFlip(elements, options)
        .forEach((anim) => tl.add(anim, 0));

    return tl;
}

function SVGCCPageTurnEffect(filter, filterManager, elem) {
    filter.setAttribute('id', createElementID());
    elem.globalData.defs.appendChild(filter);

    const feFlood = createNS('feFlood');
    feFlood.setAttribute('result', 'flood');
    filter.appendChild(feFlood);

    const feComposite = createNS('feComposite');
    feComposite.setAttribute('in', 'flood');
    feComposite.setAttribute('in2', 'SourceGraphic');
    feComposite.setAttribute('operator', 'in');
    feComposite.setAttribute('result', 'back');
    filter.appendChild(feComposite);

    const feBlend = createNS('feBlend');
    feBlend.setAttribute('in', 'back');
    feBlend.setAttribute('in2', 'SourceGraphic');
    filter.appendChild(feBlend);

    const mask = createNS('mask');
    mask.setAttribute('id', createElementID());
    const maskRect = createNS('rect');
    maskRect.setAttribute('fill', 'white');
    mask.appendChild(maskRect);
    elem.globalData.defs.appendChild(mask);

    const el = elem.getBaseElement();
    el.setAttribute('mask', `url(#${mask.id})`);

    const back = createNS('g');
    back.setAttribute('filter', `url(#${filter.id})`);

    this.initialize = function () {
        const box = el.getBBox();

        el.children.forEach((child) => {
            child.setAttribute('id', createElementID());
            const backContent = createNS('use');
            backContent.setAttribute('href', `#${child.id}`);
            back.appendChild(backContent);
        });
        el.appendChild(back);
        this.timeline = setupAnimation({
            mask: maskRect,
            box,
            back,
            feFlood,
        });
        this.timeline.seek(0);
        this.initialized = true;
    };
    this.elem = elem;
}

SVGCCPageTurnEffect.prototype.renderFrame = function (forceRender) {
    if (!this.initialized) {
        this.initialize();
    }
    let currentTime = 0;
    if (forceRender) {
        this.startTime = null;
    } else {
        if (!this.startTime) {
            this.startTime = Date.now();
        }
        currentTime = Date.now() - this.startTime;
    }
    this.timeline.seek(currentTime);
};