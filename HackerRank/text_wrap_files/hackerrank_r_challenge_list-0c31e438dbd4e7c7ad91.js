(window.webpackJsonp=window.webpackJsonp||[]).push([[51],{"5T8g":function(e,t,a){"use strict";a.r(t);a("bWfx");var n=a("lwsE"),r=a.n(n),l=a("W8MJ"),i=a.n(l),c=a("a1gu"),o=a.n(c),s=a("Nsbk"),u=a.n(s),p=a("7W2i"),h=a.n(p),f=a("lSNA"),m=a.n(f),d=(a("f3/d"),a("cDcd")),v=a.n(d),g=a("17x9"),S=a.n(g),b=a("/MKj"),k=a("MGin"),w=a("eOGF"),y=a("5J+W"),C=a("3ESS");a("nq5B");function N(e){var t=e.tutorial,a=e.assetPath;return v.a.createElement("div",{className:"col-md-6"},v.a.createElement(k.Link,{to:"/domains/tutorials/".concat(t.slug),className:"tutorial-tile"},v.a.createElement("img",{src:a("dashboard/".concat(t.slug,".svg")),alt:"Track Image",className:"tutorial-img"}),v.a.createElement("span",{className:"tutorial-name bold"},t.name)))}Object(w.P)("dashboard/.*.svg");var E=function(e){function t(){return r()(this,t),o()(this,u()(t).apply(this,arguments))}return h()(t,e),i()(t,[{key:"render",value:function(){var e=this.props,t=e.track,a=e.chapters,n=e.appUtil.assetPath;return v.a.createElement("div",{className:"b4 tutorials-list-page"},v.a.createElement("div",{className:"container"},v.a.createElement(C.a,{track:t}),v.a.createElement("div",{className:"tutorials-list row"},a.map(function(e){return v.a.createElement(N,{key:e.slug,tutorial:e,assetPath:n})}))))}}]),t}(d.PureComponent);m()(E,"propTypes",{chapters:S.a.arrayOf(S.a.object),track:S.a.object,appUtil:S.a.object}),E=Object(b.b)(function(e){var t=e.community.domains.dict.tutorials;return{chapters:t.chapters,track:{id:t.id,slug:t.slug,name:t.name}}})(E),E=Object(y.a)(E),t.default=E},F39y:function(e,t,a){},H4Rz:function(e,t,a){},MfAl:function(e,t,a){"use strict";a("VRzm");var n=a("MrcO"),r=a("ZaSc"),l=a("Ckvm"),i={};t.a=function(e){return new Promise(function(t,a){if(i[e])t(i[e]);else if(n.a.get(e)){var c=n.a.get(e);i[e]=c,t(c)}else Object(r.g)({url:"".concat(Object(l.b)(),"shorten"),data:{url:encodeURIComponent(e)},success:function(a){var r=a.url;i[e]=r,n.a.set(e,r),t(r)},error:a})})}},MrcO:function(e,t,a){"use strict";var n="undefined"==typeof localStorage?{}:localStorage;function r(){var e;try{e=JSON.parse(n.jStorage)}catch(t){e={}}return e}var l={set:function(e,t){var a=r();a[e]=t,n.jStorage=JSON.stringify(a)},get:function(e){return r()[e]}};"undefined"!=typeof window&&(window.jStorage=l),t.a=l},Vdmo:function(e,t,a){"use strict";a.r(t),a.d(t,"makeTrackChallengesProps",function(){return b}),a.d(t,"mapDispatchToProps",function(){return k}),a.d(t,"mergeProps",function(){return w});var n=a("MVZn"),r=a.n(n),l=(a("0l/t"),a("bWfx"),a("/MKj")),i=a("fvjX"),c=a("peh1"),o=a("iGQG"),s=a("5J+W"),u=a("cK/l"),p=a("LNHK"),h=a("rw7i"),f=a("Z/B0"),m=function(e){return e.community.profile},d=function(e,t){return t.appUtil.params},v=Object(c.createSelector)([function(e,t){return t.appUtil.location},d],function(e,t){var a=t.trackSlug,n=t.chapterSlug;return Object(u.i)(e,a,n)}),g=function(e){return e.community.challenges.challengeList},S=function(e){return e.community.domains.dict},b=function(){return Object(c.createSelector)([m,u.g,g,v,d,S],function(e,t,a,n,r,l){var i=r.trackSlug,c=r.chapterSlug,o=a.challengePages,s=a.current_track,p=o[Object(u.j)(i,n)]||{list:[],firstUnsolvedChallenge:null,total:0},h=p.list,m=p.firstUnsolvedChallenge,d=p.total,v=h.length,g=h.map(function(e){return t[Object(u.k)(e,"master")]});m&&(g=g.filter(function(e){return e.slug!==m.slug}));var S=l[s.slug],b=S.chapterDict;return{challenges:g,currentChallengesCount:v,totalChallenges:d||0,chapters:S.chapters,chapter:b[c],profile:e,filters:n,track:s,firstUnsolvedChallenge:m,listType:f.a.TRACK}})},k=function(e){return{challengeActions:Object(i.b)(p.a,e)}},w=function(e,t,a){var n=e.track,l=void 0===n?{}:n,i=e.filters,c=e.currentChallengesCount,o=e.chapter,s=void 0===o?{}:o;return r()({},e,t,a,{loadChallenges:function(){return t.challengeActions.getTrackChallengeList({trackSlug:l.slug,filters:i,offset:c,limit:Object(u.h)(s.slug)})}})},y=Object(i.d)(s.a,o.b,Object(l.b)(b(),k,w))(h.a);t.default=y},W6q9:function(e,t,a){"use strict";a("2Spj"),a("bWfx"),a("Z2Ku"),a("L9s1"),a("0l/t");var n=a("lwsE"),r=a.n(n),l=a("W8MJ"),i=a.n(l),c=a("a1gu"),o=a.n(c),s=a("Nsbk"),u=a.n(s),p=a("PJYZ"),h=a.n(p),f=a("7W2i"),m=a.n(f),d=a("pVnL"),v=a.n(d),g=a("QILm"),S=a.n(g),b=a("lSNA"),k=a.n(b),w=a("cDcd"),y=a.n(w),C=a("vN+2"),N=a.n(C),E=a("Wt1U"),O=a.n(E),P=a("g+WX"),j=a("1OM/"),A=a("TSYQ"),M=a.n(A),T=(a("byxf"),function(e){function t(e){var a;return r()(this,t),a=o()(this,u()(t).call(this,e)),k()(h()(a),"state",void 0),k()(h()(a),"props",void 0),k()(h()(a),"toggleShowAll",function(){a.setState({showAll:!a.state.showAll})}),k()(h()(a),"handleSearchInput",function(e){var t=e.currentTarget.value,n=a.props.searchCallback;a.setState({searchState:t},function(){n(t)})}),k()(h()(a),"checklistChange",function(e,t){var n=a.props,r=n.value,l=n.onChange,i=t.target.checked,c=O()(r,e.value);i&&c.push(e.value),l(c,e,i)}),a.state={showAll:!e.itemSize,searchState:e.initialSearchState||""},a}return m()(t,e),i()(t,[{key:"getChecklist",value:function(){var e=this.state.searchState,t=this.props,a=t.list;if(t.isSearchable&&e){var n=e.toLowerCase();a=a.filter(function(e){return e.label.toLowerCase().includes(n)})}return a}},{key:"renderSearchBar",value:function(){var e=this.props.searchPlaceholder,t=this.state.searchState;return y.a.createElement(j.a,{className:"checklist-input width-100",type:"text",placeholder:e,onChange:this.handleSearchInput,value:t})}},{key:"renderShowMore",value:function(e){var t=this.props,a=t.itemSize,n=t.showMoreLabel,r=t.showLessLabel,l=this.state.showAll;return!!a&&e.length>a&&y.a.createElement("div",{className:"set-footer",onClick:this.toggleShowAll},y.a.createElement("a",{className:"filter-show-more"},l?r:n))}},{key:"render",value:function(){var e=this,t=this.props,a=t.className,n=t.itemSize,r=t.isSearchable,l=t.list,i=t.value,c=t.componentClassName,o=S()(t,["className","itemSize","isSearchable","list","value","componentClassName"]),s=this.state.showAll,u=this.getChecklist(),p=s?u:u.slice(0,Math.min(l.length,n));return y.a.createElement("div",{className:M()("ui-checklist",a)},r&&this.renderSearchBar(),y.a.createElement("ul",{className:"ui-checklist-list"},p.map(function(t,a){var n=void 0!==t.key?t.key:a,r=i.includes(t.value);return y.a.createElement("li",{className:"ui-checklist-list-item",key:n},y.a.createElement("div",{className:"ui-checklist-item-wrap"},y.a.createElement(P.a,v()({},o,{onChange:e.checklistChange.bind(e,t),value:t.value,checked:r,label:t.label,className:c,required:void 0}))))})),this.renderShowMore(u))}}]),t}(w.Component));k()(T,"defaultProps",{searchPlaceholder:"",isSearchable:!1,itemSize:1/0,initialSearchState:"",searchCallback:N.a,className:"",componentClassName:"",showMoreLabel:"More",showLessLabel:"Less",value:[]}),t.a=T},bQgK:function(e,t,a){(function(t){(function(){var a,n,r,l,i,c;"undefined"!=typeof performance&&null!==performance&&performance.now?e.exports=function(){return performance.now()}:null!=t&&t.hrtime?(e.exports=function(){return(a()-i)/1e6},n=t.hrtime,l=(a=function(){var e;return 1e9*(e=n())[0]+e[1]})(),c=1e9*t.uptime(),i=l-c):Date.now?(e.exports=function(){return Date.now()-r},r=Date.now()):(e.exports=function(){return(new Date).getTime()-r},r=(new Date).getTime())}).call(this)}).call(this,a("8oxB"))},byxf:function(e,t,a){},nB3z:function(e,t,a){"use strict";var n=a("lwsE"),r=a.n(n),l=a("W8MJ"),i=a.n(l),c=a("a1gu"),o=a.n(c),s=a("Nsbk"),u=a.n(s),p=a("PJYZ"),h=a.n(p),f=a("7W2i"),m=a.n(f),d=a("lSNA"),v=a.n(d),g=a("cDcd"),S=a("vN+2"),b=a.n(S),k=function(e){function t(){var e,a;r()(this,t);for(var n=arguments.length,l=new Array(n),i=0;i<n;i++)l[i]=arguments[i];return a=o()(this,(e=u()(t)).call.apply(e,[this].concat(l))),v()(h()(a),"currentPromise",null),v()(h()(a),"failedCount",0),v()(h()(a),"state",{optimisticState:a.props.initialValue}),v()(h()(a),"handleToggle",function(e){var t=!a.state.optimisticState;a.setState({optimisticState:t});var n=a.props.action(t,e);a.currentPromise=n,n.catch(function(e){a.failedCount++,a.currentPromise===n&&a.setState(function(e){return{optimisticState:a.failedCount%2==0?e.optimisticState:!e.optimisticState}},function(){a.failedCount=0})})}),a}return m()(t,e),i()(t,[{key:"render",value:function(){return this.props.children(this.state.optimisticState,this.handleToggle)}}]),t}(g.Component);v()(k,"defaultProps",{initialValue:!1,action:b.a}),t.a=k},nq5B:function(e,t,a){},oOaF:function(e,t,a){"use strict";var n=a("pVnL"),r=a.n(n),l=a("QILm"),i=a.n(l),c=a("cDcd"),o=a.n(c),s=a("TSYQ"),u=a.n(s),p=a("vN+2"),h=a.n(p),f=a("nB3z"),m=a("OEX3");a("F39y");function d(e){var t=e.initialValue,a=e.className,n=e.label,l=e.onClick,c=i()(e,["initialValue","className","label","onClick"]);return o.a.createElement(f.a,{initialValue:t,action:l},function(e,t){var l=e?"star-icon-filled":"",i=e?"ui-icon-star-filled":"ui-icon-star";return o.a.createElement(m.b,r()({"aria-label":n(e),className:"star-button",onClick:t},c),o.a.createElement("i",{className:u()(a,"star-icon",i,l)}))})}d.defaultProps={initialValue:!1,label:function(e){return e?"Unstar":"Star"},onClick:h.a},t.a=d},ve2B:function(e,t,a){"use strict";var n=a("lwsE"),r=a.n(n),l=a("W8MJ"),i=a.n(l),c=a("a1gu"),o=a.n(c),s=a("Nsbk"),u=a.n(s),p=a("PJYZ"),h=a.n(p),f=a("7W2i"),m=a.n(f),d=a("lSNA"),v=a.n(d),g=a("cDcd"),S=a.n(g),b=a("TSYQ"),k=a.n(b),w=a("OEX3"),y=a("3N0A"),C=a("Q9J+"),N=(a("H4Rz"),function(e){function t(){var e,a;r()(this,t);for(var n=arguments.length,l=new Array(n),i=0;i<n;i++)l[i]=arguments[i];return a=o()(this,(e=u()(t)).call.apply(e,[this].concat(l))),v()(h()(a),"props",void 0),a}return m()(t,e),i()(t,[{key:"componentDidUpdate",value:function(){this.shouldHideScrollBar()?C.a.hideScrollBars():C.a.showScrollBars()}},{key:"componentWillUnmount",value:function(){C.a.showScrollBars()}},{key:"shouldShowOverlay",value:function(){var e=this.props,t=e.open,a=e.overlay;return t&&a}},{key:"shouldHideScrollBar",value:function(){var e=this.props,t=e.open,a=e.type,n=e.popupTarget;return(this.shouldShowOverlay()||t&&"full-screen"===a)&&!n}},{key:"renderPopup",value:function(){var e=this.props,t=e.children,a=e.type,n=e.handleClose,r=e.className,l=e.popupTarget,i=this.shouldShowOverlay();return S.a.createElement(y.a,{target:l},S.a.createElement("div",{className:k()("fab-popup",r)},i&&S.a.createElement("div",{className:"fab-popup-overlay",onClick:n}),S.a.createElement("div",{className:k()("fab-popup-content","fab-popup-".concat(a))},t)))}},{key:"renderPopupHandle",value:function(){var e=this.props,t=e.icon,a=e.handleOpen,n=e.active;return S.a.createElement(w.c,{className:k()("fab-popup-handle",n?"active":"default"),onClick:a},S.a.createElement("i",{className:k()(t,"fab-popup-icon")}))}},{key:"render",value:function(){return this.props.open?this.renderPopup():this.renderPopupHandle()}}]),t}(g.PureComponent));v()(N,"defaultProps",{type:"menu",overlay:!0,active:!1}),t.a=N},xEkU:function(e,t,a){(function(t){for(var n=a("bQgK"),r="undefined"==typeof window?t:window,l=["moz","webkit"],i="AnimationFrame",c=r["request"+i],o=r["cancel"+i]||r["cancelRequest"+i],s=0;!c&&s<l.length;s++)c=r[l[s]+"Request"+i],o=r[l[s]+"Cancel"+i]||r[l[s]+"CancelRequest"+i];if(!c||!o){var u=0,p=0,h=[];c=function(e){if(0===h.length){var t=n(),a=Math.max(0,1e3/60-(t-u));u=a+t,setTimeout(function(){var e=h.slice(0);h.length=0;for(var t=0;t<e.length;t++)if(!e[t].cancelled)try{e[t].callback(u)}catch(e){setTimeout(function(){throw e},0)}},Math.round(a))}return h.push({handle:++p,callback:e,cancelled:!1}),p},o=function(e){for(var t=0;t<h.length;t++)h[t].handle===e&&(h[t].cancelled=!0)}}e.exports=function(e){return c.call(r,e)},e.exports.cancel=function(){o.apply(r,arguments)},e.exports.polyfill=function(e){e||(e=r),e.requestAnimationFrame=c,e.cancelAnimationFrame=o}}).call(this,a("yLpj"))}}]);
//# sourceMappingURL=https://staging.hackerrank.net/fcore-assets/sourcemaps/hackerrank_r_challenge_list-0c31e438dbd4e7c7ad91.js.map