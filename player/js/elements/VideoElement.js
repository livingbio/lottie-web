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
    this.innerElem.setAttribute('preserveAspectRatio',this.assetData.pr || this.globalData.renderConfig.imagePreserveAspectRatio);

    var videoElem = document.createElementNS('http://www.w3.org/1999/xhtml','video');
    videoElem.setAttribute('muted',''); //iphone suuport - we need to mute audio to allow play/stop video from js
    videoElem.setAttribute('preload','');
    videoElem.setAttribute('loop','loop');
    videoElem.setAttribute('playsinline',''); //for iphone support
    videoElem.setAttribute('width',this.assetData.w);
    videoElem.setAttribute('height',this.assetData.h);
    videoElem.setAttribute('style','object-fit: fill');
    videoElem.setAttribute('src',assetPath);
    this.innerElem.appendChild(videoElem);

    // this.maskedElement = this.innerElem.parentElement;
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

IVideoElement.prototype.show = function() {
    if (this.isInRange && !this.isTransparent){
        if (!this.data.hd) {
            var elem = this.baseElement || this.layerElement;

            if (elem.parentElement.parentElement.getElementsByTagName('g').item(0) != undefined){
                if(elem.getElementsByTagName('video').length !=0) {
                    elem.getElementsByTagName('video').item(0).setAttribute('style',elem.parentElement.parentElement.getAttribute("style"));
                }
            }

            if(elem.getElementsByTagName('video').length !=0 && elem.getElementsByTagName('video')[0].currentTime == 0) {
                elem.getElementsByTagName('video')[0].play();
            }

            elem.style.display = 'block';
        }
        this.hidden = false;
        this._isFirstFrame = true;
    }
};

IVideoElement.prototype.sourceRectAtTime = function() {
    return this.sourceRect;
};
