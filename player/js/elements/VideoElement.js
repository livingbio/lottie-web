function IVideoElement(data,globalData,comp){
    this.assetData = globalData.getAssetData(data.refId);
    this.initElement(data,globalData,comp);
    this.sourceRect = {top:0,left:0,width:this.assetData.w,height:this.assetData.h};
}

extendPrototype([BaseElement,TransformElement,SVGBaseElement,HierarchyElement,FrameElement,RenderableDOMElement], IVideoElement);

IVideoElement.prototype.createContent = function(){

    var assetPath = this.globalData.getAssetsPath(this.assetData);

    this.innerElem = createNS('foreignObject');
    this.innerElem.setAttribute('width',this.assetData.w+"px");
    this.innerElem.setAttribute('height',this.assetData.h+"px");

    var cont = document.createElementNS('http://www.w3.org/1999/xhtml','video');
    styleDiv(cont);

    cont.setAttribute('muted',''); //iphone suuport - we need to mute audio to allow play/stop video from js
    cont.setAttribute('preload','');
    cont.setAttribute('loop','loop');
    cont.setAttribute('playsinline',''); //for iphone support
    cont.setAttribute('width',this.assetData.w);
    cont.setAttribute('height',this.assetData.h);
    cont.setAttribute('style','object-fit: fill');
    this.innerElem.appendChild(cont);

    this.videoElem = document.createElementNS('http://www.w3.org/1999/xhtml','source');
    this.videoElem.setAttribute('src',assetPath);
    cont.appendChild(this.videoElem);

    this.innerElem.setAttribute('preserveAspectRatio',this.assetData.pr || this.globalData.renderConfig.imagePreserveAspectRatio);
    this.maskedElement = this.innerElem.parent;
    this.layerElement.appendChild(this.innerElem);
};

IVideoElement.prototype.hide = function(){
    if (!this.hidden && (!this.isInRange || this.isTransparent)) {
        var elem = this.baseElement || this.layerElement;

        if (elem.getElementsByTagName('video').length != 0) {
            elem.getElementsByTagName('video')[0].pause();
            elem.getElementsByTagName('video')[0].currentTime = 0;
        }

        elem.style.display = 'none';
        this.hidden = true;
    }
};

IVideoElement.prototype.renderFrame = function(){
    if (this.data.hd || this.hidden) {
        var elem = this.baseElement || this.layerElement;

        if (elem.parentElement.parentElement.getElementsByTagName('g').item(0) != undefined){
            if(elem.getElementsByTagName('video').length !=0) {
                elem.getElementsByTagName('video').item(0).setAttribute('style',elem.parentElement.parentElement.getAttribute("style"));
            }
        }

        if(elem.getElementsByTagName('video').length !=0 && elem.getElementsByTagName('video')[0].currentTime == 0) {
            elem.getElementsByTagName('video')[0].play();
        }

        return;
    }

    this.renderTransform();
    this.renderRenderable();
    this.renderElement();
    this.renderInnerContent();
    if (this._isFirstFrame) {
        this._isFirstFrame = false;
    }
};

IVideoElement.prototype.sourceRectAtTime = function() {
    return this.sourceRect;
}
