(function(_ds){var window=this;'use strict';var AL=function(a){var b=a.position,c=a.labels;a=a.Xo;var d="";_ds.zl(b,"footer")&&(d+='<div class="devsite-rating-caption">Was this page helpful?</div>');d+='<div class="devsite-rating-stars">';for(var e=Math.max(0,Math.ceil(c.length)),g=0;g<e;g++){var k=g;d+='<div class="devsite-rating-star devsite-rating-star-outline gc-analytics-event material-icons" data-rating-val="'+_ds.V(k+1)+'" track-metadata-score="'+_ds.V(k+1)+'" track-type="feedback" track-name="rating" track-metadata-position="'+
_ds.V(b)+'" role="button" tabindex="0" data-title="'+_ds.V(a[k])+'" aria-label="'+_ds.V(c[k])+'"></div>'}return(0,_ds.T)(d+"</div>")},BL=function(){return"Unusable documentation"},CL=function(){return"Poor documentation"},DL=function(){return"OK documentation"},EL=function(){return"Good documentation"},FL=function(){return"Excellent documentation"},GL=function(a){return'You rated "'+(a.Of+'"')},HL=function(a){return a.Of},IL=function(){this.h=_ds.tg();this.j=null},JL=function(a,b){a=a(b||{},{});return String(a)},
KL=function(a,b,c){b=b(c||{},{});a.Wc(null,b.sb);return b},LL=function(){var a=_ds.S.call(this)||this;a.h=new _ds.Aj;a.C=["Unusable documentation, with a rating of 1 out of 5","Poor documentation, with a rating of 2 out of 5","OK documentation, with a rating of 3 out of 5","Good documentation, with a rating of 4 out of 5","Excellent documentation, with a rating of 5 out of 5"];a.F=new IL;a.j=0;a.D=["You rated this page 1 out of 5 stars.","You rated this page 2 out of 5 stars.","You rated this page 3 out of 5 stars.",
"You rated this page 4 out of 5 stars.","You rated this page 5 out of 5 stars."];a.m=[];var b=[JL(BL),JL(CL),JL(DL),JL(EL),JL(FL)];a.o=b;return a},NL=function(a){var b="onpointerover"in window?"pointerover":"mouseover",c="onpointerout"in window?"pointerout":"mouseout";a.h.listen(a,["click","keypress"],function(d){var e=d.target;!e.classList.contains("devsite-rating-star")||"click"!==d.type&&13!==d.keyCode||(d=Number(e.getAttribute("data-rating-val")),d!=a.j&&(ML("selected-rating",d),e={nonInteraction:!0,
page:_ds.ji().pathname,referrer:_ds.ji().pathname,ratings_value:d,ratings_count:1},a.dispatchEvent(new CustomEvent("devsite-analytics-pageview",{detail:e,bubbles:!0}))),3>=d&&(e=document.querySelector("devsite-feedback"))&&e.dispatchEvent(new Event("click")),a.setAttribute("aria-label",a.D[d-1]))});a.h.listen(a,[b,"focusin"],function(d){d.target.classList.contains("devsite-rating-star")&&(d=Number(d.target.getAttribute("data-rating-val")),ML("hover-rating-star",d))});a.h.listen(a,[c,"focusout"],function(d){d.target.classList.contains("devsite-rating-star")&&
ML("hover-rating-star",a.j)})},ML=function(a,b){Array.from(document.getElementsByTagName("devsite-page-rating")).forEach(function(c){return c.setAttribute(a,b)})},OL=function(a,b){a.m.forEach(function(c){Number(c.getAttribute("data-rating-val"))<=b?c.classList.add("devsite-rating-star-full"):c.classList.remove("devsite-rating-star-full")})};/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
_ds.f=IL.prototype;_ds.f.Y$=function(a,b){a=_ds.km(a,b,{},this.h);this.Wc(a,_ds.sl);return a};_ds.f.X$=function(a,b){a=_ds.lm(a,b,{},this.h);this.Wc(a,_ds.sl);return a};_ds.f.$$=function(a,b,c){_ds.im(a,b,c,{});this.Wc(a,_ds.sl)};_ds.f.render=function(a,b){a=a(b||{},{});this.Wc(null,a instanceof _ds.rl?a.sb:null);return String(a)};_ds.f.caa=function(a,b){return KL(this,a,b)};_ds.f.aaa=function(a,b){return _ds.tl(KL(this,a,b))};_ds.f.baa=function(a,b){return KL(this,a,b).h()};_ds.f.JD=function(){return this.h};
_ds.f.Wc=_ds.hb;_ds.u(LL,_ds.S);LL.prototype.connectedCallback=function(){var a=_ds.lm(AL,{position:this.getAttribute("position")||"",labels:this.C,Xo:this.o});this.m=Array.from(a.querySelectorAll(".devsite-rating-star"));this.hasAttribute("selected-rating")||this.setAttribute("selected-rating","0");this.hasAttribute("hover-rating-star")||this.setAttribute("hover-rating-star","0");this.appendChild(a);NL(this)};
LL.prototype.attributeChangedCallback=function(a,b,c){if("selected-rating"===a&&null!=b){var d=this.j=Number(c)||0;b=Number(b)||0;var e=d-1,g=b-1;0<b&&5>=b&&this.m[g].setAttribute("data-title",JL(HL,{Of:this.o[g]}));0<d&&5>=d&&this.m[e].setAttribute("data-title",JL(GL,{Of:this.o[e]}))}"hover-rating-star"===a&&OL(this,Number(c)||0)};LL.prototype.disconnectedCallback=function(){_ds.Gj(this.h)};
_ds.l.Object.defineProperties(LL,{observedAttributes:{configurable:!0,enumerable:!0,get:function(){return["selected-rating","hover-rating-star"]}}});LL.prototype.disconnectedCallback=LL.prototype.disconnectedCallback;LL.prototype.attributeChangedCallback=LL.prototype.attributeChangedCallback;LL.prototype.connectedCallback=LL.prototype.connectedCallback;try{window.customElements.define("devsite-page-rating",LL)}catch(a){console.warn("devsite.app.customElement.DevsitePageRating",a)};})(_ds_www);
