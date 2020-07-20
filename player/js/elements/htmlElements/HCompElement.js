function HCompElement(data,globalData,comp){
    this.layers = data.layers;
    this.supports3d = !data.hasMask;
    this.completeLayers = false;
    this.pendingElements = [];
    this.elements = this.layers ? createSizedArray(this.layers.length) : [];
    this.initElement(data,globalData,comp);
    this.tm = data.tm ? PropertyFactory.getProp(this,data.tm,0,globalData.frameRate,this) : {_placeholder:true};
}

// var isvideo = false

// function checkVideoLayer(layers){
//     if (layers) {
//         for (var i = layers.length - 1; i >= 0; i--) {
//             if (layers[i].layers != undefined){
//                 checkVideoLayer(layers[i].layers)
//             }

//             if(layers[i].ty == 9) {
//                 isvideo = true;
//             }
//         }}
// }

extendPrototype([HybridRenderer, ICompElement, HBaseElement], HCompElement);
HCompElement.prototype._createBaseContainerElements = HCompElement.prototype.createContainerElements;

HCompElement.prototype.createContainerElements = function(){
    this._createBaseContainerElements();
    //divElement.style.clip = 'rect(0px, '+this.data.w+'px, '+this.data.h+'px, 0px)';
    if (this.data.hasMask) {
        // isvideo = false
        // checkVideoLayer(this.data.layers)
        // if (isvideo != true && this.data.layers[0].ty != 9) {} else {}

        this.svgElement.setAttribute('width',this.data.w);
        this.svgElement.setAttribute('height',this.data.h);
        this.transformedElement = this.baseElement;
    } else {
        this.transformedElement = this.layerElement;
    }
};

HCompElement.prototype.addTo3dContainer = function(elem,pos) {
    var j = 0;
    var nextElement;
    while(j<pos){
        if(this.elements[j] && this.elements[j].getBaseElement){
            nextElement = this.elements[j].getBaseElement();
        }
        j += 1;
    }
    if(nextElement){
        this.layerElement.insertBefore(elem, nextElement);
    } else {
        this.layerElement.appendChild(elem);
    }
}
