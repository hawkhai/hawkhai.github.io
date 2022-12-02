<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml" class="logged-out-marketing-header" lang="en"><head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8" />
<title>celt/cwrs.c · 5a6912d46449cb77e799f6c18f31b3108c5b3780 · Marcus Asteborg / Opus · GitLab</title>
<link rel="preload" href="/assets/application_utilities-6e21d68b1ca9da299256cfb26f7422439a6d11822c228fc18238d1c7d737f1df.css" as="style" type="text/css" />
<link rel="preload" href="/assets/application-67bc0612f9d717c9132e562be68773069c94a2dd9f952b1622c47ab0cb0438b4.css" as="style" type="text/css" />
<link rel="preload" href="/assets/highlight/themes/white-925931f55f1eb5f0fdef8460d44b95748a47b6d0ecf3e9a50587f3686ff7c5bd.css" as="style" type="text/css" />

<meta content="IE=edge" http-equiv="X-UA-Compatible" />
<script>
//&lt;![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: String!\n  $ref: String!\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: [$filePath], ref: $ref) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"xnorpx/opus","ref":"5a6912d46449cb77e799f6c18f31b3108c5b3780","filePath":"celt/cwrs.c","shouldFetchRawText":true}}];

if (gl.startup_calls &amp;&amp; window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall =&gt; {
   gl.startup_calls[apiCall] = {
      fetchCall: fetch(apiCall, {
        // Emulate XHR for Rails AJAX request checks
        headers: {
          'X-Requested-With': 'XMLHttpRequest'
        },
        // fetch won’t send cookies in older browsers, unless you set the credentials init option.
        // We set to `same-origin` which is default value in modern browsers.
        // See https://github.com/whatwg/fetch/pull/585 for more information.
        credentials: 'same-origin'
      })
    };
  });
}
if (gl.startup_graphql_calls &amp;&amp; window.fetch) {
  const headers = {"X-CSRF-Token":"1Ywb9nDJjMDu16qfC8EKZDB4T2o6X0rZogFxHQ+6Hzkrf7g8w94UJVZDdsy7NMXRHsxreqCz8Kq8IabFqq3uAQ==","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.xiph.org/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call =&gt; ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]&gt;
</script>
<link rel="prefetch" href="/assets/webpack/monaco.5a5ad95b.chunk.js" />
<link rel="shortcut icon" type="image/png" href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" id="favicon" data-original-href="/assets/favicon-72a2cad5025aa931d6ea56c3201d1f18e68a8cd39788c7c80d5b2b82aa5143ef.png" />
<style>
@keyframes blinking-dot{0%{opacity:1}25%{opacity:0.4}75%{opacity:0.4}100%{opacity:1}}@keyframes blinking-scroll-button{0%{opacity:0.2}50%{opacity:1}100%{opacity:0.2}}@keyframes gl-spinner-rotate{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}body.ui-indigo{--gl-theme-accent: #6666c4}body.ui-indigo .navbar-gitlab{background-color:#292961}body.ui-indigo .navbar-gitlab .navbar-collapse{color:#d1d1f0}body.ui-indigo .navbar-gitlab .container-fluid .navbar-toggler{border-left:1px solid #6868b9;color:#d1d1f0}body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li&gt;a:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li&gt;a:focus,body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li&gt;button:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li&gt;button:focus,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li&gt;a:hover,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li&gt;a:focus,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li&gt;button:hover,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li&gt;button:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li.active&gt;a,body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li.active&gt;button,body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li.dropdown.show&gt;a,body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li.dropdown.show&gt;button,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li.active&gt;a,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li.active&gt;button,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li.dropdown.show&gt;a,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li.dropdown.show&gt;button{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .navbar-sub-nav&gt;li.line-separator,body.ui-indigo .navbar-gitlab .navbar-nav&gt;li.line-separator{border-left:1px solid rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav&gt;li{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav&gt;li.header-search-new{color:#333238}body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a .notification-dot{border:2px solid #292961}body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a.header-help-dropdown-toggle .notification-dot{background-color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a.header-user-dropdown-toggle .header-user-avatar{border-color:#d1d1f0}@media (min-width: 576px){body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a:hover,body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a:focus{background-color:rgba(209,209,240,0.2)}}body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a:hover svg,body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a:focus svg{fill:currentColor}body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a:focus .notification-dot{will-change:border-color, background-color;border-color:#4a4a82}body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a.header-help-dropdown-toggle:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav&gt;li&gt;a.header-help-dropdown-toggle:focus .notification-dot{background-color:#fff}body.ui-indigo .navbar-gitlab .nav&gt;li.active&gt;a,body.ui-indigo .navbar-gitlab .nav&gt;li.dropdown.show&gt;a{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .nav&gt;li.active&gt;a:hover svg,body.ui-indigo .navbar-gitlab .nav&gt;li.dropdown.show&gt;a:hover svg{fill:#292961}body.ui-indigo .navbar-gitlab .nav&gt;li.active&gt;a .notification-dot,body.ui-indigo .navbar-gitlab .nav&gt;li.dropdown.show&gt;a .notification-dot{border-color:#fff}body.ui-indigo .navbar-gitlab .nav&gt;li.active&gt;a.header-help-dropdown-toggle .notification-dot,body.ui-indigo .navbar-gitlab .nav&gt;li.dropdown.show&gt;a.header-help-dropdown-toggle .notification-dot{background-color:#292961}body.ui-indigo .navbar-gitlab .nav&gt;li .impersonated-user svg,body.ui-indigo .navbar-gitlab .nav&gt;li .impersonated-user:hover svg{fill:#292961}body.ui-indigo .navbar .title&gt;a:hover,body.ui-indigo .navbar .title&gt;a:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .header-search{background-color:rgba(209,209,240,0.2) !important;border-radius:4px}body.ui-indigo .header-search:hover{background-color:rgba(209,209,240,0.3) !important}body.ui-indigo .header-search svg.gl-search-box-by-type-search-icon{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input{background-color:transparent;color:rgba(209,209,240,0.8);box-shadow:inset 0 0 0 1px rgba(209,209,240,0.4)}body.ui-indigo .header-search input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input:focus::placeholder,body.ui-indigo .header-search input:active::placeholder{color:#89888d}body.ui-indigo .header-search .keyboard-shortcut-helper{color:#d1d1f0;background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form{background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form:hover{background-color:rgba(209,209,240,0.3)}body.ui-indigo .search .search-input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .search .search-input-wrap .search-icon,body.ui-indigo .search .search-input-wrap .clear-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .search.search-active form{background-color:#fff}body.ui-indigo .search.search-active .search-input-wrap .search-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .search-sidebar .nav-link.active,body.ui-indigo .search-sidebar .nav-link:hover{background-color:rgba(236,236,239,0.8);color:#333238}body.ui-indigo .nav-sidebar li.active&gt;a{color:#333238}body.ui-indigo .nav-sidebar .fly-out-top-item a,body.ui-indigo .nav-sidebar .fly-out-top-item a:hover,body.ui-indigo .nav-sidebar .fly-out-top-item.active a,body.ui-indigo .nav-sidebar .fly-out-top-item .fly-out-top-item-container{background-color:var(--gray-100, #ececef);color:var(--gray-900, #333238)}body.ui-indigo .branch-header-title{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active.is-right{box-shadow:inset -3px 0 #4b4ba3}

*,*::before,*::after{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15}aside,header{display:block}body{margin:0;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:1rem;font-weight:400;line-height:1.5;color:#333238;text-align:left;background-color:#fff}ul{margin-top:0;margin-bottom:1rem}ul ul{margin-bottom:0}strong{font-weight:bolder}a{color:#1f75cb;text-decoration:none;background-color:transparent}a:not([href]):not([class]){color:inherit;text-decoration:none}kbd{font-family:"Menlo", "DejaVu Sans Mono", "Liberation Mono", "Consolas", "Ubuntu Mono", "Courier New", "andale mono", "lucida console", monospace;font-size:1em}img{vertical-align:middle;border-style:none}svg{overflow:hidden;vertical-align:middle}button{border-radius:0}input,button{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button{text-transform:none}[role="button"]{cursor:pointer}button:not(:disabled),[type="button"]:not(:disabled){cursor:pointer}button::-moz-focus-inner,[type="button"]::-moz-focus-inner{padding:0;border-style:none}[type="search"]{outline-offset:-2px}.list-unstyled{padding-left:0;list-style:none}kbd{padding:0.2rem 0.4rem;font-size:90%;color:#fff;background-color:#333238;border-radius:0.2rem}kbd kbd{padding:0;font-size:100%;font-weight:600}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.form-control{display:block;width:100%;height:34px;padding:0.375rem 0.75rem;font-size:0.875rem;font-weight:400;line-height:1.5;color:#333238;background-color:#fff;background-clip:padding-box;border:1px solid #89888d;border-radius:0.25rem}.form-control:-moz-focusring{color:transparent;text-shadow:0 0 0 #333238}.form-control::placeholder{color:#626168;opacity:1}.form-control:disabled{background-color:#fbfafd;opacity:1}.form-inline{display:flex;flex-flow:row wrap;align-items:center}@media (min-width: 576px){.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}}.btn{display:inline-block;font-weight:400;color:#333238;text-align:center;vertical-align:middle;-webkit-user-select:none;user-select:none;background-color:transparent;border:1px solid transparent;padding:0.375rem 0.75rem;font-size:1rem;line-height:20px;border-radius:0.25rem}.btn:disabled{opacity:0.65}.btn:not(:disabled):not(.disabled){cursor:pointer}.collapse:not(.show){display:none}.dropdown{position:relative}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:10rem;padding:0.5rem 0;margin:0.125rem 0 0;font-size:1rem;color:#333238;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,0.15);border-radius:0.25rem}.nav{display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.navbar{position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:0.25rem 0.5rem}.navbar .container-fluid{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between}.navbar-nav{display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:0.25rem 0.75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:0.25rem}@media (max-width: 575.98px){.navbar-expand-sm&gt;.container-fluid{padding-right:0;padding-left:0}}@media (min-width: 576px){.navbar-expand-sm{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm&gt;.container-fluid{flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:flex !important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}}.badge{display:inline-block;padding:0.25em 0.4em;font-size:75%;font-weight:600;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:0.25rem}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.badge-pill{padding-right:0.6em;padding-left:0.6em;border-radius:10rem}.badge-success{color:#fff;background-color:#108548}.badge-info{color:#fff;background-color:#1f75cb}.badge-warning{color:#fff;background-color:#ab6100}.rounded-circle{border-radius:50% !important}.d-none{display:none !important}.d-block{display:block !important}@media (min-width: 576px){.d-sm-none{display:none !important}.d-sm-inline-block{display:inline-block !important}}@media (min-width: 768px){.d-md-block{display:block !important}}@media (min-width: 992px){.d-lg-none{display:none !important}}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border:0}.gl-avatar{border-width:1px;border-style:solid;border-color:rgba(31,30,36,0.08);overflow:hidden;flex-shrink:0}.gl-avatar-s24{width:1.5rem;height:1.5rem;font-size:0.75rem;line-height:1rem;border-radius:0.25rem}.gl-avatar-circle{border-radius:50%}.gl-badge{display:inline-flex;align-items:center;font-size:0.75rem;font-weight:400;line-height:1rem;padding-top:0.25rem;padding-bottom:0.25rem;padding-left:0.5rem;padding-right:0.5rem}.gl-badge.sm{padding-top:0;padding-bottom:0}.gl-badge.badge-info{background-color:#cbe2f9;color:#0b5cad}a.gl-badge.badge-info.active,a.gl-badge.badge-info:active{color:#033464;background-color:#9dc7f1}a.gl-badge.badge-info:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-badge.badge-success{background-color:#c3e6cd;color:#24663b}a.gl-badge.badge-success.active,a.gl-badge.badge-success:active{color:#0a4020;background-color:#91d4a8}a.gl-badge.badge-success:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-badge.badge-warning{background-color:#f5d9a8;color:#8f4700}a.gl-badge.badge-warning.active,a.gl-badge.badge-warning:active{color:#5c2900;background-color:#e9be74}a.gl-badge.badge-warning:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-button .gl-badge{top:0}.gl-form-input,.gl-form-input.form-control{background-color:#fff;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:0.875rem;line-height:1rem;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;height:auto;color:#333238;box-shadow:inset 0 0 0 1px #89888d;border-style:none;-webkit-appearance:none;appearance:none;-moz-appearance:none}.gl-form-input:disabled,.gl-form-input:not(.form-control-plaintext):not([type="color"]):read-only,.gl-form-input.form-control:disabled,.gl-form-input.form-control:not(.form-control-plaintext):not([type="color"]):read-only{background-color:#fbfafd;box-shadow:inset 0 0 0 1px #dcdcde}.gl-form-input:disabled,.gl-form-input.form-control:disabled{cursor:not-allowed;color:#737278}.gl-form-input::placeholder,.gl-form-input.form-control::placeholder{color:#89888d}.gl-icon{fill:currentColor}.gl-icon.s12{width:12px;height:12px}.gl-icon.s16{width:16px;height:16px}.gl-icon.s32{width:32px;height:32px}.gl-link{font-size:0.875rem;color:#1f75cb}.gl-link:active{color:#0b5cad}.gl-link:active{text-decoration:underline;outline:2px solid #428fdc;outline-offset:2px}.gl-button{display:inline-flex}.gl-button:not(.btn-link):active{text-decoration:none}.gl-button.gl-button{border-width:0;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;background-color:transparent;line-height:1rem;color:#333238;fill:currentColor;box-shadow:inset 0 0 0 1px #bfbfc3;justify-content:center;align-items:center;font-size:0.875rem;border-radius:0.25rem}.gl-button.gl-button.btn-default{background-color:#fff}.gl-button.gl-button.btn-default:active,.gl-button.gl-button.btn-default.active{box-shadow:inset 0 0 0 1px #626168, 0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none;background-color:#dcdcde}.gl-button.gl-button.btn-default:active .gl-icon,.gl-button.gl-button.btn-default.active .gl-icon{color:#333238}.gl-button.gl-button.btn-default .gl-icon{color:#737278}.gl-search-box-by-type-search-icon{margin:0.5rem;color:#737278;width:1rem;position:absolute}.gl-search-box-by-type{display:flex;position:relative}.gl-search-box-by-type-input,.gl-search-box-by-type-input.gl-form-input{height:2rem;padding-right:2rem;padding-left:1.75rem}body{font-size:0.875rem}button,html [type="button"],[role="button"]{cursor:pointer}strong{font-weight:bold}svg{vertical-align:baseline}.form-control,.search form{font-size:0.875rem}.hidden{display:none !important;visibility:hidden !important}.hide{display:none}.badge:not(.gl-badge){padding:4px 5px;font-size:12px;font-style:normal;font-weight:400;display:inline-block}.divider{height:0;margin:4px 0;overflow:hidden;border-top:1px solid #dcdcde}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left{color:#737278}html{overflow-y:scroll}@media (min-width: 576px){.logged-out-marketing-header{--header-height: 72px}}.btn{border-radius:4px;font-size:0.875rem;font-weight:400;padding:6px 10px;background-color:#fff;border-color:#dcdcde;color:#333238;color:#333238;white-space:nowrap}.btn:active{background-color:#ececef;box-shadow:none}.btn:active,.btn.active{background-color:#eaeaea;border-color:#e3e3e3;color:#333238}.btn svg{height:15px;width:15px}.btn svg:not(:last-child){margin-right:5px}.badge.badge-pill:not(.gl-badge){font-weight:400;background-color:rgba(0,0,0,0.07);color:#535158;vertical-align:baseline}.gl-font-sm{font-size:12px}.dropdown{position:relative}.dropdown-menu-toggle:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.search-input-container .dropdown-menu{margin-top:11px}.dropdown-menu-toggle{padding:6px 8px 6px 10px;background-color:#fff;color:#333238;font-size:14px;text-align:left;border:1px solid #dcdcde;border-radius:0.25rem;white-space:nowrap}.dropdown-menu-toggle.no-outline{outline:0}.dropdown-menu-toggle.dropdown-menu-toggle{justify-content:flex-start;overflow:hidden;padding-right:25px;position:relative;text-overflow:ellipsis;width:160px}.dropdown-menu{display:none;position:absolute;width:auto;top:100%;z-index:300;min-width:240px;max-width:500px;margin-top:4px;margin-bottom:24px;font-size:0.875rem;font-weight:400;padding:8px 0;background-color:#fff;border:1px solid #dcdcde;border-radius:0.25rem;box-shadow:0 2px 4px rgba(0,0,0,0.1)}.dropdown-menu ul{margin:0;padding:0}.dropdown-menu li{display:block;text-align:left;list-style:none}.dropdown-menu li&gt;a,.dropdown-menu li button{background:transparent;border:0;border-radius:0;box-shadow:none;display:block;font-weight:400;position:relative;padding:8px 12px;color:#333238;line-height:16px;white-space:normal;overflow:hidden;text-align:left;width:100%}.dropdown-menu li&gt;a:active,.dropdown-menu li button:active{background-color:#ececef;color:#333238;outline:0;text-decoration:none}.dropdown-menu li&gt;a:active,.dropdown-menu li button:active{box-shadow:inset 0 0 0 2px #428fdc, inset 0 0 0 3px #fff, inset 0 0 0 1px #fff;outline:none}.dropdown-menu .divider{height:1px;margin:0.25rem 0;padding:0;background-color:#dcdcde}.dropdown-menu .badge.badge-pill+span:not(.badge):not(.badge-pill){margin-right:40px}@media (max-width: 575.98px){.navbar-gitlab li.dropdown{position:static}.navbar-gitlab li.dropdown.user-counter{margin-left:8px !important}.navbar-gitlab li.dropdown.user-counter&gt;a{padding:0 4px !important}header.navbar-gitlab .dropdown .dropdown-menu{width:100%;min-width:100%}}@media (max-width: 767.98px){.dropdown-menu-toggle.dropdown-menu-toggle{width:100%}}input{border-radius:0.25rem;color:#333238;background-color:#fff}.form-control{border-radius:4px;padding:6px 10px}.form-control::placeholder{color:#89888d}kbd{display:inline-block;padding:3px 5px;font-size:0.6875rem;line-height:10px;color:var(--gray-700, #535158);vertical-align:middle;background-color:var(--gray-10, #fbfafd);border-width:1px;border-style:solid;border-color:var(--gray-100, #dcdcde) var(--gray-100, #dcdcde) var(--gray-200, #bfbfc3);border-image:none;border-radius:3px;box-shadow:0 -1px 0 var(--gray-200, #bfbfc3) inset}.navbar-gitlab{padding:0 16px;z-index:1000;margin-bottom:0;min-height:var(--header-height, 48px);border:0;position:fixed;top:0;left:0;right:0;border-radius:0}.navbar-gitlab .close-icon{display:none}.navbar-gitlab .header-content{width:100%;display:flex;justify-content:space-between;position:relative;min-height:var(--header-height, 48px);padding-left:0}.navbar-gitlab .header-content .title{padding-right:0;color:currentColor;display:flex;position:relative;margin:0;font-size:18px;vertical-align:top;white-space:nowrap}.navbar-gitlab .header-content .title img{height:24px}.navbar-gitlab .header-content .title a:not(.canary-badge){display:flex;align-items:center;padding:2px 8px;margin:4px 2px 4px -8px;border-radius:4px}.navbar-gitlab .header-content .title a:not(.canary-badge):active{box-shadow:0 0 0 1px rgba(0,0,0,0.6),0 0 0 3px #63a6e9;outline:none}.navbar-gitlab .header-content .navbar-collapse&gt;ul.nav&gt;li:not(.d-none){margin:0 2px}.navbar-gitlab .navbar-collapse{flex:0 0 auto;border-top:0;padding:0}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse{flex:1 1 auto}}.navbar-gitlab .navbar-collapse .nav{flex-wrap:nowrap}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse .nav&gt;li:not(.d-none) a{margin-left:0}}.navbar-gitlab .container-fluid{padding:0}.navbar-gitlab .container-fluid .user-counter svg{margin-right:3px}.navbar-gitlab .container-fluid .navbar-toggler{position:relative;right:-10px;border-radius:0;min-width:45px;padding:0;margin:8px 8px 8px 0;font-size:14px;text-align:center;color:currentColor}.navbar-gitlab .container-fluid .navbar-toggler.active{color:currentColor;background-color:transparent}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .navbar-nav{display:flex;padding-right:10px;flex-direction:row}}.navbar-gitlab .container-fluid .navbar-nav li .badge.badge-pill:not(.gl-badge){box-shadow:none;font-weight:600}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav&gt;li.header-user{padding-left:10px}}.navbar-gitlab .container-fluid .nav&gt;li&gt;a{will-change:color;margin:4px 0;padding:6px 8px;height:32px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav&gt;li&gt;a{padding:0}}.navbar-gitlab .container-fluid .nav&gt;li&gt;a.header-user-dropdown-toggle{margin-left:2px}.navbar-gitlab .container-fluid .nav&gt;li&gt;a.header-user-dropdown-toggle .header-user-avatar{margin-right:0}.navbar-gitlab .container-fluid .nav&gt;li .header-new-dropdown-toggle{margin-right:0}.navbar-sub-nav&gt;li&gt;a,.navbar-sub-nav&gt;li&gt;button,.navbar-nav&gt;li&gt;a,.navbar-nav&gt;li&gt;button{display:flex;align-items:center;justify-content:center;padding:6px 8px;margin:4px 2px;font-size:12px;color:currentColor;border-radius:4px;height:32px;font-weight:600}.navbar-sub-nav&gt;li&gt;a:active,.navbar-sub-nav&gt;li&gt;button:active,.navbar-nav&gt;li&gt;a:active,.navbar-nav&gt;li&gt;button:active{box-shadow:0 0 0 1px rgba(0,0,0,0.6),0 0 0 3px #63a6e9;outline:none}.navbar-sub-nav&gt;li .top-nav-toggle,.navbar-sub-nav&gt;li&gt;button,.navbar-nav&gt;li .top-nav-toggle,.navbar-nav&gt;li&gt;button{background:transparent;border:0}.navbar-sub-nav .dropdown-menu,.navbar-nav .dropdown-menu{position:absolute}.navbar-sub-nav{display:flex;align-items:center;height:100%;margin:0 0 0 6px}.caret-down,.btn .caret-down{top:0;height:11px;width:11px;margin-left:4px;fill:currentColor}.header-user .dropdown-menu,.header-new .dropdown-menu{margin-top:4px}.btn-sign-in{background-color:#ebebfa;color:#292961;font-weight:600;line-height:18px;margin:4px 0 4px 2px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid{font-size:18px}.navbar-gitlab .container-fluid .navbar-nav{table-layout:fixed;width:100%;margin:0;text-align:right}.navbar-gitlab .container-fluid .navbar-collapse{margin-left:-8px;margin-right:-10px}.navbar-gitlab .container-fluid .navbar-collapse .nav&gt;li:not(.d-none){flex:1}.header-user-dropdown-toggle{text-align:center}.header-user-avatar{float:none}}.header-user-avatar{float:left;margin-right:5px;border-radius:50%;border:1px solid #f2f2f4}.notification-dot{background-color:#d99530;height:12px;width:12px;pointer-events:none;visibility:hidden;top:3px}.tanuki-logo .tanuki{fill:#e24329}.tanuki-logo .left-cheek,.tanuki-logo .right-cheek{fill:#fc6d26}.tanuki-logo .chin{fill:#fca326}.context-header{position:relative;margin-right:2px;width:256px}.context-header&gt;a,.context-header&gt;button{font-weight:600;display:flex;width:100%;align-items:center;padding:10px 16px 10px 10px;color:#333238;background-color:transparent;border:0;text-align:left}.context-header .avatar-container{flex:0 0 32px;background-color:#fff}.context-header .sidebar-context-title{overflow:hidden;text-overflow:ellipsis;color:#333238}@media (min-width: 768px){.page-with-contextual-sidebar{padding-left:56px}}@media (min-width: 1200px){.page-with-contextual-sidebar{padding-left:256px}}@media (min-width: 768px){.page-with-icon-sidebar{padding-left:56px}}.nav-sidebar{position:fixed;bottom:0;left:0;z-index:600;width:256px;top:var(--header-height, 48px);background-color:#fbfafd;border-right:1px solid #e9e9e9;transform:translate3d(0, 0, 0)}.nav-sidebar.sidebar-collapsed-desktop{width:56px}.nav-sidebar.sidebar-collapsed-desktop .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar.sidebar-collapsed-desktop .badge.badge-pill:not(.fly-out-badge),.nav-sidebar.sidebar-collapsed-desktop .nav-item-name,.nav-sidebar.sidebar-collapsed-desktop .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar.sidebar-collapsed-desktop .sidebar-top-level-items&gt;li&gt;a{min-height:unset}.nav-sidebar.sidebar-collapsed-desktop .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar.sidebar-collapsed-desktop .avatar-container{margin:0 auto}.nav-sidebar.sidebar-collapsed-desktop li.active:not(.fly-out-top-item)&gt;a{background-color:rgba(41,41,97,0.08)}.nav-sidebar a{text-decoration:none;color:#333238}.nav-sidebar li{white-space:nowrap}.nav-sidebar li .nav-item-name{flex:1;overflow:hidden;text-overflow:ellipsis}.nav-sidebar li&gt;a,.nav-sidebar li&gt;.fly-out-top-item-container{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 8px}.nav-sidebar li.active&gt;a{font-weight:600}.nav-sidebar li.active:not(.fly-out-top-item)&gt;a:not(.has-sub-items){background-color:rgba(0,0,0,0.08)}.nav-sidebar ul{padding-left:0;list-style:none}@media (max-width: 767.98px){.nav-sidebar{left:-256px}}.nav-sidebar .nav-icon-container{display:flex;margin-right:8px}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:-0.25rem;margin-bottom:-0.25rem;margin-top:0;position:relative;color:#fff;background:var(--black, #000)}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container strong{font-weight:400}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container::before{position:absolute;content:"";display:block;top:50%;left:-0.25rem;margin-top:-0.25rem;width:0;height:0;border-top:0.25rem solid transparent;border-bottom:0.25rem solid transparent;border-right:0.25rem solid #000;border-right-color:var(--black, #000)}@media (min-width: 576px){.nav-sidebar a.has-sub-items+.sidebar-sub-level-items{min-width:150px}}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:0;border-bottom-left-radius:0;border-bottom-right-radius:0}@media (min-width: 768px) and (max-width: 1199px){.nav-sidebar:not(.sidebar-expanded-mobile){width:56px}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar:not(.sidebar-expanded-mobile) .badge.badge-pill:not(.fly-out-badge),.nav-sidebar:not(.sidebar-expanded-mobile) .nav-item-name,.nav-sidebar:not(.sidebar-expanded-mobile) .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items&gt;li&gt;a{min-height:unset}.nav-sidebar:not(.sidebar-expanded-mobile) .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar:not(.sidebar-expanded-mobile) .avatar-container{margin:0 auto}.nav-sidebar:not(.sidebar-expanded-mobile) li.active:not(.fly-out-top-item)&gt;a{background-color:rgba(41,41,97,0.08)}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:60px;width:56px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:10px 4px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:auto}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:0.25rem}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items&gt;li .sidebar-sub-level-items:not(.flyout-list){display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-icon-container{margin-right:0}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button{width:55px;padding:0 21px}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .collapse-text{display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}}.nav-sidebar-inner-scroll{height:100%;width:100%;overflow-x:hidden;overflow-y:auto}.nav-sidebar-inner-scroll&gt;div.context-header{margin-top:0.25rem}.nav-sidebar-inner-scroll&gt;div.context-header a{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 8px;padding:0.25rem;margin-bottom:0.25rem;margin-top:0.125rem}.nav-sidebar-inner-scroll&gt;div.context-header a .avatar-container{font-weight:400;flex:none}.sidebar-top-level-items{margin-bottom:60px}.sidebar-top-level-items .context-header a{padding:0.25rem;margin-bottom:0.25rem;margin-top:0.125rem}.sidebar-top-level-items .context-header a .avatar-container{font-weight:400;flex:none}.sidebar-top-level-items&gt;li.active .sidebar-sub-level-items:not(.is-fly-out-only){display:block}.sidebar-top-level-items li&gt;a.gl-link{color:#333238}.sidebar-top-level-items li&gt;a.gl-link:active{text-decoration:none}.sidebar-sub-level-items{padding-top:0;padding-bottom:0;display:none}.sidebar-sub-level-items:not(.fly-out-list) li&gt;a{padding-left:2.25rem}.toggle-sidebar-button,.close-nav-button{height:48px;padding:0 16px;background-color:#fbfafd;border:0;color:#737278;display:flex;align-items:center;background-color:#fbfafd;position:fixed;bottom:0;width:255px}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left,.close-nav-button .collapse-text,.close-nav-button .icon-chevron-double-lg-left{color:inherit}.collapse-text{white-space:nowrap;overflow:hidden}.sidebar-collapsed-desktop .context-header{height:60px;width:56px}.sidebar-collapsed-desktop .context-header a{padding:10px 4px}.sidebar-collapsed-desktop .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.sidebar-collapsed-desktop .context-header{height:auto}.sidebar-collapsed-desktop .context-header a{padding:0.25rem}.sidebar-collapsed-desktop .sidebar-top-level-items&gt;li .sidebar-sub-level-items:not(.flyout-list){display:none}.sidebar-collapsed-desktop .nav-icon-container{margin-right:0}.sidebar-collapsed-desktop .toggle-sidebar-button{width:55px;padding:0 21px}.sidebar-collapsed-desktop .toggle-sidebar-button .collapse-text{display:none}.sidebar-collapsed-desktop .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}.close-nav-button{display:none}@media (max-width: 767.98px){.close-nav-button{display:flex}.toggle-sidebar-button{display:none}}input::-moz-placeholder{color:#89888d;opacity:1}input::-ms-input-placeholder{color:#89888d}input:-ms-input-placeholder{color:#89888d}svg{fill:currentColor}svg.s12{width:12px;height:12px}svg.s16{width:16px;height:16px}svg.s32{width:32px;height:32px}svg.s12{vertical-align:-1px}svg.s16{vertical-align:-3px}.header-content .header-search-new{max-width:640px}.header-search{min-width:320px}@media (min-width: 768px) and (max-width: 1199.98px){.header-search{min-width:200px}}.header-search .keyboard-shortcut-helper{transform:translateY(calc(50% - 2px));box-shadow:none;border-color:transparent}.search{margin:0 8px}.search form{display:block;margin:0;padding:4px;width:200px;line-height:24px;height:32px;border:0;border-radius:4px}@media (min-width: 1200px){.search form{width:320px}}.search .search-input{border:0;font-size:14px;padding:0 20px 0 0;margin-left:5px;line-height:25px;width:98%;color:#fff;background:none}.search .search-input-container{display:flex;position:relative}.search .search-input-wrap{width:100%}.search .search-input-wrap .search-icon,.search .search-input-wrap .clear-icon{position:absolute;right:5px;top:4px}.search .search-input-wrap .search-icon{-webkit-user-select:none;user-select:none}.search .search-input-wrap .clear-icon{display:none}.search .search-input-wrap .dropdown{position:static}.search .search-input-wrap .dropdown-menu{left:-5px;max-height:400px;overflow:auto}@media (min-width: 1200px){.search .search-input-wrap .dropdown-menu{width:320px}}.search .identicon{flex-basis:16px;flex-shrink:0;margin-right:4px}.avatar,.avatar-container{float:left;margin-right:16px;border-radius:50%}.avatar.s16,.avatar-container.s16{width:16px;height:16px;margin-right:8px}.avatar.s32,.avatar-container.s32{width:32px;height:32px;margin-right:8px}.avatar{transition-property:none;width:40px;height:40px;padding:0;background:#fefefe;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(31,30,36,0.1)}.avatar.avatar-tile{border-radius:0;border:0}.identicon{text-align:center;vertical-align:top;color:#333238;background-color:#ececef}.identicon.s16{font-size:10px;line-height:16px}.identicon.s32{font-size:14px;line-height:32px}.identicon.bg1{background-color:#fcf1ef}.identicon.bg2{background-color:#f4f0ff}.identicon.bg3{background-color:#f1f1ff}.identicon.bg4{background-color:#e9f3fc}.identicon.bg5{background-color:#ecf4ee}.identicon.bg6{background-color:#fdf1dd}.identicon.bg7{background-color:#ececef}.avatar-container{overflow:hidden;display:flex}.avatar-container a{width:100%;height:100%;display:flex;text-decoration:none}.avatar-container .avatar{border-radius:0;border:0;height:auto;width:100%;margin:0;align-self:center}.rect-avatar{border-radius:2px}.rect-avatar.s16{border-radius:2px}.rect-avatar.s16 .avatar{border-radius:2px}.rect-avatar.s32{border-radius:4px}.rect-avatar.s32 .avatar{border-radius:4px}.tab-width-8{tab-size:8}.gl-sr-only{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.gl-border-none\!{border-style:none !important}.gl-display-none{display:none}@media (min-width: 576px){.gl-sm-display-none{display:none}}.gl-display-flex{display:flex}@media (min-width: 992px){.gl-lg-display-flex{display:flex}}@media (min-width: 576px){.gl-sm-display-block{display:block}}@media (min-width: 992px){.gl-lg-display-block{display:block}}.gl-align-items-center{align-items:center}.gl-align-items-stretch{align-items:stretch}.gl-flex-grow-1{flex-grow:1}.gl-justify-content-end{justify-content:flex-end}.gl-relative{position:relative}.gl-absolute{position:absolute}.gl-top-0{top:0}.gl-right-3{right:0.5rem}.gl-w-full{width:100%}.gl-px-3{padding-left:0.5rem;padding-right:0.5rem}.gl-pr-2{padding-right:0.25rem}.gl-pt-0{padding-top:0}.gl-mr-auto{margin-right:auto}.gl-mr-3{margin-right:0.5rem}.gl-ml-n2{margin-left:-0.25rem}.gl-ml-3{margin-left:0.5rem}.gl-mx-0\!{margin-left:0 !important;margin-right:0 !important}.gl-text-right{text-align:right}.gl-white-space-nowrap{white-space:nowrap}.gl-font-sm{font-size:0.75rem}.gl-font-weight-bold{font-weight:600}.gl-z-index-1{z-index:1}.cloak-startup,.content-wrapper&gt;.alert-wrapper,#content-body,.modal-dialog{display:none}

</style>


<link rel="stylesheet" media="all" href="/assets/application-67bc0612f9d717c9132e562be68773069c94a2dd9f952b1622c47ab0cb0438b4.css" data-startupcss="loaded" />
<link rel="stylesheet" media="all" href="/assets/page_bundles/tree-28bc93087ca1345e26583661b19e340e319d368cc7967e6b5811102349a4d026.css" data-startupcss="loaded" />
<link rel="stylesheet" media="all" href="/assets/application_utilities-6e21d68b1ca9da299256cfb26f7422439a6d11822c228fc18238d1c7d737f1df.css" data-startupcss="loaded" />


<link rel="stylesheet" media="all" href="/assets/highlight/themes/white-925931f55f1eb5f0fdef8460d44b95748a47b6d0ecf3e9a50587f3686ff7c5bd.css" data-startupcss="loaded" />
<script>
//&lt;![CDATA[
document.querySelectorAll('link[media="print"]').forEach(linkTag =&gt; {
  linkTag.setAttribute('data-startupcss', 'loading');
  const startupLinkLoadedEvent = new CustomEvent('CSSStartupLinkLoaded');
  linkTag.addEventListener('load',function(){this.media='all';this.setAttribute('data-startupcss', 'loaded');document.dispatchEvent(startupLinkLoadedEvent);},{once: true});
})

//]]&gt;
</script>

<script>
//&lt;![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://gitlab.xiph.org/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=50;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.user_color_scheme="white";gon.markdown_surround_selection=null;gon.markdown_automatic_lists=null;gon.recaptcha_api_server_url="https://www.google.com/recaptcha/api.js";gon.recaptcha_sitekey="6LffqyUTAAAAAG5jWurvEFTINZ2obr4iMHlIe_1V";gon.gitlab_url="https://gitlab.xiph.org";gon.revision="7f1a7c62df9";gon.feature_category="source_code_management";gon.gitlab_logo="/assets/gitlab_logo-2957169c8ef64c58616a1ac3f4fc626e8a35ce4eb3ed31bb0d873712f2a041a0.png";gon.secure=true;gon.sprite_icons="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg";gon.sprite_file_icons="/assets/file_icons-958d18a1c33aa82a81e2eb1ffbffc33131d501c41ad95838a70b089e5ffbd7a0.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-e1b1ba2d7a86a445dcb1110d1b6e7dd0200ecaa993a445df77a07537dbf8f475.css";gon.select2_css_path="/assets/lazy_bundles/select2-f3964bfc05fa591b32f66a871083754d3a3161c3c5a63a0a45449cb651d3416a.css";gon.gridstack_css_path="/assets/lazy_bundles/gridstack-f9e005145f1f29d3fd436ec6eda8b264c017ee47886472841ed47e32332518ff.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#009966":"Green-cyan","#8fbc8f":"Dark sea green","#3cb371":"Medium sea green","#00b140":"Green screen","#013220":"Dark green","#6699cc":"Blue-gray","#0000ff":"Blue","#e6e6fa":"Lavender","#9400d3":"Dark violet","#330066":"Deep violet","#808080":"Gray","#36454f":"Charcoal grey","#f7e7ce":"Champagne","#c21e56":"Rose red","#cc338b":"Magenta-pink","#dc143c":"Crimson","#ff0000":"Red","#cd5b45":"Dark coral","#eee600":"Titanium yellow","#ed9121":"Carrot orange","#c39953":"Aztec Gold"};gon.first_day_of_week=0;gon.time_display_relative=true;gon.ee=false;gon.jh=false;gon.dot_com=false;gon.features={"usageDataApi":true,"securityAutoFix":false,"newHeaderSearch":true,"sourceEditorToolbar":false,"integrationSlackAppNotifications":false,"vueGroupSelect":false,"highlightJs":true,"fileLineBlame":false};
//]]&gt;
</script>





<script src="/assets/webpack/runtime.a9e3ec9e.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.57ea2c9f.chunk.js" defer="defer"></script>
<script src="/assets/webpack/graphql.a062ade3.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-IssuablePopoverBundle-pages.admin.application_settings-pages.admin.application_settings.ci_c-69e35067.54210162.chunk.js" defer="defer"></script>
<script src="/assets/webpack/shortcutsBundle.8f8c4616.chunk.js" defer="defer"></script>
<script src="/assets/webpack/5.e7817178.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.boards-pages.groups.details-pages.groups.show-pages.projects-pages.projects.act-ecfb63eb.6e5bec89.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.new-pages.ide-pages.projects-pages.projects.activity-pages.projects.alert_manag-7f73e6eb.4263a9b0.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-c4605bcb.9d785218.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-jira_connect_app-pages.admin.application_settings-pages.admin.application_settings.ci_cd-pag-8a1f10d7.40528169.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.edit-pages.projects.sni-dd84f7c7.91acaaf4.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-25c821a4.60781507.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.forks.new-pages.projects.show-pages.projects.tree.show.9f5719d7.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.21b29a3f.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.e76c73b9.chunk.js" defer="defer"></script>

<meta content="object" property="og:type" />
<meta content="GitLab" property="og:site_name" />
<meta content="celt/cwrs.c · 5a6912d46449cb77e799f6c18f31b3108c5b3780 · Marcus Asteborg / Opus · GitLab" property="og:title" />
<meta content="Official Opus low-latency codec repository" property="og:description" />
<meta content="https://gitlab.xiph.org/uploads/-/system/project/avatar/116/opus-logo-imageonly.png" property="og:image" />
<meta content="64" property="og:image:width" />
<meta content="64" property="og:image:height" />
<meta content="https://gitlab.xiph.org/xnorpx/opus/-/blob/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c" property="og:url" />
<meta content="summary" property="twitter:card" />
<meta content="celt/cwrs.c · 5a6912d46449cb77e799f6c18f31b3108c5b3780 · Marcus Asteborg / Opus · GitLab" property="twitter:title" />
<meta content="Official Opus low-latency codec repository" property="twitter:description" />
<meta content="https://gitlab.xiph.org/uploads/-/system/project/avatar/116/opus-logo-imageonly.png" property="twitter:image" />

<meta content="Official Opus low-latency codec repository" name="description" />
<link href="/-/manifest.json" rel="manifest" />
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport" />
<meta content="#292961" name="theme-color" />
<meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="nMwxNnslDkIuK8COZqmUxCcUKyEPBqrM/K9+s6HJfIdiP5L8yDKWp5a/HN3WXFtxCaAPMZXqEL/ij6lrBN6Nvw==" />
<meta name="csp-nonce" />
<meta name="action-cable-url" content="/-/cable" />
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png" />
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml" />





<script charset="utf-8" src="/assets/webpack/hello.67787be5.chunk.js"></script><script charset="utf-8" src="/assets/webpack/734.b311dbc5.chunk.js"></script><script charset="utf-8" src="/assets/webpack/vendors-globalSearch-top_nav.68a4ee22.chunk.js"></script><script charset="utf-8" src="/assets/webpack/vendors-top_nav.1076b3c1.chunk.js"></script><script charset="utf-8" src="/assets/webpack/top_nav.0177f3d1.chunk.js"></script><script charset="utf-8" src="/assets/webpack/94.a0ed0130.chunk.js"></script><script charset="utf-8" src="/assets/webpack/hl-c.1b477250.chunk.js"></script></head>

<body class="ui-indigo tab-width-8 gl-browser-chrome gl-platform-windows page-initialised" data-find-file="/xnorpx/opus/-/find_file/5a6912d46449cb77e799f6c18f31b3108c5b3780" data-namespace-id="2498" data-page="projects:blob:show" data-page-type-id="5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c" data-project="opus" data-project-id="116">

<script>
//&lt;![CDATA[
gl = window.gl || {};
gl.client = {"isChrome":true,"isWindows":true};


//]]&gt;
</script>



<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<div class="header-content js-header-content">
<div class="title-container hide-when-top-nav-responsive-open gl-transition-medium gl-display-flex gl-align-items-stretch gl-pt-0 gl-mr-3">
<div class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" class="has-tooltip" href="/"><svg class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z" fill="#E24329"/>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z" fill="#FC6D26"/>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z" fill="#FCA326"/>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z" fill="#FC6D26"/>
</svg>

</a></div>
<div class="gl-display-flex gl-align-items-center">
</div>
<ul class="nav navbar-sub-nav gl-display-none gl-lg-display-flex gl-align-items-center">
<li class="dropdown gl-mr-3">
<button data-toggle="dropdown" type="button">
About GitLab
<svg xmlns="http://www.w3.org/2000/svg" class="s16 caret-down" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"/></svg>
</button>
<div class="dropdown-menu">
<ul>
<li>
<a href="https://about.gitlab.com/stages-devops-lifecycle/">GitLab: the DevOps platform
</a></li>
<li>
<a href="/explore">Explore GitLab
</a></li>
<li>
<a href="https://about.gitlab.com/install/">Install GitLab
</a></li>
<li>
<a href="https://about.gitlab.com/is-it-any-good/">How GitLab compares
</a></li>
<li>
<a href="https://about.gitlab.com/get-started/">Get started
</a></li>
<li>
<a href="https://docs.gitlab.com/">GitLab docs
</a></li>
<li>
<a href="https://about.gitlab.com/learn/">GitLab Learn
</a></li>
</ul>
</div>
</li>
<li class="gl-mr-3">
<a href="https://about.gitlab.com/pricing/">Pricing
</a></li>
<li class="gl-mr-3">
<a href="https://about.gitlab.com/sales/">Talk to an expert
</a></li>
</ul>

</div>
<div class="navbar-collapse gl-transition-medium collapse gl-mr-auto global-search-container hide-when-top-nav-responsive-open">
<ul class="nav navbar-nav gl-w-full gl-align-items-center">
<li class="nav-item header-search-new gl-display-none gl-lg-display-block gl-w-full">
<div class="header-search is-not-active gl-relative gl-w-full" data-autocomplete-path="/search/autocomplete" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-search-context="{&quot;project&quot;:{&quot;id&quot;:116,&quot;name&quot;:&quot;Opus&quot;},&quot;project_metadata&quot;:{&quot;issues_path&quot;:&quot;/xnorpx/opus/-/issues&quot;,&quot;mr_path&quot;:&quot;/xnorpx/opus/-/merge_requests&quot;},&quot;code_search&quot;:true,&quot;ref&quot;:&quot;5a6912d46449cb77e799f6c18f31b3108c5b3780&quot;,&quot;scope&quot;:null,&quot;for_snippets&quot;:null}" data-search-path="/search" id="js-header-search">
<form action="/search" accept-charset="UTF-8" method="get"><div class="gl-search-box-by-type">
<svg xmlns="http://www.w3.org/2000/svg" class="s16 gl-search-box-by-type-search-icon gl-icon" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"/></svg>
<input autocomplete="off" class="form-control gl-form-input gl-search-box-by-type-input" data-qa-selector="search_box" id="search" name="search" placeholder="Search GitLab" type="text" />
</div>

<input type="hidden" name="project_id" id="project_id" value="116" autocomplete="off" />
<input type="hidden" name="scope" id="scope" autocomplete="off" />
<input type="hidden" name="search_code" id="search_code" value="true" autocomplete="off" />
<input type="hidden" name="snippets" id="snippets" autocomplete="off" />
<input type="hidden" name="repository_ref" id="repository_ref" value="5a6912d46449cb77e799f6c18f31b3108c5b3780" autocomplete="off" />
<input type="hidden" name="nav_source" id="nav_source" value="navbar" autocomplete="off" />
<kbd class="gl-absolute gl-right-3 gl-top-0 keyboard-shortcut-helper gl-z-index-1 has-tooltip" data-html="true" data-placement="bottom" title="Use the shortcut key &lt;kbd&gt;/&lt;/kbd&gt; to start a search">
/
</kbd>
</form></div>

</li>
<li class="nav-item d-none d-sm-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search?project_id=116"><svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"/></svg>
</a></li>
</ul>
</div>
<div class="navbar-collapse gl-transition-medium collapse">
<ul class="nav navbar-nav gl-w-full gl-align-items-center gl-justify-content-end">
<li class="nav-item header-help dropdown d-none d-md-block" data-track-action="click_question_mark_link" data-track-experiment="cross_stage_fdm" data-track-label="main_navigation" data-track-property="navigation">
<a class="header-help-dropdown-toggle gl-relative" data-toggle="dropdown" href="/help"><span class="gl-sr-only">
Help
</span>
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="question-o-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#question-o"/></svg>
<span class="notification-dot rounded-circle gl-absolute"></span>
<svg xmlns="http://www.w3.org/2000/svg" class="s16 caret-down" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"/></svg>
</a><div class="dropdown-menu dropdown-menu-right">
<ul>
<li>

</li>


<li>
<a href="/help">Help</a>
</li>
<li>
<a href="https://about.gitlab.com/getting-help/">Support</a>
</li>
<li>
<a target="_blank" class="text-nowrap" rel="noopener noreferrer" data-track-action="click_forum" data-track-property="question_menu" href="https://forum.gitlab.com">Community forum</a>

</li>
<li>
<button class="js-shortcuts-modal-trigger" type="button">
Keyboard shortcuts
<kbd aria-hidden="true" class="flat float-right">?</kbd>
</button>
</li>
<li class="divider"></li>
<li>
<a href="https://about.gitlab.com/submit-feedback">Submit feedback</a>
</li>
<li>
<a target="_blank" class="text-nowrap" href="https://about.gitlab.com/contributing">Contribute to GitLab
</a>
</li>

</ul>

</div>
</li>
<li class="nav-item gl-display-none gl-sm-display-block">
<ul class="nav navbar-sub-nav"><li class="nav-item b-nav-dropdown dropdown gl-new-dropdown" data-qa-selector="navbar_dropdown" data-qa-title="Menu" id="__BVID__60"><a role="button" aria-haspopup="true" aria-expanded="false" href="#" target="_self" class="nav-link dropdown-toggle top-nav-toggle js-top-nav-dropdown-toggle gl-px-3! dropdown-toggle-no-caret" id="__BVID__60__BV_toggle_"><svg xmlns="http://www.w3.org/2000/svg" data-testid="hamburger-icon" role="img" aria-hidden="true" class="gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#hamburger"/></svg> <!----></a><ul tabindex="-1" class="dropdown-menu gl-mt-3! gl-max-w-none! gl-max-h-none! gl-sm-w-auto! js-top-nav-dropdown-menu" aria-labelledby="__BVID__60__BV_toggle_"> <li role="presentation"><form tabindex="-1" class="b-dropdown-form gl-p-0"><div class="gl-display-flex gl-align-items-stretch"><div data-testid="menu-sidebar" class="gl-w-grid-size-30 gl-flex-shrink-0 gl-bg-gray-10 gl-p-3 gl-w-full"><div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column"><div data-testid="menu-section" class=""><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block">
        Explore
      </strong><a aria-label="Projects" data-qa-selector="menu_item_link" data-qa-title="Projects" href="/explore" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-shadow-none! gl-font-weight-bold! active gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="project-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#project"/></svg> 
      Projects
      <!----></span></span></a><a aria-label="Groups" data-qa-selector="menu_item_link" data-qa-title="Groups" href="/explore/groups" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="group-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#group"/></svg> 
      Groups
      <!----></span></span></a><a aria-label="Snippets" data-qa-selector="menu_item_link" data-qa-title="Snippets" href="/explore/snippets" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="snippet-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#snippet"/></svg> 
      Snippets
      <!----></span></span></a></div></div></div> <div data-testid="menu-subview" data-qa-selector="menu_subview_container" class="gl-w-grid-size-40 gl-overflow-hidden gl-p-3" style="display: none;"></div></div></form></li></ul></li></ul>
<div class="hidden">
<a class="dashboard-shortcuts-projects" href="/explore">Projects
</a><a class="dashboard-shortcuts-groups" href="/explore/groups">Groups
</a><a class="dashboard-shortcuts-snippets" href="/explore/snippets">Snippets
</a></div>

</li>
<li class="nav-item gl-display-none gl-sm-display-block">
<a class="gl-button btn btn-default btn-sign-in" href="/users/sign_up">Sign up now</a>
</li>
<li class="nav-item gl-display-none gl-sm-display-block">
<a href="/users/sign_in?redirect_to_referer=yes">Login</a>
</li>
<li class="nav-item gl-sm-display-none">
<div>
<a class="gl-button btn btn-default btn-sign-in" href="/users/sign_in?redirect_to_referer=yes">Sign in / Register</a>
</div>
</li>

</ul>
</div>
<button class="navbar-toggler d-block d-sm-none gl-border-none!" data-qa-selector="mobile_navbar_button" data-testid="top-nav-responsive-toggle" type="button">
<span class="sr-only">Toggle navigation</span>
<span class="more-icon gl-px-3 gl-font-sm gl-font-weight-bold">
<span class="gl-pr-2">Menu</span>
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="hamburger-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#hamburger"/></svg>
</span>
<svg xmlns="http://www.w3.org/2000/svg" class="s12 close-icon" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"/></svg>
</button>
</div>
</div>
</header>

<div class="layout-page hide-when-top-nav-responsive-open page-with-contextual-sidebar">
<aside aria-label="Project navigation" class="nav-sidebar js-sidebar-collapsed">
<div class="nav-sidebar-inner-scroll">
<ul class="sidebar-top-level-items" data-qa-selector="project_sidebar">
<li data-track-label="scope_menu" data-container="body" data-placement="right" class="context-header has-tooltip" title="Opus"><a aria-label="Opus" class="shortcuts-project rspec-project-link gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project scope" href="/xnorpx/opus"><span class="avatar-container rect-avatar s32 project_avatar">
<img alt="Opus" class="avatar avatar-tile s32 js-lazy-loaded" width="32" height="32" src="/uploads/-/system/project/avatar/116/opus-logo-imageonly.png?width=32" loading="lazy" data-qa_selector="js_lazy_loaded_content" />
</span>
<span class="sidebar-context-title">
Opus
</span>
</a></li>
<li data-track-label="project_information_menu" class="home"><a aria-label="Project information" class="shortcuts-project-information has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project information" href="/xnorpx/opus/activity"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="project-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#project"/></svg>
</span>
<span class="nav-item-name">
Project information
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Project information
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="activity" class=""><a aria-label="Activity" class="shortcuts-project-activity gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Activity" href="/xnorpx/opus/activity"><span>
Activity
</span>
</a></li><li data-track-label="labels" class=""><a aria-label="Labels" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Labels" href="/xnorpx/opus/-/labels"><span>
Labels
</span>
</a></li><li data-track-label="members" class=""><a aria-label="Members" id="js-onboarding-members-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Members" href="/xnorpx/opus/-/project_members"><span>
Members
</span>
</a></li>
</ul>

</li><li data-track-label="repository_menu" class="active"><a aria-label="Repository" class="shortcuts-tree has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Repository" href="/xnorpx/opus/-/tree/5a6912d46449cb77e799f6c18f31b3108c5b3780"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="doc-text-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#doc-text"/></svg>
</span>
<span class="nav-item-name" id="js-onboarding-repo-link">
Repository
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item active"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Repository
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="files" class="active"><a aria-label="Files" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Files" href="/xnorpx/opus/-/tree/5a6912d46449cb77e799f6c18f31b3108c5b3780"><span>
Files
</span>
</a></li><li data-track-label="commits" class=""><a aria-label="Commits" id="js-onboarding-commits-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Commits" href="/xnorpx/opus/-/commits/5a6912d46449cb77e799f6c18f31b3108c5b3780"><span>
Commits
</span>
</a></li><li data-track-label="branches" class=""><a aria-label="Branches" id="js-onboarding-branches-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Branches" href="/xnorpx/opus/-/branches"><span>
Branches
</span>
</a></li><li data-track-label="tags" class=""><a aria-label="Tags" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Tags" href="/xnorpx/opus/-/tags"><span>
Tags
</span>
</a></li><li data-track-label="contributors" class=""><a aria-label="Contributors" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Contributors" href="/xnorpx/opus/-/graphs/5a6912d46449cb77e799f6c18f31b3108c5b3780"><span>
Contributors
</span>
</a></li><li data-track-label="graphs" class=""><a aria-label="Graph" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Graph" href="/xnorpx/opus/-/network/5a6912d46449cb77e799f6c18f31b3108c5b3780"><span>
Graph
</span>
</a></li><li data-track-label="compare" class=""><a aria-label="Compare" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Compare" href="/xnorpx/opus/-/compare?from=master&amp;to=5a6912d46449cb77e799f6c18f31b3108c5b3780"><span>
Compare
</span>
</a></li>
</ul>

</li><li data-track-label="issues_menu" class=""><a aria-label="Issues" class="shortcuts-issues has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Issues" href="/xnorpx/opus/-/issues"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="issues-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#issues"/></svg>
</span>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="gl-badge badge badge-pill badge-info sm count issue_counter">0
</span></a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Issues
</strong>
<span class="gl-badge badge badge-pill badge-info sm count fly-out-badge issue_counter">0
</span></span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="issue_list" class=""><a aria-label="Issues" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="List" href="/xnorpx/opus/-/issues"><span>
List
</span>
</a></li><li data-track-label="boards" class=""><a aria-label="Boards" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Boards" href="/xnorpx/opus/-/boards"><span>
Boards
</span>
</a></li><li data-track-label="service_desk" class=""><a aria-label="Service Desk" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Service Desk" href="/xnorpx/opus/-/issues/service_desk"><span>
Service Desk
</span>
</a></li><li data-track-label="milestones" class=""><a aria-label="Milestones" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Milestones" href="/xnorpx/opus/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>

</li><li data-track-label="merge_requests_menu" class=""><a aria-label="Merge requests" class="shortcuts-merge_requests gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Merge requests" href="/xnorpx/opus/-/merge_requests"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="git-merge-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#git-merge"/></svg>
</span>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge requests
</span>
<span class="gl-badge badge badge-pill badge-info sm count merge_counter js-merge-counter">0
</span></a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Merge requests
</strong>
<span class="gl-badge badge badge-pill badge-info sm count fly-out-badge merge_counter js-merge-counter">0
</span></span>
</li></ul>

</li><li data-track-label="ci_cd_menu" class=""><a aria-label="CI/CD" class="shortcuts-pipelines rspec-link-pipelines has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="CI/CD" href="/xnorpx/opus/-/pipelines"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="rocket-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#rocket"/></svg>
</span>
<span class="nav-item-name" id="js-onboarding-pipelines-link">
CI/CD
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
CI/CD
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="pipelines" class=""><a aria-label="Pipelines" class="shortcuts-pipelines gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Pipelines" href="/xnorpx/opus/-/pipelines"><span>
Pipelines
</span>
</a></li><li data-track-label="jobs" class=""><a aria-label="Jobs" class="shortcuts-builds gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Jobs" href="/xnorpx/opus/-/jobs"><span>
Jobs
</span>
</a></li><li data-track-label="pipeline_schedules" class=""><a aria-label="Schedules" class="shortcuts-builds gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Schedules" href="/xnorpx/opus/-/pipeline_schedules"><span>
Schedules
</span>
</a></li>
</ul>

</li><li data-track-label="deployments_menu" class=""><a aria-label="Deployments" class="shortcuts-deployments has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Deployments" href="/xnorpx/opus/-/environments"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="deployments-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#deployments"/></svg>
</span>
<span class="nav-item-name">
Deployments
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Deployments
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="environments" class=""><a aria-label="Environments" class="shortcuts-environments gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Environments" href="/xnorpx/opus/-/environments"><span>
Environments
</span>
</a></li><li data-track-label="releases" class=""><a aria-label="Releases" class="shortcuts-deployments-releases gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Releases" href="/xnorpx/opus/-/releases"><span>
Releases
</span>
</a></li>
</ul>

</li><li data-track-label="monitor_menu" class=""><a aria-label="Monitor" class="shortcuts-monitor has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Monitor" href="/xnorpx/opus/-/incidents"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="monitor-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#monitor"/></svg>
</span>
<span class="nav-item-name">
Monitor
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Monitor
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="incidents" class=""><a aria-label="Incidents" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Incidents" href="/xnorpx/opus/-/incidents"><span>
Incidents
</span>
</a></li>
</ul>

</li><li data-track-label="analytics_menu" class=""><a aria-label="Analytics" class="shortcuts-analytics has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Analytics" href="/xnorpx/opus/-/value_stream_analytics"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="chart-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chart"/></svg>
</span>
<span class="nav-item-name">
Analytics
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Analytics
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="cycle_analytics" class=""><a aria-label="Value stream" class="shortcuts-project-cycle-analytics gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Value stream" href="/xnorpx/opus/-/value_stream_analytics"><span>
Value stream
</span>
</a></li><li data-track-label="ci_cd_analytics" class=""><a aria-label="CI/CD" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="CI/CD" href="/xnorpx/opus/-/pipelines/charts"><span>
CI/CD
</span>
</a></li><li data-track-label="repository_analytics" class=""><a aria-label="Repository" class="shortcuts-repository-charts gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Repository" href="/xnorpx/opus/-/graphs/5a6912d46449cb77e799f6c18f31b3108c5b3780/charts"><span>
Repository
</span>
</a></li>
</ul>

</li><li data-track-label="wiki_menu" class=""><a aria-label="Wiki" class="shortcuts-wiki gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Wiki" href="/xnorpx/opus/-/wikis/home"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="book-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#book"/></svg>
</span>
<span class="nav-item-name">
Wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Wiki
</strong>
</span>
</li></ul>

</li><li data-track-label="snippets_menu" class=""><a aria-label="Snippets" class="shortcuts-snippets gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Snippets" href="/xnorpx/opus/-/snippets"><span class="nav-icon-container">
<svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="snippet-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#snippet"/></svg>
</span>
<span class="nav-item-name">
Snippets
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Snippets
</strong>
</span>
</li></ul>

</li>
<li class="hidden">
<a aria-label="Activity" class="shortcuts-project-activity gl-link" href="/xnorpx/opus/activity">Activity
</a></li>
<li class="hidden">
<a aria-label="Graph" class="shortcuts-network gl-link" href="/xnorpx/opus/-/network/5a6912d46449cb77e799f6c18f31b3108c5b3780">Graph
</a></li>
<li class="hidden">
<a aria-label="Create a new issue" class="shortcuts-new-issue gl-link" href="/xnorpx/opus/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a aria-label="Jobs" class="shortcuts-builds gl-link" href="/xnorpx/opus/-/jobs">Jobs
</a></li>
<li class="hidden">
<a aria-label="Commits" class="shortcuts-commits gl-link" href="/xnorpx/opus/-/commits/master">Commits
</a></li>
<li class="hidden">
<a aria-label="Issue Boards" class="shortcuts-issue-boards gl-link" href="/xnorpx/opus/-/boards">Issue Boards
</a></li>

</ul>
<a class="toggle-sidebar-button js-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg xmlns="http://www.w3.org/2000/svg" class="s12 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-double-lg-left"/></svg>
<span class="collapse-text gl-ml-3">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg xmlns="http://www.w3.org/2000/svg" class="s16" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"/></svg>
<span class="collapse-text gl-ml-3">Close sidebar</span>
</button>
</div>
</aside>


<div class="content-wrapper content-wrapper-margin">
<div class="mobile-overlay"></div>

<div class="alert-wrapper gl-force-block-formatting-context">




















<nav aria-label="Breadcrumbs" class="breadcrumbs container-fluid container-limited project-highlight-puc">
<div class="breadcrumbs-container">
<button name="button" type="button" class="toggle-mobile-nav" data-qa-selector="toggle_mobile_nav_button"><span class="sr-only">Open sidebar</span>
<svg xmlns="http://www.w3.org/2000/svg" class="s18" data-testid="sidebar-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#sidebar"/></svg>
</button><div class="breadcrumbs-links" data-qa-selector="breadcrumb_links_content" data-testid="breadcrumb-links">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a href="/xnorpx">Marcus Asteborg</a><svg xmlns="http://www.w3.org/2000/svg" class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"/></svg></li> <li><a href="/xnorpx/opus"><img alt="Opus" class="avatar-tile js-lazy-loaded" width="15" height="15" src="/uploads/-/system/project/avatar/116/opus-logo-imageonly.png?width=15" loading="lazy" data-qa_selector="js_lazy_loaded_content" /><span class="breadcrumb-item-text js-breadcrumb-item-text">Opus</span></a><svg xmlns="http://www.w3.org/2000/svg" class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-lg-right"/></svg></li>

<li data-qa-selector="breadcrumb_current_link" data-testid="breadcrumb-current-link">
<a href="/xnorpx/opus/-/blob/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c">Repository</a>
</li>
</ul>
</div>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Marcus Asteborg","item":"https://gitlab.xiph.org/xnorpx"},{"@type":"ListItem","position":2,"name":"Opus","item":"https://gitlab.xiph.org/xnorpx/opus"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://gitlab.xiph.org/xnorpx/opus/-/blob/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c"}]}

</script>

</div>
</nav>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope="" itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-qa-selector="flash_container">
</div>



<div class="js-signature-container" data-signatures-path="/xnorpx/opus/-/commits/3aa264732ce0e5200e5d931e88221d22270f2b00/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/xnorpx/opus/-/refs/switch" accept-charset="UTF-8" method="get"><input type="hidden" name="destination" id="destination" value="blob" autocomplete="off" />
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown" type="button" data-toggle="dropdown" data-selected="5a6912d46449cb77e799f6c18f31b3108c5b3780" data-ref="5a6912d46449cb77e799f6c18f31b3108c5b3780" data-refs-url="/xnorpx/opus/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true" data-qa-selector="branches_dropdown" data-testid="branches-select"><span class="dropdown-toggle-text ">5a6912d46449cb77e799f6c18f31b3108c5b3780</span><svg xmlns="http://www.w3.org/2000/svg" class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#chevron-down"/></svg></button>
<div class="dropdown-menu dropdown-menu-selectable git-revision-dropdown dropdown-menu-paging" data-qa-selector="branches_dropdown_content">
<div class="dropdown-page-one">
<div class="dropdown-title gl-display-flex"><span class="gl-ml-auto">Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close gl-ml-auto" aria-label="Close" type="button"><svg xmlns="http://www.w3.org/2000/svg" class="s16 dropdown-menu-close-icon" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"/></svg></button></div>
<div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off" /><svg xmlns="http://www.w3.org/2000/svg" class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"/></svg><svg xmlns="http://www.w3.org/2000/svg" class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#close"/></svg></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span aria-label="Loading" class="gl-spinner gl-spinner-md gl-spinner-dark gl-vertical-align-text-bottom!"></span></div></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/xnorpx/opus/-/tree/5a6912d46449cb77e799f6c18f31b3108c5b3780">opus
</a></li>
<li class="breadcrumb-item">
<a href="/xnorpx/opus/-/tree/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt">celt</a>
</li>
<li class="breadcrumb-item">
<a href="/xnorpx/opus/-/blob/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c"><strong>cwrs.c</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="gl-button btn btn-default shortcuts-find-file" rel="nofollow" href="/xnorpx/opus/-/find_file/5a6912d46449cb77e799f6c18f31b3108c5b3780">Find file
</a><a class="gl-button btn btn-default js-blob-blame-link" href="/xnorpx/opus/-/blame/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c">Blame</a><a class="gl-button btn btn-default" href="/xnorpx/opus/-/commits/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c">History</a><a class="gl-button btn btn-default js-data-file-blob-permalink-url" href="/xnorpx/opus/-/blob/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-3aa26473">
<div class="avatar-cell d-none d-sm-block">
<a href="mailto:giles@mozilla.com"><img alt="Ralph Giles's avatar" src="/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png" class="avatar s40 d-none d-sm-inline-block" title="Ralph Giles" /></a>
</div>
<div class="commit-detail flex-list gl-display-flex gl-justify-content-space-between gl-align-items-flex-start gl-flex-grow-1 gl-min-w-0">
<div class="commit-content" data-qa-selector="commit_content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/xnorpx/opus/-/commit/3aa264732ce0e5200e5d931e88221d22270f2b00">Fix an indentation issue.</a>
<span class="commit-row-message d-inline d-sm-none">
·
3aa26473
</span>
<div class="committer">
<a class="commit-author-link" href="mailto:giles@mozilla.com">Ralph Giles</a> authored <time class="js-timeago" title="Oct 18, 2012 2:12am GMT+0800" datetime="2012-10-17T18:12:41Z" data-toggle="tooltip" data-placement="bottom" data-container="body">10 years ago</time>
</div>

</div>
<div class="commit-actions flex-row">

<div class="js-commit-pipeline-status" data-endpoint="/xnorpx/opus/-/commit/3aa264732ce0e5200e5d931e88221d22270f2b00/pipelines?ref=5a6912d46449cb77e799f6c18f31b3108c5b3780"></div>
<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
3aa26473
</div>
<button class="btn gl-button btn btn-default btn-icon" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA" data-class="gl-button btn btn-default btn-icon" data-clipboard-text="3aa264732ce0e5200e5d931e88221d22270f2b00" type="button" title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite"><svg xmlns="http://www.w3.org/2000/svg" class="s16 gl-icon" data-testid="copy-to-clipboard-icon"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#copy-to-clipboard"/></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>
<div data-blob-path="celt/cwrs.c" data-branch="5a6912d46449cb77e799f6c18f31b3108c5b3780" data-project-path="xnorpx/opus" id="js-code-owners"></div>

</div>
<div class="blob-content-holder js-per-page" data-blame-per-page="1000" id="blob-content-holder">
<div><!----> <div class="file-holder"><div class="js-file-title file-title-flex-parent"><div class="gl-display-flex"><!----> <div class="file-header-content d-flex align-items-center lh-100"> <span aria-hidden="true"><svg xmlns="http://www.w3.org/2000/svg" class="s16 gl-mr-3"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="/assets/file_icons-958d18a1c33aa82a81e2eb1ffbffc33131d501c41ad95838a70b089e5ffbd7a0.svg#c"/></svg></span> <strong data-qa-selector="file_title_content" class="file-title-name mr-1 js-blob-header-filepath">cwrs.c</strong> <button id="clipboard-button-2" title="Copy file path" data-clipboard-text="{&quot;text&quot;:&quot;celt/cwrs.c&quot;,&quot;gfm&quot;:&quot;`celt/cwrs.c`&quot;}" data-clipboard-handle-tooltip="false" aria-label="Copy file path" aria-live="polite" type="button" class="btn btn-default btn-md gl-button btn-default-tertiary btn-icon btn-clipboard btn-transparent lh-100 position-static"><!----> <svg xmlns="http://www.w3.org/2000/svg" data-testid="copy-to-clipboard-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#copy-to-clipboard"/></svg>  <!----></button> <small class="gl-mr-3">19.80 KiB</small> <!----></div></div> <div class="gl-display-flex gl-flex-wrap file-actions"><!----> <div class="gl-sm-ml-3 gl-mr-3"><div class="dropdown b-dropdown gl-new-dropdown btn-group" data-qa-selector="action_dropdown" split-href="/-/ide/project/xnorpx/opus/edit/5a6912d46449cb77e799f6c18f31b3108c5b3780/-/celt/cwrs.c" id="__BVID__19"><a href="/-/ide/project/xnorpx/opus/edit/5a6912d46449cb77e799f6c18f31b3108c5b3780/-/celt/cwrs.c" target="_self" class="btn btn-confirm btn-md gl-button split-content-button" id="__BVID__19__BV_button_"><span data-qa-selector="web_ide_button" data-track-action="click_consolidated_edit_ide" data-track-label="web_ide" class="gl-new-dropdown-button-text">
      Open in Web IDE
    </span></a><button aria-haspopup="true" aria-expanded="false" type="button" class="btn dropdown-toggle btn-confirm btn-md gl-button gl-dropdown-toggle dropdown-toggle-split" id="__BVID__19__BV_toggle_"><span class="sr-only">Toggle dropdown</span></button><ul role="menu" tabindex="-1" class="dropdown-menu" aria-labelledby="__BVID__19__BV_button_"><div class="gl-new-dropdown-inner"><!----> <!----> <div class="gl-new-dropdown-contents"><!---->  <li role="presentation" class="gl-new-dropdown-item"><button data-qa-selector="webide_menu_item" data-testid="action_webide" role="menuitem" type="button" class="dropdown-item"><svg xmlns="http://www.w3.org/2000/svg" data-testid="dropdown-item-checkbox" role="img" aria-hidden="true" class="gl-icon s16 gl-new-dropdown-item-check-icon gl-mt-3 gl-align-self-start"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#mobile-issue-close"/></svg> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary"><span class="gl-font-weight-bold">Open in Web IDE</span></p> <p class="gl-new-dropdown-item-text-secondary">Quickly and easily edit multiple files in your project.</p></div> <!----></button></li> <li role="presentation" class="gl-new-dropdown-divider"><hr role="separator" aria-orientation="horizontal" class="dropdown-divider" /></li><li role="presentation" class="gl-new-dropdown-item"><button data-qa-selector="edit_menu_item" data-testid="action_edit" role="menuitem" type="button" class="dropdown-item"><svg xmlns="http://www.w3.org/2000/svg" data-testid="dropdown-item-checkbox" role="img" aria-hidden="true" class="gl-icon s16 gl-new-dropdown-item-check-icon gl-visibility-hidden gl-mt-3 gl-align-self-start"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#mobile-issue-close"/></svg> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary"><span class="gl-font-weight-bold">Edit</span></p> <p class="gl-new-dropdown-item-text-secondary">Edit this file only.</p></div> <!----></button></li> <!----></div> <!----></div></ul></div> <!----> <!----> <!----></div> <!----> <div data-qa-selector="default_actions_container" role="group" class="btn-group"><button aria-label="Copy file contents" title="Copy file contents" data-testid="copyContentsButton" data-qa-selector="copy_contents_button" type="button" class="btn js-copy-blob-source-btn btn-default btn-md gl-button btn-icon"><!----> <svg xmlns="http://www.w3.org/2000/svg" data-testid="copy-to-clipboard-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#copy-to-clipboard"/></svg>  <!----></button> <a aria-label="Open raw" title="Open raw" href="/xnorpx/opus/-/raw/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c" rel="noopener" target="_blank" class="btn btn-default btn-md gl-button btn-icon"><!----> <svg xmlns="http://www.w3.org/2000/svg" data-testid="doc-code-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#doc-code"/></svg>  <!----></a> <a aria-label="Download" title="Download" href="https://gitlab.xiph.org/xnorpx/opus/-/raw/5a6912d46449cb77e799f6c18f31b3108c5b3780/celt/cwrs.c?inline=false" rel="noopener" target="_blank" class="btn btn-default btn-md gl-button btn-icon"><!----> <svg xmlns="http://www.w3.org/2000/svg" data-testid="download-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#download"/></svg>  <!----></a> <!----></div></div></div> <!----> <div data-type="simple" data-path="celt/cwrs.c" data-qa-selector="blob_viewer_file_content" class="file-content code js-syntax-highlight blob-content gl-display-flex gl-flex-direction-column gl-overflow-auto blob-viewer white"><div><div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L1" href="#L1" data-line-number="1" class="gl-user-select-none gl-shadow-none! file-line-num">
      1
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC1" lang="c" data-testid="content" class="line"><span class="hljs-comment">/* Copyright (c) 2007-2008 CSIRO</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L2" href="#L2" data-line-number="2" class="gl-user-select-none gl-shadow-none! file-line-num">
      2
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC2" lang="c" data-testid="content" class="line"><span class="hljs-comment">   Copyright (c) 2007-2009 Xiph.Org Foundation</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L3" href="#L3" data-line-number="3" class="gl-user-select-none gl-shadow-none! file-line-num">
      3
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC3" lang="c" data-testid="content" class="line"><span class="hljs-comment">   Copyright (c) 2007-2009 Timothy B. Terriberry</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L4" href="#L4" data-line-number="4" class="gl-user-select-none gl-shadow-none! file-line-num">
      4
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC4" lang="c" data-testid="content" class="line"><span class="hljs-comment">   Written by Timothy B. Terriberry and Jean-Marc Valin */</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L5" href="#L5" data-line-number="5" class="gl-user-select-none gl-shadow-none! file-line-num">
      5
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC5" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-comment"><span class="hljs-comment">/*</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L6" href="#L6" data-line-number="6" class="gl-user-select-none gl-shadow-none! file-line-num">
      6
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC6" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">   Redistribution and use </span><span class="hljs-comment">in</span><span class="hljs-comment"> source and binary </span><span class="hljs-comment">forms, with or without</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L7" href="#L7" data-line-number="7" class="gl-user-select-none gl-shadow-none! file-line-num">
      7
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC7" lang="c" data-testid="content" class="line"><span class="hljs-comment">   modification,</span><span class="hljs-comment"> are permitted provided </span><span class="hljs-comment">that the following conditions</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L8" href="#L8" data-line-number="8" class="gl-user-select-none gl-shadow-none! file-line-num">
      8
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC8" lang="c" data-testid="content" class="line"><span class="hljs-comment">   are met:</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L9" href="#L9" data-line-number="9" class="gl-user-select-none gl-shadow-none! file-line-num">
      9
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC9" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L10" href="#L10" data-line-number="10" class="gl-user-select-none gl-shadow-none! file-line-num">
      10
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC10" lang="c" data-testid="content" class="line"><span class="hljs-comment">   - Redistributions of</span><span class="hljs-comment"> source code must </span><span class="hljs-comment">retain the above copyright</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L11" href="#L11" data-line-number="11" class="gl-user-select-none gl-shadow-none! file-line-num">
      11
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC11" lang="c" data-testid="content" class="line"><span class="hljs-comment">   notice, this list of</span><span class="hljs-comment"> conditions and the </span><span class="hljs-comment">following disclaimer.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L12" href="#L12" data-line-number="12" class="gl-user-select-none gl-shadow-none! file-line-num">
      12
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC12" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L13" href="#L13" data-line-number="13" class="gl-user-select-none gl-shadow-none! file-line-num">
      13
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC13" lang="c" data-testid="content" class="line"><span class="hljs-comment">   -</span><span class="hljs-comment"> Redistributions in binary </span><span class="hljs-comment">form</span><span class="hljs-comment"> must reproduce the </span><span class="hljs-comment">above copyright</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L14" href="#L14" data-line-number="14" class="gl-user-select-none gl-shadow-none! file-line-num">
      14
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC14" lang="c" data-testid="content" class="line"><span class="hljs-comment">   notice, this list of</span><span class="hljs-comment"> conditions and the </span><span class="hljs-comment">following disclaimer in the</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L15" href="#L15" data-line-number="15" class="gl-user-select-none gl-shadow-none! file-line-num">
      15
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC15" lang="c" data-testid="content" class="line"><span class="hljs-comment">   documentation and/or</span><span class="hljs-comment"> other materials provided </span><span class="hljs-comment">with the distribution.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L16" href="#L16" data-line-number="16" class="gl-user-select-none gl-shadow-none! file-line-num">
      16
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC16" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L17" href="#L17" data-line-number="17" class="gl-user-select-none gl-shadow-none! file-line-num">
      17
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC17" lang="c" data-testid="content" class="line"><span class="hljs-comment">   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L18" href="#L18" data-line-number="18" class="gl-user-select-none gl-shadow-none! file-line-num">
      18
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC18" lang="c" data-testid="content" class="line"><span class="hljs-comment">   ``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L19" href="#L19" data-line-number="19" class="gl-user-select-none gl-shadow-none! file-line-num">
      19
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC19" lang="c" data-testid="content" class="line"><span class="hljs-comment">   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L20" href="#L20" data-line-number="20" class="gl-user-select-none gl-shadow-none! file-line-num">
      20
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC20" lang="c" data-testid="content" class="line"><span class="hljs-comment">   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L21" href="#L21" data-line-number="21" class="gl-user-select-none gl-shadow-none! file-line-num">
      21
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC21" lang="c" data-testid="content" class="line"><span class="hljs-comment">   OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L22" href="#L22" data-line-number="22" class="gl-user-select-none gl-shadow-none! file-line-num">
      22
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC22" lang="c" data-testid="content" class="line"><span class="hljs-comment">   EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L23" href="#L23" data-line-number="23" class="gl-user-select-none gl-shadow-none! file-line-num">
      23
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC23" lang="c" data-testid="content" class="line"><span class="hljs-comment">   PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L24" href="#L24" data-line-number="24" class="gl-user-select-none gl-shadow-none! file-line-num">
      24
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC24" lang="c" data-testid="content" class="line"><span class="hljs-comment">   PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L25" href="#L25" data-line-number="25" class="gl-user-select-none gl-shadow-none! file-line-num">
      25
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC25" lang="c" data-testid="content" class="line"><span class="hljs-comment">   LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L26" href="#L26" data-line-number="26" class="gl-user-select-none gl-shadow-none! file-line-num">
      26
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC26" lang="c" data-testid="content" class="line"><span class="hljs-comment">   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L27" href="#L27" data-line-number="27" class="gl-user-select-none gl-shadow-none! file-line-num">
      27
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC27" lang="c" data-testid="content" class="line"><span class="hljs-comment">   SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L28" href="#L28" data-line-number="28" class="gl-user-select-none gl-shadow-none! file-line-num">
      28
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC28" lang="c" data-testid="content" class="line"><span class="hljs-comment">*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L29" href="#L29" data-line-number="29" class="gl-user-select-none gl-shadow-none! file-line-num">
      29
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC29" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L30" href="#L30" data-line-number="30" class="gl-user-select-none gl-shadow-none! file-line-num">
      30
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC30" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">ifdef</span><span class="hljs-meta"> HAVE_CONFIG_H</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L31" href="#L31" data-line-number="31" class="gl-user-select-none gl-shadow-none! file-line-num">
      31
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC31" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"config.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L32" href="#L32" data-line-number="32" class="gl-user-select-none gl-shadow-none! file-line-num">
      32
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC32" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">endif</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L33" href="#L33" data-line-number="33" class="gl-user-select-none gl-shadow-none! file-line-num">
      33
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC33" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L34" href="#L34" data-line-number="34" class="gl-user-select-none gl-shadow-none! file-line-num">
      34
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC34" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"os_support.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L35" href="#L35" data-line-number="35" class="gl-user-select-none gl-shadow-none! file-line-num">
      35
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC35" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cwrs.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L36" href="#L36" data-line-number="36" class="gl-user-select-none gl-shadow-none! file-line-num">
      36
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC36" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"mathops.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L37" href="#L37" data-line-number="37" class="gl-user-select-none gl-shadow-none! file-line-num">
      37
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC37" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"arch.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L38" href="#L38" data-line-number="38" class="gl-user-select-none gl-shadow-none! file-line-num">
      38
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC38" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L39" href="#L39" data-line-number="39" class="gl-user-select-none gl-shadow-none! file-line-num">
      39
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC39" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">ifdef</span><span class="hljs-meta"> CUSTOM_MODES</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L40" href="#L40" data-line-number="40" class="gl-user-select-none gl-shadow-none! file-line-num">
      40
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC40" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L41" href="#L41" data-line-number="41" class="gl-user-select-none gl-shadow-none! file-line-num">
      41
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC41" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-comment"><span class="hljs-comment">/*Guaranteed</span><span class="hljs-comment"> to return a </span><span class="hljs-comment">conservatively large estimate of the binary logarithm</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L42" href="#L42" data-line-number="42" class="gl-user-select-none gl-shadow-none! file-line-num">
      42
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC42" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">   with frac bits </span><span class="hljs-comment">of fractional precision.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L43" href="#L43" data-line-number="43" class="gl-user-select-none gl-shadow-none! file-line-num">
      43
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC43" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">  Tested for all </span><span class="hljs-comment">possible 32-bit inputs with frac=4, where the maximum</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L44" href="#L44" data-line-number="44" class="gl-user-select-none gl-shadow-none! file-line-num">
      44
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC44" lang="c" data-testid="content" class="line"><span class="hljs-comment">   overestimation is 0.06254243 bits.*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L45" href="#L45" data-line-number="45" class="gl-user-select-none gl-shadow-none! file-line-num">
      45
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC45" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-type">int</span><span class=""> </span><span class="hljs-title.function">log2_frac</span><span class="hljs-params"><span class="hljs-params">(opus_uint32 val, </span><span class="hljs-type">int</span><span class="hljs-params"> frac)</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L46" href="#L46" data-line-number="46" class="gl-user-select-none gl-shadow-none! file-line-num">
      46
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC46" lang="c" data-testid="content" class="line"><span class=""></span><span class="">{</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L47" href="#L47" data-line-number="47" class="gl-user-select-none gl-shadow-none! file-line-num">
      47
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC47" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">int</span><span class=""> l;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L48" href="#L48" data-line-number="48" class="gl-user-select-none gl-shadow-none! file-line-num">
      48
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC48" lang="c" data-testid="content" class="line"><span class="">  l</span><span class="">=EC_ILOG</span><span class="">(val)</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L49" href="#L49" data-line-number="49" class="gl-user-select-none gl-shadow-none! file-line-num">
      49
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC49" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class="">(val&amp;</span><span class="">(val</span><span class="hljs-number">-1</span><span class="">)</span><span class="">)</span><span class="">{</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L50" href="#L50" data-line-number="50" class="gl-user-select-none gl-shadow-none! file-line-num">
      50
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC50" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-comment"><span class="hljs-comment">/*This is (val&gt;&gt;l-16),</span><span class="hljs-comment"> but guaranteed to </span><span class="hljs-comment">round up,</span><span class="hljs-comment"> even if adding </span><span class="hljs-comment">a bias</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L51" href="#L51" data-line-number="51" class="gl-user-select-none gl-shadow-none! file-line-num">
      51
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC51" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">       before the shift </span><span class="hljs-comment">would cause overflow (e.g., for 0xFFFFxxxx).</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L52" href="#L52" data-line-number="52" class="gl-user-select-none gl-shadow-none! file-line-num">
      52
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC52" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">       Doesn't work for </span><span class="hljs-comment">val=0,</span><span class="hljs-comment"> but that case </span><span class="hljs-comment">fails the test above.*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L53" href="#L53" data-line-number="53" class="gl-user-select-none gl-shadow-none! file-line-num">
      53
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC53" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class="">(l&gt;</span><span class="hljs-number">16</span><span class="">)</span><span class="">val</span><span class="">=</span><span class="">(</span><span class="">(val</span><span class="hljs-number">-1</span><span class="">)</span><span class="">&gt;&gt;</span><span class="">(l</span><span class="hljs-number">-16</span><span class="">)</span><span class="">)</span><span class="">+</span><span class="hljs-number">1</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L54" href="#L54" data-line-number="54" class="gl-user-select-none gl-shadow-none! file-line-num">
      54
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC54" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">else</span><span class=""> val&lt;&lt;=</span><span class="hljs-number">16</span><span class="">-l;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L55" href="#L55" data-line-number="55" class="gl-user-select-none gl-shadow-none! file-line-num">
      55
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC55" lang="c" data-testid="content" class="line"><span class="">    l</span><span class="">=</span><span class="">(l</span><span class="hljs-number">-1</span><span class="">)</span><span class="">&lt;&lt;frac;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L56" href="#L56" data-line-number="56" class="gl-user-select-none gl-shadow-none! file-line-num">
      56
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC56" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-comment"><span class="hljs-comment">/*Note that we</span><span class="hljs-comment"> always need one </span><span class="hljs-comment">iteration,</span><span class="hljs-comment"> since the rounding </span><span class="hljs-comment">up above means</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L57" href="#L57" data-line-number="57" class="gl-user-select-none gl-shadow-none! file-line-num">
      57
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC57" lang="c" data-testid="content" class="line"><span class="hljs-comment">       that we</span><span class="hljs-comment"> might need to </span><span class="hljs-comment">adjust</span><span class="hljs-comment"> the integer part </span><span class="hljs-comment">of the logarithm.*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L58" href="#L58" data-line-number="58" class="gl-user-select-none gl-shadow-none! file-line-num">
      58
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC58" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">do</span><span class="">{</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L59" href="#L59" data-line-number="59" class="gl-user-select-none gl-shadow-none! file-line-num">
      59
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC59" lang="c" data-testid="content" class="line"><span class="">      </span><span class="hljs-type">int</span><span class=""> b;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L60" href="#L60" data-line-number="60" class="gl-user-select-none gl-shadow-none! file-line-num">
      60
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC60" lang="c" data-testid="content" class="line"><span class="">      b</span><span class="">=</span><span class="">(</span><span class="hljs-type">int</span><span class="">)</span><span class="">(val&gt;&gt;</span><span class="hljs-number">16</span><span class="">)</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L61" href="#L61" data-line-number="61" class="gl-user-select-none gl-shadow-none! file-line-num">
      61
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC61" lang="c" data-testid="content" class="line"><span class="">      l+</span><span class="">=b&lt;&lt;frac;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L62" href="#L62" data-line-number="62" class="gl-user-select-none gl-shadow-none! file-line-num">
      62
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC62" lang="c" data-testid="content" class="line"><span class="">      val</span><span class="">=</span><span class="">(val+b)</span><span class="">&gt;&gt;b;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L63" href="#L63" data-line-number="63" class="gl-user-select-none gl-shadow-none! file-line-num">
      63
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC63" lang="c" data-testid="content" class="line"><span class="">      val</span><span class="">=</span><span class="">(val*val+</span><span class="hljs-number">0x7FFF</span><span class="">)</span><span class="">&gt;&gt;</span><span class="hljs-number">15</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L64" href="#L64" data-line-number="64" class="gl-user-select-none gl-shadow-none! file-line-num">
      64
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC64" lang="c" data-testid="content" class="line"><span class="">    }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L65" href="#L65" data-line-number="65" class="gl-user-select-none gl-shadow-none! file-line-num">
      65
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC65" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">while</span><span class="">(frac--&gt;</span><span class="hljs-number">0</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L66" href="#L66" data-line-number="66" class="gl-user-select-none gl-shadow-none! file-line-num">
      66
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC66" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-comment"><span class="hljs-comment">/*If</span><span class="hljs-comment"> val is not </span><span class="hljs-comment">exactly 0x8000, then we</span><span class="hljs-comment"> have to round </span><span class="hljs-comment">up the remainder.*/</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L67" href="#L67" data-line-number="67" class="gl-user-select-none gl-shadow-none! file-line-num">
      67
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC67" lang="c" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">return</span><span class=""> l+</span><span class="">(val&gt;</span><span class="hljs-number">0x8000</span><span class="">)</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L68" href="#L68" data-line-number="68" class="gl-user-select-none gl-shadow-none! file-line-num">
      68
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC68" lang="c" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L69" href="#L69" data-line-number="69" class="gl-user-select-none gl-shadow-none! file-line-num">
      69
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC69" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment">/*Exact powers of two require no rounding.*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L70" href="#L70" data-line-number="70" class="gl-user-select-none gl-shadow-none! file-line-num">
      70
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC70" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">else</span><span class=""> </span><span class="hljs-keyword">return</span><span class=""> </span><span class="">(l</span><span class="hljs-number">-1</span><span class="">)</span><span class="">&lt;&lt;frac;</span></span></code></pre></div></div></div> <div><div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L71" href="#L71" data-line-number="71" class="gl-user-select-none gl-shadow-none! file-line-num">
      71
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC71" lang="c" data-testid="content" class="line"><span class="">}</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L72" href="#L72" data-line-number="72" class="gl-user-select-none gl-shadow-none! file-line-num">
      72
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC72" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">endif</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L73" href="#L73" data-line-number="73" class="gl-user-select-none gl-shadow-none! file-line-num">
      73
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC73" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L74" href="#L74" data-line-number="74" class="gl-user-select-none gl-shadow-none! file-line-num">
      74
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC74" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">ifndef</span><span class="hljs-meta"> SMALL_FOOTPRINT</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L75" href="#L75" data-line-number="75" class="gl-user-select-none gl-shadow-none! file-line-num">
      75
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC75" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L76" href="#L76" data-line-number="76" class="gl-user-select-none gl-shadow-none! file-line-num">
      76
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC76" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">define</span><span class="hljs-meta"> MASK32 (0xFFFFFFFF)</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L77" href="#L77" data-line-number="77" class="gl-user-select-none gl-shadow-none! file-line-num">
      77
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC77" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L78" href="#L78" data-line-number="78" class="gl-user-select-none gl-shadow-none! file-line-num">
      78
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC78" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-comment"><span class="hljs-comment">/*INV_TABLE[i]</span><span class="hljs-comment"> holds the multiplicative </span><span class="hljs-comment">inverse of (2*i+1) mod 2**32.*/</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L79" href="#L79" data-line-number="79" class="gl-user-select-none gl-shadow-none! file-line-num">
      79
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC79" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-type">static</span><span class=""> </span><span class="hljs-type">const</span><span class=""> opus_uint32 INV_TABLE[</span><span class="hljs-number">53</span><span class="">]</span><span class="">={</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L80" href="#L80" data-line-number="80" class="gl-user-select-none gl-shadow-none! file-line-num">
      80
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC80" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0x00000001</span><span class="">,</span><span class="hljs-number">0xAAAAAAAB</span><span class="">,</span><span class="hljs-number">0xCCCCCCCD</span><span class="">,</span><span class="hljs-number">0xB6DB6DB7</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L81" href="#L81" data-line-number="81" class="gl-user-select-none gl-shadow-none! file-line-num">
      81
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC81" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0x38E38E39</span><span class="">,</span><span class="hljs-number">0xBA2E8BA3</span><span class="">,</span><span class="hljs-number">0xC4EC4EC5</span><span class="">,</span><span class="hljs-number">0xEEEEEEEF</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L82" href="#L82" data-line-number="82" class="gl-user-select-none gl-shadow-none! file-line-num">
      82
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC82" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xF0F0F0F1</span><span class="">,</span><span class="hljs-number">0x286BCA1B</span><span class="">,</span><span class="hljs-number">0x3CF3CF3D</span><span class="">,</span><span class="hljs-number">0xE9BD37A7</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L83" href="#L83" data-line-number="83" class="gl-user-select-none gl-shadow-none! file-line-num">
      83
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC83" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xC28F5C29</span><span class="">,</span><span class="hljs-number">0x684BDA13</span><span class="">,</span><span class="hljs-number">0x4F72C235</span><span class="">,</span><span class="hljs-number">0xBDEF7BDF</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L84" href="#L84" data-line-number="84" class="gl-user-select-none gl-shadow-none! file-line-num">
      84
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC84" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0x3E0F83E1</span><span class="">,</span><span class="hljs-number">0x8AF8AF8B</span><span class="">,</span><span class="hljs-number">0x914C1BAD</span><span class="">,</span><span class="hljs-number">0x96F96F97</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L85" href="#L85" data-line-number="85" class="gl-user-select-none gl-shadow-none! file-line-num">
      85
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC85" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xC18F9C19</span><span class="">,</span><span class="hljs-number">0x2FA0BE83</span><span class="">,</span><span class="hljs-number">0xA4FA4FA5</span><span class="">,</span><span class="hljs-number">0x677D46CF</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L86" href="#L86" data-line-number="86" class="gl-user-select-none gl-shadow-none! file-line-num">
      86
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC86" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0x1A1F58D1</span><span class="">,</span><span class="hljs-number">0xFAFAFAFB</span><span class="">,</span><span class="hljs-number">0x8C13521D</span><span class="">,</span><span class="hljs-number">0x586FB587</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L87" href="#L87" data-line-number="87" class="gl-user-select-none gl-shadow-none! file-line-num">
      87
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC87" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xB823EE09</span><span class="">,</span><span class="hljs-number">0xA08AD8F3</span><span class="">,</span><span class="hljs-number">0xC10C9715</span><span class="">,</span><span class="hljs-number">0xBEFBEFBF</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L88" href="#L88" data-line-number="88" class="gl-user-select-none gl-shadow-none! file-line-num">
      88
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC88" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xC0FC0FC1</span><span class="">,</span><span class="hljs-number">0x07A44C6B</span><span class="">,</span><span class="hljs-number">0xA33F128D</span><span class="">,</span><span class="hljs-number">0xE327A977</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L89" href="#L89" data-line-number="89" class="gl-user-select-none gl-shadow-none! file-line-num">
      89
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC89" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xC7E3F1F9</span><span class="">,</span><span class="hljs-number">0x962FC963</span><span class="">,</span><span class="hljs-number">0x3F2B3885</span><span class="">,</span><span class="hljs-number">0x613716AF</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L90" href="#L90" data-line-number="90" class="gl-user-select-none gl-shadow-none! file-line-num">
      90
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC90" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0x781948B1</span><span class="">,</span><span class="hljs-number">0x2B2E43DB</span><span class="">,</span><span class="hljs-number">0xFCFCFCFD</span><span class="">,</span><span class="hljs-number">0x6FD0EB67</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L91" href="#L91" data-line-number="91" class="gl-user-select-none gl-shadow-none! file-line-num">
      91
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC91" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xFA3F47E9</span><span class="">,</span><span class="hljs-number">0xD2FD2FD3</span><span class="">,</span><span class="hljs-number">0x3F4FD3F5</span><span class="">,</span><span class="hljs-number">0xD4E25B9F</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L92" href="#L92" data-line-number="92" class="gl-user-select-none gl-shadow-none! file-line-num">
      92
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC92" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0x5F02A3A1</span><span class="">,</span><span class="hljs-number">0xBF5A814B</span><span class="">,</span><span class="hljs-number">0x7C32B16D</span><span class="">,</span><span class="hljs-number">0xD3431B57</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L93" href="#L93" data-line-number="93" class="gl-user-select-none gl-shadow-none! file-line-num">
      93
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC93" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-number">0xD8FD8FD9</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L94" href="#L94" data-line-number="94" class="gl-user-select-none gl-shadow-none! file-line-num">
      94
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC94" lang="c" data-testid="content" class="line"><span class="">};</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L95" href="#L95" data-line-number="95" class="gl-user-select-none gl-shadow-none! file-line-num">
      95
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC95" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L96" href="#L96" data-line-number="96" class="gl-user-select-none gl-shadow-none! file-line-num">
      96
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC96" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-comment"><span class="hljs-comment">/*Computes (_a*_b-_c)/(2*_d+1)</span><span class="hljs-comment"> when the quotient </span><span class="hljs-comment">is known to be exact.</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L97" href="#L97" data-line-number="97" class="gl-user-select-none gl-shadow-none! file-line-num">
      97
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC97" lang="c" data-testid="content" class="line"><span class="hljs-comment">  _a, _b, _c, and _d may be</span><span class="hljs-comment"> arbitrary so long </span><span class="hljs-comment">as</span><span class="hljs-comment"> the arbitrary precision </span><span class="hljs-comment">result</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L98" href="#L98" data-line-number="98" class="gl-user-select-none gl-shadow-none! file-line-num">
      98
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC98" lang="c" data-testid="content" class="line"><span class="hljs-comment">   fits in 32 bits,</span><span class="hljs-comment"> but currently the </span><span class="hljs-comment">table</span><span class="hljs-comment"> for multiplicative inverses </span><span class="hljs-comment">is only</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L99" href="#L99" data-line-number="99" class="gl-user-select-none gl-shadow-none! file-line-num">
      99
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC99" lang="c" data-testid="content" class="line"><span class="hljs-comment">   valid for _d&lt;=52.*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L100" href="#L100" data-line-number="100" class="gl-user-select-none gl-shadow-none! file-line-num">
      100
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC100" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-type">static</span><span class=""> </span><span class="hljs-keyword">inline</span><span class=""> opus_uint32 </span><span class="hljs-title.function">imusdiv32odd</span><span class="hljs-params"><span class="hljs-params">(opus_uint32 _a,opus_uint32 _b,</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L101" href="#L101" data-line-number="101" class="gl-user-select-none gl-shadow-none! file-line-num">
      101
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC101" lang="c" data-testid="content" class="line"><span class="hljs-params"> opus_uint32 _c,</span><span class="hljs-type">int</span><span class="hljs-params"> _d)</span><span class="">{</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L102" href="#L102" data-line-number="102" class="gl-user-select-none gl-shadow-none! file-line-num">
      102
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC102" lang="c" data-testid="content" class="line"><span class="">  celt_assert</span><span class="">(_d&lt;=</span><span class="hljs-number">52</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L103" href="#L103" data-line-number="103" class="gl-user-select-none gl-shadow-none! file-line-num">
      103
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC103" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">return</span><span class=""> </span><span class="">(_a*_b-_c)</span><span class="">*INV_TABLE[_d]&amp;MASK32;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L104" href="#L104" data-line-number="104" class="gl-user-select-none gl-shadow-none! file-line-num">
      104
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC104" lang="c" data-testid="content" class="line"><span class="">}</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L105" href="#L105" data-line-number="105" class="gl-user-select-none gl-shadow-none! file-line-num">
      105
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC105" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L106" href="#L106" data-line-number="106" class="gl-user-select-none gl-shadow-none! file-line-num">
      106
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC106" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-comment"><span class="hljs-comment">/*Computes (_a*_b-_c)/_d</span><span class="hljs-comment"> when the quotient </span><span class="hljs-comment">is known to be exact.</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L107" href="#L107" data-line-number="107" class="gl-user-select-none gl-shadow-none! file-line-num">
      107
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC107" lang="c" data-testid="content" class="line"><span class="hljs-comment">  _d</span><span class="hljs-comment"> does not actually </span><span class="hljs-comment">have to be even, but imusdiv32odd will be faster when</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L108" href="#L108" data-line-number="108" class="gl-user-select-none gl-shadow-none! file-line-num">
      108
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC108" lang="c" data-testid="content" class="line"><span class="hljs-comment">   it's odd,</span><span class="hljs-comment"> so you should </span><span class="hljs-comment">use that instead.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L109" href="#L109" data-line-number="109" class="gl-user-select-none gl-shadow-none! file-line-num">
      109
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC109" lang="c" data-testid="content" class="line"><span class="hljs-comment">  _a and _d</span><span class="hljs-comment"> are assumed to </span><span class="hljs-comment">be small (e.g., _a*_d fits in 32 bits; currently the</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L110" href="#L110" data-line-number="110" class="gl-user-select-none gl-shadow-none! file-line-num">
      110
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC110" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">   table for multiplicative </span><span class="hljs-comment">inverses</span><span class="hljs-comment"> is only valid </span><span class="hljs-comment">for _d&lt;=54).</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L111" href="#L111" data-line-number="111" class="gl-user-select-none gl-shadow-none! file-line-num">
      111
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC111" lang="c" data-testid="content" class="line"><span class="hljs-comment">  _b and _c may be</span><span class="hljs-comment"> arbitrary so long </span><span class="hljs-comment">as</span><span class="hljs-comment"> the arbitrary precision </span><span class="hljs-comment">reuslt fits in</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L112" href="#L112" data-line-number="112" class="gl-user-select-none gl-shadow-none! file-line-num">
      112
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC112" lang="c" data-testid="content" class="line"><span class="hljs-comment">   32 bits.*/</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L113" href="#L113" data-line-number="113" class="gl-user-select-none gl-shadow-none! file-line-num">
      113
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC113" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-type">static</span><span class=""> </span><span class="hljs-keyword">inline</span><span class=""> opus_uint32 </span><span class="hljs-title.function">imusdiv32even</span><span class="hljs-params"><span class="hljs-params">(opus_uint32 _a,opus_uint32 _b,</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L114" href="#L114" data-line-number="114" class="gl-user-select-none gl-shadow-none! file-line-num">
      114
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC114" lang="c" data-testid="content" class="line"><span class="hljs-params"> opus_uint32 _c,</span><span class="hljs-type">int</span><span class="hljs-params"> _d)</span><span class="">{</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L115" href="#L115" data-line-number="115" class="gl-user-select-none gl-shadow-none! file-line-num">
      115
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC115" lang="c" data-testid="content" class="line"><span class="">  opus_uint32 inv;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L116" href="#L116" data-line-number="116" class="gl-user-select-none gl-shadow-none! file-line-num">
      116
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC116" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">int</span><span class="">           mask;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L117" href="#L117" data-line-number="117" class="gl-user-select-none gl-shadow-none! file-line-num">
      117
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC117" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">int</span><span class="">           shift;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L118" href="#L118" data-line-number="118" class="gl-user-select-none gl-shadow-none! file-line-num">
      118
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC118" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">int</span><span class="">           one;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L119" href="#L119" data-line-number="119" class="gl-user-select-none gl-shadow-none! file-line-num">
      119
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC119" lang="c" data-testid="content" class="line"><span class="">  celt_assert</span><span class="">(_d&gt;</span><span class="hljs-number">0</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L120" href="#L120" data-line-number="120" class="gl-user-select-none gl-shadow-none! file-line-num">
      120
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC120" lang="c" data-testid="content" class="line"><span class="">  celt_assert</span><span class="">(_d&lt;=</span><span class="hljs-number">54</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L121" href="#L121" data-line-number="121" class="gl-user-select-none gl-shadow-none! file-line-num">
      121
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC121" lang="c" data-testid="content" class="line"><span class="">  shift</span><span class="">=EC_ILOG</span><span class="">(_d^</span><span class="">(_d</span><span class="hljs-number">-1</span><span class="">)</span><span class="">)</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L122" href="#L122" data-line-number="122" class="gl-user-select-none gl-shadow-none! file-line-num">
      122
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC122" lang="c" data-testid="content" class="line"><span class="">  inv</span><span class="">=INV_TABLE[</span><span class="">(_d</span><span class="hljs-number">-1</span><span class="">)</span><span class="">&gt;&gt;shift];</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L123" href="#L123" data-line-number="123" class="gl-user-select-none gl-shadow-none! file-line-num">
      123
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC123" lang="c" data-testid="content" class="line"><span class="">  shift--;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L124" href="#L124" data-line-number="124" class="gl-user-select-none gl-shadow-none! file-line-num">
      124
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC124" lang="c" data-testid="content" class="line"><span class="">  one</span><span class="">=</span><span class="hljs-number">1</span><span class="">&lt;&lt;shift;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L125" href="#L125" data-line-number="125" class="gl-user-select-none gl-shadow-none! file-line-num">
      125
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC125" lang="c" data-testid="content" class="line"><span class="">  mask</span><span class="">=one</span><span class="hljs-number">-1</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L126" href="#L126" data-line-number="126" class="gl-user-select-none gl-shadow-none! file-line-num">
      126
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC126" lang="c" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">return</span><span class=""> </span><span class="">(_a*</span><span class="">(_b&gt;&gt;shift)</span><span class="">-</span><span class="">(_c&gt;&gt;shift)</span><span class="">+</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L127" href="#L127" data-line-number="127" class="gl-user-select-none gl-shadow-none! file-line-num">
      127
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC127" lang="c" data-testid="content" class="line"><span class="">   </span><span class="">(</span><span class="">(_a*</span><span class="">(_b&amp;mask)</span><span class="">+one-</span><span class="">(_c&amp;mask)</span><span class="">)</span><span class="">&gt;&gt;shift)</span><span class="hljs-number">-1</span><span class="">)</span><span class="">*inv&amp;MASK32;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L128" href="#L128" data-line-number="128" class="gl-user-select-none gl-shadow-none! file-line-num">
      128
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC128" lang="c" data-testid="content" class="line"><span class="">}</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L129" href="#L129" data-line-number="129" class="gl-user-select-none gl-shadow-none! file-line-num">
      129
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC129" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L130" href="#L130" data-line-number="130" class="gl-user-select-none gl-shadow-none! file-line-num">
      130
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC130" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">endif</span><span class="hljs-meta"> </span><span class="hljs-comment">/* SMALL_FOOTPRINT */</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L131" href="#L131" data-line-number="131" class="gl-user-select-none gl-shadow-none! file-line-num">
      131
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC131" lang="c" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L132" href="#L132" data-line-number="132" class="gl-user-select-none gl-shadow-none! file-line-num">
      132
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC132" lang="c" data-testid="content" class="line"><span class=""></span><span class="hljs-comment"><span class="hljs-comment">/*Although derived separately,</span><span class="hljs-comment"> the pulse vector </span><span class="hljs-comment">coding</span><span class="hljs-comment"> scheme is equivalent </span><span class="hljs-comment">to</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L133" href="#L133" data-line-number="133" class="gl-user-select-none gl-shadow-none! file-line-num">
      133
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC133" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">   a Pyramid Vector </span><span class="hljs-comment">Quantizer \cite{Fis86}.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L134" href="#L134" data-line-number="134" class="gl-user-select-none gl-shadow-none! file-line-num">
      134
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC134" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">  Some additional notes </span><span class="hljs-comment">about an</span><span class="hljs-comment"> early version appear </span><span class="hljs-comment">at</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L135" href="#L135" data-line-number="135" class="gl-user-select-none gl-shadow-none! file-line-num">
      135
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC135" lang="c" data-testid="content" class="line"><span class="hljs-comment">   http://people.xiph.org/~tterribe/notes/cwrs.html,</span><span class="hljs-comment"> but the codebook </span><span class="hljs-comment">ordering</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L136" href="#L136" data-line-number="136" class="gl-user-select-none gl-shadow-none! file-line-num">
      136
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC136" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">   and the definitions </span><span class="hljs-comment">of</span><span class="hljs-comment"> some terms have </span><span class="hljs-comment">evolved</span><span class="hljs-comment"> since that was </span><span class="hljs-comment">written.</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L137" href="#L137" data-line-number="137" class="gl-user-select-none gl-shadow-none! file-line-num">
      137
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC137" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L138" href="#L138" data-line-number="138" class="gl-user-select-none gl-shadow-none! file-line-num">
      138
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC138" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">  The conversion from </span><span class="hljs-comment">a</span><span class="hljs-comment"> pulse vector to </span><span class="hljs-comment">an integer index (encoding) and back</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L139" href="#L139" data-line-number="139" class="gl-user-select-none gl-shadow-none! file-line-num">
      139
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC139" lang="c" data-testid="content" class="line"><span class="hljs-comment">   (decoding) is governed by two related functions, V(N,K) and U(N,K).</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L140" href="#L140" data-line-number="140" class="gl-user-select-none gl-shadow-none! file-line-num">
      140
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC140" lang="c" data-testid="content" class="line"><span class="hljs-comment"></span></span></code></pre></div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L141" data-testid="line-number">141</span><span id="L142" data-testid="line-number">142</span><span id="L143" data-testid="line-number">143</span><span id="L144" data-testid="line-number">144</span><span id="L145" data-testid="line-number">145</span><span id="L146" data-testid="line-number">146</span><span id="L147" data-testid="line-number">147</span><span id="L148" data-testid="line-number">148</span><span id="L149" data-testid="line-number">149</span><span id="L150" data-testid="line-number">150</span><span id="L151" data-testid="line-number">151</span><span id="L152" data-testid="line-number">152</span><span id="L153" data-testid="line-number">153</span><span id="L154" data-testid="line-number">154</span><span id="L155" data-testid="line-number">155</span><span id="L156" data-testid="line-number">156</span><span id="L157" data-testid="line-number">157</span><span id="L158" data-testid="line-number">158</span><span id="L159" data-testid="line-number">159</span><span id="L160" data-testid="line-number">160</span><span id="L161" data-testid="line-number">161</span><span id="L162" data-testid="line-number">162</span><span id="L163" data-testid="line-number">163</span><span id="L164" data-testid="line-number">164</span><span id="L165" data-testid="line-number">165</span><span id="L166" data-testid="line-number">166</span><span id="L167" data-testid="line-number">167</span><span id="L168" data-testid="line-number">168</span><span id="L169" data-testid="line-number">169</span><span id="L170" data-testid="line-number">170</span><span id="L171" data-testid="line-number">171</span><span id="L172" data-testid="line-number">172</span><span id="L173" data-testid="line-number">173</span><span id="L174" data-testid="line-number">174</span><span id="L175" data-testid="line-number">175</span><span id="L176" data-testid="line-number">176</span><span id="L177" data-testid="line-number">177</span><span id="L178" data-testid="line-number">178</span><span id="L179" data-testid="line-number">179</span><span id="L180" data-testid="line-number">180</span><span id="L181" data-testid="line-number">181</span><span id="L182" data-testid="line-number">182</span><span id="L183" data-testid="line-number">183</span><span id="L184" data-testid="line-number">184</span><span id="L185" data-testid="line-number">185</span><span id="L186" data-testid="line-number">186</span><span id="L187" data-testid="line-number">187</span><span id="L188" data-testid="line-number">188</span><span id="L189" data-testid="line-number">189</span><span id="L190" data-testid="line-number">190</span><span id="L191" data-testid="line-number">191</span><span id="L192" data-testid="line-number">192</span><span id="L193" data-testid="line-number">193</span><span id="L194" data-testid="line-number">194</span><span id="L195" data-testid="line-number">195</span><span id="L196" data-testid="line-number">196</span><span id="L197" data-testid="line-number">197</span><span id="L198" data-testid="line-number">198</span><span id="L199" data-testid="line-number">199</span><span id="L200" data-testid="line-number">200</span><span id="L201" data-testid="line-number">201</span><span id="L202" data-testid="line-number">202</span><span id="L203" data-testid="line-number">203</span><span id="L204" data-testid="line-number">204</span><span id="L205" data-testid="line-number">205</span><span id="L206" data-testid="line-number">206</span><span id="L207" data-testid="line-number">207</span><span id="L208" data-testid="line-number">208</span><span id="L209" data-testid="line-number">209</span><span id="L210" data-testid="line-number">210</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">  V(N,K) = the number of combinations, with replacement, of N items, taken K
   at a time, when a sign bit is added to each item taken at least once (i.e.,
   the number of N-dimensional unit pulse vectors with K pulses).
  One way to compute this is via
    V(N,K) = K&gt;0 ? sum(k=1...K,2**k*choose(N,k)*choose(K-1,k-1)) : 1,
   where choose() is the binomial function.
  A table of values for N&lt;10 and K&lt;10 looks like:
  V[10][10] = {
    {1,  0,   0,    0,    0,     0,     0,      0,      0,       0},
    {1,  2,   2,    2,    2,     2,     2,      2,      2,       2},
    {1,  4,   8,   12,   16,    20,    24,     28,     32,      36},
    {1,  6,  18,   38,   66,   102,   146,    198,    258,     326},
    {1,  8,  32,   88,  192,   360,   608,    952,   1408,    1992},
    {1, 10,  50,  170,  450,  1002,  1970,   3530,   5890,    9290},
    {1, 12,  72,  292,  912,  2364,  5336,  10836,  20256,   35436},
    {1, 14,  98,  462, 1666,  4942, 12642,  28814,  59906,  115598},
    {1, 16, 128,  688, 2816,  9424, 27008,  68464, 157184,  332688},
    {1, 18, 162,  978, 4482, 16722, 53154, 148626, 374274,  864146}
  };

  U(N,K) = the number of such combinations wherein N-1 objects are taken at
   most K-1 at a time.
  This is given by
    U(N,K) = sum(k=0...K-1,V(N-1,k))
           = K&gt;0 ? (V(N-1,K-1) + V(N,K-1))/2 : 0.
  The latter expression also makes clear that U(N,K) is half the number of such
   combinations wherein the first object is taken at least once.
  Although it may not be clear from either of these definitions, U(N,K) is the
   natural function to work with when enumerating the pulse vector codebooks,
   not V(N,K).
  U(N,K) is not well-defined for N=0, but with the extension
    U(0,K) = K&gt;0 ? 0 : 1,
   the function becomes symmetric: U(N,K) = U(K,N), with a similar table:
  U[10][10] = {
    {1, 0,  0,   0,    0,    0,     0,     0,      0,      0},
    {0, 1,  1,   1,    1,    1,     1,     1,      1,      1},
    {0, 1,  3,   5,    7,    9,    11,    13,     15,     17},
    {0, 1,  5,  13,   25,   41,    61,    85,    113,    145},
    {0, 1,  7,  25,   63,  129,   231,   377,    575,    833},
    {0, 1,  9,  41,  129,  321,   681,  1289,   2241,   3649},
    {0, 1, 11,  61,  231,  681,  1683,  3653,   7183,  13073},
    {0, 1, 13,  85,  377, 1289,  3653,  8989,  19825,  40081},
    {0, 1, 15, 113,  575, 2241,  7183, 19825,  48639, 108545},
    {0, 1, 17, 145,  833, 3649, 13073, 40081, 108545, 265729}
  };

  With this extension, V(N,K) may be written in terms of U(N,K):
    V(N,K) = U(N,K) + U(N,K+1)
   for all N&gt;=0, K&gt;=0.
  Thus U(N,K+1) represents the number of combinations where the first element
   is positive or zero, and U(N,K) represents the number of combinations where
   it is negative.
  With a large enough table of U(N,K) values, we could write O(N) encoding
   and O(min(N*log(K),N+K)) decoding routines, but such a table would be
   prohibitively large for small embedded devices (K may be as large as 32767
   for small N, and N may be as large as 200).

  Both functions obey the same recurrence relation:
    V(N,K) = V(N-1,K) + V(N,K-1) + V(N-1,K-1),
    U(N,K) = U(N-1,K) + U(N,K-1) + U(N-1,K-1),
   for all N&gt;0, K&gt;0, with different initial conditions at N=0 or K=0.
  This allows us to construct a row of one of the tables above given the
   previous row or the next row.
  Thus we can derive O(NK) encoding and decoding routines with O(K) memory
   using only addition and subtraction.

  When encoding, we build up from the U(2,K) row and work our way forwards.
  When decoding, we need to start at the U(N,K) row and work our way backwards,
   which requires a means of computing U(N,K).
  U(N,K) may be computed from two previous values with the same N:</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L211" data-testid="line-number">211</span><span id="L212" data-testid="line-number">212</span><span id="L213" data-testid="line-number">213</span><span id="L214" data-testid="line-number">214</span><span id="L215" data-testid="line-number">215</span><span id="L216" data-testid="line-number">216</span><span id="L217" data-testid="line-number">217</span><span id="L218" data-testid="line-number">218</span><span id="L219" data-testid="line-number">219</span><span id="L220" data-testid="line-number">220</span><span id="L221" data-testid="line-number">221</span><span id="L222" data-testid="line-number">222</span><span id="L223" data-testid="line-number">223</span><span id="L224" data-testid="line-number">224</span><span id="L225" data-testid="line-number">225</span><span id="L226" data-testid="line-number">226</span><span id="L227" data-testid="line-number">227</span><span id="L228" data-testid="line-number">228</span><span id="L229" data-testid="line-number">229</span><span id="L230" data-testid="line-number">230</span><span id="L231" data-testid="line-number">231</span><span id="L232" data-testid="line-number">232</span><span id="L233" data-testid="line-number">233</span><span id="L234" data-testid="line-number">234</span><span id="L235" data-testid="line-number">235</span><span id="L236" data-testid="line-number">236</span><span id="L237" data-testid="line-number">237</span><span id="L238" data-testid="line-number">238</span><span id="L239" data-testid="line-number">239</span><span id="L240" data-testid="line-number">240</span><span id="L241" data-testid="line-number">241</span><span id="L242" data-testid="line-number">242</span><span id="L243" data-testid="line-number">243</span><span id="L244" data-testid="line-number">244</span><span id="L245" data-testid="line-number">245</span><span id="L246" data-testid="line-number">246</span><span id="L247" data-testid="line-number">247</span><span id="L248" data-testid="line-number">248</span><span id="L249" data-testid="line-number">249</span><span id="L250" data-testid="line-number">250</span><span id="L251" data-testid="line-number">251</span><span id="L252" data-testid="line-number">252</span><span id="L253" data-testid="line-number">253</span><span id="L254" data-testid="line-number">254</span><span id="L255" data-testid="line-number">255</span><span id="L256" data-testid="line-number">256</span><span id="L257" data-testid="line-number">257</span><span id="L258" data-testid="line-number">258</span><span id="L259" data-testid="line-number">259</span><span id="L260" data-testid="line-number">260</span><span id="L261" data-testid="line-number">261</span><span id="L262" data-testid="line-number">262</span><span id="L263" data-testid="line-number">263</span><span id="L264" data-testid="line-number">264</span><span id="L265" data-testid="line-number">265</span><span id="L266" data-testid="line-number">266</span><span id="L267" data-testid="line-number">267</span><span id="L268" data-testid="line-number">268</span><span id="L269" data-testid="line-number">269</span><span id="L270" data-testid="line-number">270</span><span id="L271" data-testid="line-number">271</span><span id="L272" data-testid="line-number">272</span><span id="L273" data-testid="line-number">273</span><span id="L274" data-testid="line-number">274</span><span id="L275" data-testid="line-number">275</span><span id="L276" data-testid="line-number">276</span><span id="L277" data-testid="line-number">277</span><span id="L278" data-testid="line-number">278</span><span id="L279" data-testid="line-number">279</span><span id="L280" data-testid="line-number">280</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">    U(N,K) = ((2*N-1)*U(N,K-1) - U(N,K-2))/(K-1) + U(N,K-2)
   for all N&gt;1, and since U(N,K) is symmetric, a similar relation holds for two
   previous values with the same K:
    U(N,K&gt;1) = ((2*K-1)*U(N-1,K) - U(N-2,K))/(N-1) + U(N-2,K)
   for all K&gt;1.
  This allows us to construct an arbitrary row of the U(N,K) table by starting
   with the first two values, which are constants.
  This saves roughly 2/3 the work in our O(NK) decoding routine, but costs O(K)
   multiplications.
  Similar relations can be derived for V(N,K), but are not used here.

  For N&gt;0 and K&gt;0, U(N,K) and V(N,K) take on the form of an (N-1)-degree
   polynomial for fixed N.
  The first few are
    U(1,K) = 1,
    U(2,K) = 2*K-1,
    U(3,K) = (2*K-2)*K+1,
    U(4,K) = (((4*K-6)*K+8)*K-3)/3,
    U(5,K) = ((((2*K-4)*K+10)*K-8)*K+3)/3,
   and
    V(1,K) = 2,
    V(2,K) = 4*K,
    V(3,K) = 4*K*K+2,
    V(4,K) = 8*(K*K+2)*K/3,
    V(5,K) = ((4*K*K+20)*K*K+6)/3,
   for all K&gt;0.
  This allows us to derive O(N) encoding and O(N*log(K)) decoding routines for
   small N (and indeed decoding is also O(N) for N&lt;3).

  @ARTICLE{Fis86,
    author="Thomas R. Fischer",
    title="A Pyramid Vector Quantizer",
    journal="IEEE Transactions on Information Theory",
    volume="IT-32",
    number=4,
    pages="568--583",
    month=Jul,
    year=1986
  }*/

#ifndef SMALL_FOOTPRINT
/*Compute U(2,_k).
  Note that this may be called with _k=32768 (maxK[2]+1).*/
static inline unsigned ucwrs2(unsigned _k){
  celt_assert(_k&gt;0);
  return _k+(_k-1);
}

/*Compute V(2,_k).*/
static inline opus_uint32 ncwrs2(int _k){
  celt_assert(_k&gt;0);
  return 4*(opus_uint32)_k;
}

/*Compute U(3,_k).
  Note that this may be called with _k=32768 (maxK[3]+1).*/
static inline opus_uint32 ucwrs3(unsigned _k){
  celt_assert(_k&gt;0);
  return (2*(opus_uint32)_k-2)*_k+1;
}

/*Compute V(3,_k).*/
static inline opus_uint32 ncwrs3(int _k){
  celt_assert(_k&gt;0);
  return 2*(2*(unsigned)_k*(opus_uint32)_k+1);
}

/*Compute U(4,_k).*/
static inline opus_uint32 ucwrs4(int _k){
  celt_assert(_k&gt;0);</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L281" data-testid="line-number">281</span><span id="L282" data-testid="line-number">282</span><span id="L283" data-testid="line-number">283</span><span id="L284" data-testid="line-number">284</span><span id="L285" data-testid="line-number">285</span><span id="L286" data-testid="line-number">286</span><span id="L287" data-testid="line-number">287</span><span id="L288" data-testid="line-number">288</span><span id="L289" data-testid="line-number">289</span><span id="L290" data-testid="line-number">290</span><span id="L291" data-testid="line-number">291</span><span id="L292" data-testid="line-number">292</span><span id="L293" data-testid="line-number">293</span><span id="L294" data-testid="line-number">294</span><span id="L295" data-testid="line-number">295</span><span id="L296" data-testid="line-number">296</span><span id="L297" data-testid="line-number">297</span><span id="L298" data-testid="line-number">298</span><span id="L299" data-testid="line-number">299</span><span id="L300" data-testid="line-number">300</span><span id="L301" data-testid="line-number">301</span><span id="L302" data-testid="line-number">302</span><span id="L303" data-testid="line-number">303</span><span id="L304" data-testid="line-number">304</span><span id="L305" data-testid="line-number">305</span><span id="L306" data-testid="line-number">306</span><span id="L307" data-testid="line-number">307</span><span id="L308" data-testid="line-number">308</span><span id="L309" data-testid="line-number">309</span><span id="L310" data-testid="line-number">310</span><span id="L311" data-testid="line-number">311</span><span id="L312" data-testid="line-number">312</span><span id="L313" data-testid="line-number">313</span><span id="L314" data-testid="line-number">314</span><span id="L315" data-testid="line-number">315</span><span id="L316" data-testid="line-number">316</span><span id="L317" data-testid="line-number">317</span><span id="L318" data-testid="line-number">318</span><span id="L319" data-testid="line-number">319</span><span id="L320" data-testid="line-number">320</span><span id="L321" data-testid="line-number">321</span><span id="L322" data-testid="line-number">322</span><span id="L323" data-testid="line-number">323</span><span id="L324" data-testid="line-number">324</span><span id="L325" data-testid="line-number">325</span><span id="L326" data-testid="line-number">326</span><span id="L327" data-testid="line-number">327</span><span id="L328" data-testid="line-number">328</span><span id="L329" data-testid="line-number">329</span><span id="L330" data-testid="line-number">330</span><span id="L331" data-testid="line-number">331</span><span id="L332" data-testid="line-number">332</span><span id="L333" data-testid="line-number">333</span><span id="L334" data-testid="line-number">334</span><span id="L335" data-testid="line-number">335</span><span id="L336" data-testid="line-number">336</span><span id="L337" data-testid="line-number">337</span><span id="L338" data-testid="line-number">338</span><span id="L339" data-testid="line-number">339</span><span id="L340" data-testid="line-number">340</span><span id="L341" data-testid="line-number">341</span><span id="L342" data-testid="line-number">342</span><span id="L343" data-testid="line-number">343</span><span id="L344" data-testid="line-number">344</span><span id="L345" data-testid="line-number">345</span><span id="L346" data-testid="line-number">346</span><span id="L347" data-testid="line-number">347</span><span id="L348" data-testid="line-number">348</span><span id="L349" data-testid="line-number">349</span><span id="L350" data-testid="line-number">350</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">  return imusdiv32odd(2*_k,(2*_k-3)*(opus_uint32)_k+4,3,1);
}

/*Compute V(4,_k).*/
static inline opus_uint32 ncwrs4(int _k){
  celt_assert(_k&gt;0);
  return ((_k*(opus_uint32)_k+2)*_k)/3&lt;&lt;3;
}

#endif /* SMALL_FOOTPRINT */

/*Computes the next row/column of any recurrence that obeys the relation
   u[i][j]=u[i-1][j]+u[i][j-1]+u[i-1][j-1].
  _ui0 is the base case for the new row/column.*/
static inline void unext(opus_uint32 *_ui,unsigned _len,opus_uint32 _ui0){
  opus_uint32 ui1;
  unsigned      j;
  /*This do-while will overrun the array if we don't have storage for at least
     2 values.*/
  j=1; do {
    ui1=UADD32(UADD32(_ui[j],_ui[j-1]),_ui0);
    _ui[j-1]=_ui0;
    _ui0=ui1;
  } while (++j&lt;_len);
  _ui[j-1]=_ui0;
}

/*Computes the previous row/column of any recurrence that obeys the relation
   u[i-1][j]=u[i][j]-u[i][j-1]-u[i-1][j-1].
  _ui0 is the base case for the new row/column.*/
static inline void uprev(opus_uint32 *_ui,unsigned _n,opus_uint32 _ui0){
  opus_uint32 ui1;
  unsigned      j;
  /*This do-while will overrun the array if we don't have storage for at least
     2 values.*/
  j=1; do {
    ui1=USUB32(USUB32(_ui[j],_ui[j-1]),_ui0);
    _ui[j-1]=_ui0;
    _ui0=ui1;
  } while (++j&lt;_n);
  _ui[j-1]=_ui0;
}

/*Compute V(_n,_k), as well as U(_n,0..._k+1).
  _u: On exit, _u[i] contains U(_n,i) for i in [0..._k+1].*/
static opus_uint32 ncwrs_urow(unsigned _n,unsigned _k,opus_uint32 *_u){
  opus_uint32 um2;
  unsigned      len;
  unsigned      k;
  len=_k+2;
  /*We require storage at least 3 values (e.g., _k&gt;0).*/
  celt_assert(len&gt;=3);
  _u[0]=0;
  _u[1]=um2=1;
#ifndef SMALL_FOOTPRINT
  /*_k&gt;52 doesn't work in the false branch due to the limits of INV_TABLE,
    but _k isn't tested here because k&lt;=52 for n=7*/
  if(_n&lt;=6)
#endif
  {
    /*If _n==0, _u[0] should be 1 and the rest should be 0.*/
    /*If _n==1, _u[i] should be 1 for i&gt;1.*/
    celt_assert(_n&gt;=2);
    /*If _k==0, the following do-while loop will overflow the buffer.*/
    celt_assert(_k&gt;0);
    k=2;
    do _u[k]=(k&lt;&lt;1)-1;
    while(++k&lt;len);
    for(k=2;k&lt;_n;k++)unext(_u+1,_k+1,1);
  }</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L351" data-testid="line-number">351</span><span id="L352" data-testid="line-number">352</span><span id="L353" data-testid="line-number">353</span><span id="L354" data-testid="line-number">354</span><span id="L355" data-testid="line-number">355</span><span id="L356" data-testid="line-number">356</span><span id="L357" data-testid="line-number">357</span><span id="L358" data-testid="line-number">358</span><span id="L359" data-testid="line-number">359</span><span id="L360" data-testid="line-number">360</span><span id="L361" data-testid="line-number">361</span><span id="L362" data-testid="line-number">362</span><span id="L363" data-testid="line-number">363</span><span id="L364" data-testid="line-number">364</span><span id="L365" data-testid="line-number">365</span><span id="L366" data-testid="line-number">366</span><span id="L367" data-testid="line-number">367</span><span id="L368" data-testid="line-number">368</span><span id="L369" data-testid="line-number">369</span><span id="L370" data-testid="line-number">370</span><span id="L371" data-testid="line-number">371</span><span id="L372" data-testid="line-number">372</span><span id="L373" data-testid="line-number">373</span><span id="L374" data-testid="line-number">374</span><span id="L375" data-testid="line-number">375</span><span id="L376" data-testid="line-number">376</span><span id="L377" data-testid="line-number">377</span><span id="L378" data-testid="line-number">378</span><span id="L379" data-testid="line-number">379</span><span id="L380" data-testid="line-number">380</span><span id="L381" data-testid="line-number">381</span><span id="L382" data-testid="line-number">382</span><span id="L383" data-testid="line-number">383</span><span id="L384" data-testid="line-number">384</span><span id="L385" data-testid="line-number">385</span><span id="L386" data-testid="line-number">386</span><span id="L387" data-testid="line-number">387</span><span id="L388" data-testid="line-number">388</span><span id="L389" data-testid="line-number">389</span><span id="L390" data-testid="line-number">390</span><span id="L391" data-testid="line-number">391</span><span id="L392" data-testid="line-number">392</span><span id="L393" data-testid="line-number">393</span><span id="L394" data-testid="line-number">394</span><span id="L395" data-testid="line-number">395</span><span id="L396" data-testid="line-number">396</span><span id="L397" data-testid="line-number">397</span><span id="L398" data-testid="line-number">398</span><span id="L399" data-testid="line-number">399</span><span id="L400" data-testid="line-number">400</span><span id="L401" data-testid="line-number">401</span><span id="L402" data-testid="line-number">402</span><span id="L403" data-testid="line-number">403</span><span id="L404" data-testid="line-number">404</span><span id="L405" data-testid="line-number">405</span><span id="L406" data-testid="line-number">406</span><span id="L407" data-testid="line-number">407</span><span id="L408" data-testid="line-number">408</span><span id="L409" data-testid="line-number">409</span><span id="L410" data-testid="line-number">410</span><span id="L411" data-testid="line-number">411</span><span id="L412" data-testid="line-number">412</span><span id="L413" data-testid="line-number">413</span><span id="L414" data-testid="line-number">414</span><span id="L415" data-testid="line-number">415</span><span id="L416" data-testid="line-number">416</span><span id="L417" data-testid="line-number">417</span><span id="L418" data-testid="line-number">418</span><span id="L419" data-testid="line-number">419</span><span id="L420" data-testid="line-number">420</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">#ifndef SMALL_FOOTPRINT
  else{
    opus_uint32 um1;
    opus_uint32 n2m1;
    _u[2]=n2m1=um1=(_n&lt;&lt;1)-1;
    for(k=3;k&lt;len;k++){
      /*U(N,K) = ((2*N-1)*U(N,K-1)-U(N,K-2))/(K-1) + U(N,K-2)*/
      _u[k]=um2=imusdiv32even(n2m1,um1,um2,k-1)+um2;
      if(++k&gt;=len)break;
      _u[k]=um1=imusdiv32odd(n2m1,um2,um1,(k-1)&gt;&gt;1)+um1;
    }
  }
#endif /* SMALL_FOOTPRINT */
  return _u[_k]+_u[_k+1];
}

#ifndef SMALL_FOOTPRINT

/*Returns the _i'th combination of _k elements (at most 32767) chosen from a
   set of size 1 with associated sign bits.
  _y: Returns the vector of pulses.*/
static inline void cwrsi1(int _k,opus_uint32 _i,int *_y){
  int s;
  s=-(int)_i;
  _y[0]=(_k+s)^s;
}

/*Returns the _i'th combination of _k elements (at most 32767) chosen from a
   set of size 2 with associated sign bits.
  _y: Returns the vector of pulses.*/
static inline void cwrsi2(int _k,opus_uint32 _i,int *_y){
  opus_uint32 p;
  int           s;
  int           yj;
  p=ucwrs2(_k+1U);
  s=-(_i&gt;=p);
  _i-=p&amp;s;
  yj=_k;
  _k=(_i+1)&gt;&gt;1;
  p=_k?ucwrs2(_k):0;
  _i-=p;
  yj-=_k;
  _y[0]=(yj+s)^s;
  cwrsi1(_k,_i,_y+1);
}

/*Returns the _i'th combination of _k elements (at most 32767) chosen from a
   set of size 3 with associated sign bits.
  _y: Returns the vector of pulses.*/
static void cwrsi3(int _k,opus_uint32 _i,int *_y){
  opus_uint32 p;
  int           s;
  int           yj;
  p=ucwrs3(_k+1U);
  s=-(_i&gt;=p);
  _i-=p&amp;s;
  yj=_k;
  /*Finds the maximum _k such that ucwrs3(_k)&lt;=_i (tested for all
     _i&lt;2147418113=U(3,32768)).*/
  _k=_i&gt;0?(isqrt32(2*_i-1)+1)&gt;&gt;1:0;
  p=_k?ucwrs3(_k):0;
  _i-=p;
  yj-=_k;
  _y[0]=(yj+s)^s;
  cwrsi2(_k,_i,_y+1);
}

/*Returns the _i'th combination of _k elements (at most 1172) chosen from a set
   of size 4 with associated sign bits.
  _y: Returns the vector of pulses.*/</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L421" data-testid="line-number">421</span><span id="L422" data-testid="line-number">422</span><span id="L423" data-testid="line-number">423</span><span id="L424" data-testid="line-number">424</span><span id="L425" data-testid="line-number">425</span><span id="L426" data-testid="line-number">426</span><span id="L427" data-testid="line-number">427</span><span id="L428" data-testid="line-number">428</span><span id="L429" data-testid="line-number">429</span><span id="L430" data-testid="line-number">430</span><span id="L431" data-testid="line-number">431</span><span id="L432" data-testid="line-number">432</span><span id="L433" data-testid="line-number">433</span><span id="L434" data-testid="line-number">434</span><span id="L435" data-testid="line-number">435</span><span id="L436" data-testid="line-number">436</span><span id="L437" data-testid="line-number">437</span><span id="L438" data-testid="line-number">438</span><span id="L439" data-testid="line-number">439</span><span id="L440" data-testid="line-number">440</span><span id="L441" data-testid="line-number">441</span><span id="L442" data-testid="line-number">442</span><span id="L443" data-testid="line-number">443</span><span id="L444" data-testid="line-number">444</span><span id="L445" data-testid="line-number">445</span><span id="L446" data-testid="line-number">446</span><span id="L447" data-testid="line-number">447</span><span id="L448" data-testid="line-number">448</span><span id="L449" data-testid="line-number">449</span><span id="L450" data-testid="line-number">450</span><span id="L451" data-testid="line-number">451</span><span id="L452" data-testid="line-number">452</span><span id="L453" data-testid="line-number">453</span><span id="L454" data-testid="line-number">454</span><span id="L455" data-testid="line-number">455</span><span id="L456" data-testid="line-number">456</span><span id="L457" data-testid="line-number">457</span><span id="L458" data-testid="line-number">458</span><span id="L459" data-testid="line-number">459</span><span id="L460" data-testid="line-number">460</span><span id="L461" data-testid="line-number">461</span><span id="L462" data-testid="line-number">462</span><span id="L463" data-testid="line-number">463</span><span id="L464" data-testid="line-number">464</span><span id="L465" data-testid="line-number">465</span><span id="L466" data-testid="line-number">466</span><span id="L467" data-testid="line-number">467</span><span id="L468" data-testid="line-number">468</span><span id="L469" data-testid="line-number">469</span><span id="L470" data-testid="line-number">470</span><span id="L471" data-testid="line-number">471</span><span id="L472" data-testid="line-number">472</span><span id="L473" data-testid="line-number">473</span><span id="L474" data-testid="line-number">474</span><span id="L475" data-testid="line-number">475</span><span id="L476" data-testid="line-number">476</span><span id="L477" data-testid="line-number">477</span><span id="L478" data-testid="line-number">478</span><span id="L479" data-testid="line-number">479</span><span id="L480" data-testid="line-number">480</span><span id="L481" data-testid="line-number">481</span><span id="L482" data-testid="line-number">482</span><span id="L483" data-testid="line-number">483</span><span id="L484" data-testid="line-number">484</span><span id="L485" data-testid="line-number">485</span><span id="L486" data-testid="line-number">486</span><span id="L487" data-testid="line-number">487</span><span id="L488" data-testid="line-number">488</span><span id="L489" data-testid="line-number">489</span><span id="L490" data-testid="line-number">490</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">static void cwrsi4(int _k,opus_uint32 _i,int *_y){
  opus_uint32 p;
  int           s;
  int           yj;
  int           kl;
  int           kr;
  p=ucwrs4(_k+1);
  s=-(_i&gt;=p);
  _i-=p&amp;s;
  yj=_k;
  /*We could solve a cubic for k here, but the form of the direct solution does
     not lend itself well to exact integer arithmetic.
    Instead we do a binary search on U(4,K).*/
  kl=0;
  kr=_k;
  for(;;){
    _k=(kl+kr)&gt;&gt;1;
    p=_k?ucwrs4(_k):0;
    if(p&lt;_i){
      if(_k&gt;=kr)break;
      kl=_k+1;
    }
    else if(p&gt;_i)kr=_k-1;
    else break;
  }
  _i-=p;
  yj-=_k;
  _y[0]=(yj+s)^s;
  cwrsi3(_k,_i,_y+1);
}

#endif /* SMALL_FOOTPRINT */

/*Returns the _i'th combination of _k elements chosen from a set of size _n
   with associated sign bits.
  _y: Returns the vector of pulses.
  _u: Must contain entries [0..._k+1] of row _n of U() on input.
      Its contents will be destructively modified.*/
static void cwrsi(int _n,int _k,opus_uint32 _i,int *_y,opus_uint32 *_u){
  int j;
  celt_assert(_n&gt;0);
  j=0;
  do{
    opus_uint32 p;
    int           s;
    int           yj;
    p=_u[_k+1];
    s=-(_i&gt;=p);
    _i-=p&amp;s;
    yj=_k;
    p=_u[_k];
    while(p&gt;_i)p=_u[--_k];
    _i-=p;
    yj-=_k;
    _y[j]=(yj+s)^s;
    uprev(_u,_k+2,0);
  }
  while(++j&lt;_n);
}

/*Returns the index of the given combination of K elements chosen from a set
   of size 1 with associated sign bits.
  _y: The vector of pulses, whose sum of absolute values is K.
  _k: Returns K.*/
static inline opus_uint32 icwrs1(const int *_y,int *_k){
  *_k=abs(_y[0]);
  return _y[0]&lt;0;
}

#ifndef SMALL_FOOTPRINT</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L491" data-testid="line-number">491</span><span id="L492" data-testid="line-number">492</span><span id="L493" data-testid="line-number">493</span><span id="L494" data-testid="line-number">494</span><span id="L495" data-testid="line-number">495</span><span id="L496" data-testid="line-number">496</span><span id="L497" data-testid="line-number">497</span><span id="L498" data-testid="line-number">498</span><span id="L499" data-testid="line-number">499</span><span id="L500" data-testid="line-number">500</span><span id="L501" data-testid="line-number">501</span><span id="L502" data-testid="line-number">502</span><span id="L503" data-testid="line-number">503</span><span id="L504" data-testid="line-number">504</span><span id="L505" data-testid="line-number">505</span><span id="L506" data-testid="line-number">506</span><span id="L507" data-testid="line-number">507</span><span id="L508" data-testid="line-number">508</span><span id="L509" data-testid="line-number">509</span><span id="L510" data-testid="line-number">510</span><span id="L511" data-testid="line-number">511</span><span id="L512" data-testid="line-number">512</span><span id="L513" data-testid="line-number">513</span><span id="L514" data-testid="line-number">514</span><span id="L515" data-testid="line-number">515</span><span id="L516" data-testid="line-number">516</span><span id="L517" data-testid="line-number">517</span><span id="L518" data-testid="line-number">518</span><span id="L519" data-testid="line-number">519</span><span id="L520" data-testid="line-number">520</span><span id="L521" data-testid="line-number">521</span><span id="L522" data-testid="line-number">522</span><span id="L523" data-testid="line-number">523</span><span id="L524" data-testid="line-number">524</span><span id="L525" data-testid="line-number">525</span><span id="L526" data-testid="line-number">526</span><span id="L527" data-testid="line-number">527</span><span id="L528" data-testid="line-number">528</span><span id="L529" data-testid="line-number">529</span><span id="L530" data-testid="line-number">530</span><span id="L531" data-testid="line-number">531</span><span id="L532" data-testid="line-number">532</span><span id="L533" data-testid="line-number">533</span><span id="L534" data-testid="line-number">534</span><span id="L535" data-testid="line-number">535</span><span id="L536" data-testid="line-number">536</span><span id="L537" data-testid="line-number">537</span><span id="L538" data-testid="line-number">538</span><span id="L539" data-testid="line-number">539</span><span id="L540" data-testid="line-number">540</span><span id="L541" data-testid="line-number">541</span><span id="L542" data-testid="line-number">542</span><span id="L543" data-testid="line-number">543</span><span id="L544" data-testid="line-number">544</span><span id="L545" data-testid="line-number">545</span><span id="L546" data-testid="line-number">546</span><span id="L547" data-testid="line-number">547</span><span id="L548" data-testid="line-number">548</span><span id="L549" data-testid="line-number">549</span><span id="L550" data-testid="line-number">550</span><span id="L551" data-testid="line-number">551</span><span id="L552" data-testid="line-number">552</span><span id="L553" data-testid="line-number">553</span><span id="L554" data-testid="line-number">554</span><span id="L555" data-testid="line-number">555</span><span id="L556" data-testid="line-number">556</span><span id="L557" data-testid="line-number">557</span><span id="L558" data-testid="line-number">558</span><span id="L559" data-testid="line-number">559</span><span id="L560" data-testid="line-number">560</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">
/*Returns the index of the given combination of K elements chosen from a set
   of size 2 with associated sign bits.
  _y: The vector of pulses, whose sum of absolute values is K.
  _k: Returns K.*/
static inline opus_uint32 icwrs2(const int *_y,int *_k){
  opus_uint32 i;
  int           k;
  i=icwrs1(_y+1,&amp;k);
  i+=k?ucwrs2(k):0;
  k+=abs(_y[0]);
  if(_y[0]&lt;0)i+=ucwrs2(k+1U);
  *_k=k;
  return i;
}

/*Returns the index of the given combination of K elements chosen from a set
   of size 3 with associated sign bits.
  _y: The vector of pulses, whose sum of absolute values is K.
  _k: Returns K.*/
static inline opus_uint32 icwrs3(const int *_y,int *_k){
  opus_uint32 i;
  int           k;
  i=icwrs2(_y+1,&amp;k);
  i+=k?ucwrs3(k):0;
  k+=abs(_y[0]);
  if(_y[0]&lt;0)i+=ucwrs3(k+1U);
  *_k=k;
  return i;
}

/*Returns the index of the given combination of K elements chosen from a set
   of size 4 with associated sign bits.
  _y: The vector of pulses, whose sum of absolute values is K.
  _k: Returns K.*/
static inline opus_uint32 icwrs4(const int *_y,int *_k){
  opus_uint32 i;
  int           k;
  i=icwrs3(_y+1,&amp;k);
  i+=k?ucwrs4(k):0;
  k+=abs(_y[0]);
  if(_y[0]&lt;0)i+=ucwrs4(k+1);
  *_k=k;
  return i;
}

#endif /* SMALL_FOOTPRINT */

/*Returns the index of the given combination of K elements chosen from a set
   of size _n with associated sign bits.
  _y:  The vector of pulses, whose sum of absolute values must be _k.
  _nc: Returns V(_n,_k).*/
static inline opus_uint32 icwrs(int _n,int _k,opus_uint32 *_nc,const int *_y,
 opus_uint32 *_u){
  opus_uint32 i;
  int           j;
  int           k;
  /*We can't unroll the first two iterations of the loop unless _n&gt;=2.*/
  celt_assert(_n&gt;=2);
  _u[0]=0;
  for(k=1;k&lt;=_k+1;k++)_u[k]=(k&lt;&lt;1)-1;
  i=icwrs1(_y+_n-1,&amp;k);
  j=_n-2;
  i+=_u[k];
  k+=abs(_y[j]);
  if(_y[j]&lt;0)i+=_u[k+1];
  while(j--&gt;0){
    unext(_u,_k+2,0);
    i+=_u[k];
    k+=abs(_y[j]);</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L561" data-testid="line-number">561</span><span id="L562" data-testid="line-number">562</span><span id="L563" data-testid="line-number">563</span><span id="L564" data-testid="line-number">564</span><span id="L565" data-testid="line-number">565</span><span id="L566" data-testid="line-number">566</span><span id="L567" data-testid="line-number">567</span><span id="L568" data-testid="line-number">568</span><span id="L569" data-testid="line-number">569</span><span id="L570" data-testid="line-number">570</span><span id="L571" data-testid="line-number">571</span><span id="L572" data-testid="line-number">572</span><span id="L573" data-testid="line-number">573</span><span id="L574" data-testid="line-number">574</span><span id="L575" data-testid="line-number">575</span><span id="L576" data-testid="line-number">576</span><span id="L577" data-testid="line-number">577</span><span id="L578" data-testid="line-number">578</span><span id="L579" data-testid="line-number">579</span><span id="L580" data-testid="line-number">580</span><span id="L581" data-testid="line-number">581</span><span id="L582" data-testid="line-number">582</span><span id="L583" data-testid="line-number">583</span><span id="L584" data-testid="line-number">584</span><span id="L585" data-testid="line-number">585</span><span id="L586" data-testid="line-number">586</span><span id="L587" data-testid="line-number">587</span><span id="L588" data-testid="line-number">588</span><span id="L589" data-testid="line-number">589</span><span id="L590" data-testid="line-number">590</span><span id="L591" data-testid="line-number">591</span><span id="L592" data-testid="line-number">592</span><span id="L593" data-testid="line-number">593</span><span id="L594" data-testid="line-number">594</span><span id="L595" data-testid="line-number">595</span><span id="L596" data-testid="line-number">596</span><span id="L597" data-testid="line-number">597</span><span id="L598" data-testid="line-number">598</span><span id="L599" data-testid="line-number">599</span><span id="L600" data-testid="line-number">600</span><span id="L601" data-testid="line-number">601</span><span id="L602" data-testid="line-number">602</span><span id="L603" data-testid="line-number">603</span><span id="L604" data-testid="line-number">604</span><span id="L605" data-testid="line-number">605</span><span id="L606" data-testid="line-number">606</span><span id="L607" data-testid="line-number">607</span><span id="L608" data-testid="line-number">608</span><span id="L609" data-testid="line-number">609</span><span id="L610" data-testid="line-number">610</span><span id="L611" data-testid="line-number">611</span><span id="L612" data-testid="line-number">612</span><span id="L613" data-testid="line-number">613</span><span id="L614" data-testid="line-number">614</span><span id="L615" data-testid="line-number">615</span><span id="L616" data-testid="line-number">616</span><span id="L617" data-testid="line-number">617</span><span id="L618" data-testid="line-number">618</span><span id="L619" data-testid="line-number">619</span><span id="L620" data-testid="line-number">620</span><span id="L621" data-testid="line-number">621</span><span id="L622" data-testid="line-number">622</span><span id="L623" data-testid="line-number">623</span><span id="L624" data-testid="line-number">624</span><span id="L625" data-testid="line-number">625</span><span id="L626" data-testid="line-number">626</span><span id="L627" data-testid="line-number">627</span><span id="L628" data-testid="line-number">628</span><span id="L629" data-testid="line-number">629</span><span id="L630" data-testid="line-number">630</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">    if(_y[j]&lt;0)i+=_u[k+1];
  }
  *_nc=_u[k]+_u[k+1];
  return i;
}

#ifdef CUSTOM_MODES
void get_required_bits(opus_int16 *_bits,int _n,int _maxk,int _frac){
  int k;
  /*_maxk==0 =&gt; there's nothing to do.*/
  celt_assert(_maxk&gt;0);
  _bits[0]=0;
  if (_n==1)
  {
    for (k=1;k&lt;=_maxk;k++)
      _bits[k] = 1&lt;&lt;_frac;
  }
  else {
    VARDECL(opus_uint32,u);
    SAVE_STACK;
    ALLOC(u,_maxk+2U,opus_uint32);
    ncwrs_urow(_n,_maxk,u);
    for(k=1;k&lt;=_maxk;k++)
      _bits[k]=log2_frac(u[k]+u[k+1],_frac);
    RESTORE_STACK;
  }
}
#endif /* CUSTOM_MODES */

void encode_pulses(const int *_y,int _n,int _k,ec_enc *_enc){
  opus_uint32 i;
  celt_assert(_k&gt;0);
#ifndef SMALL_FOOTPRINT
  switch(_n){
    case 2:{
      i=icwrs2(_y,&amp;_k);
      ec_enc_uint(_enc,i,ncwrs2(_k));
    }break;
    case 3:{
      i=icwrs3(_y,&amp;_k);
      ec_enc_uint(_enc,i,ncwrs3(_k));
    }break;
    case 4:{
      i=icwrs4(_y,&amp;_k);
      ec_enc_uint(_enc,i,ncwrs4(_k));
    }break;
     default:
    {
#endif
      VARDECL(opus_uint32,u);
      opus_uint32 nc;
      SAVE_STACK;
      ALLOC(u,_k+2U,opus_uint32);
      i=icwrs(_n,_k,&amp;nc,_y,u);
      ec_enc_uint(_enc,i,nc);
      RESTORE_STACK;
#ifndef SMALL_FOOTPRINT
    }
    break;
  }
#endif
}

void decode_pulses(int *_y,int _n,int _k,ec_dec *_dec)
{
  celt_assert(_k&gt;0);
#ifndef SMALL_FOOTPRINT
   switch(_n){
    case 2:cwrsi2(_k,ec_dec_uint(_dec,ncwrs2(_k)),_y);break;
    case 3:cwrsi3(_k,ec_dec_uint(_dec,ncwrs3(_k)),_y);break;</div></div></div><div><div class="gl-display-flex gl-text-transparent"><div class="gl-display-flex gl-flex-direction-column content-visibility-auto"><span id="L631" data-testid="line-number">631</span><span id="L632" data-testid="line-number">632</span><span id="L633" data-testid="line-number">633</span><span id="L634" data-testid="line-number">634</span><span id="L635" data-testid="line-number">635</span><span id="L636" data-testid="line-number">636</span><span id="L637" data-testid="line-number">637</span><span id="L638" data-testid="line-number">638</span><span id="L639" data-testid="line-number">639</span><span id="L640" data-testid="line-number">640</span><span id="L641" data-testid="line-number">641</span><span id="L642" data-testid="line-number">642</span><span id="L643" data-testid="line-number">643</span><span id="L644" data-testid="line-number">644</span><span id="L645" data-testid="line-number">645</span><span id="L646" data-testid="line-number">646</span></div> <div data-testid="content" class="gl-white-space-pre-wrap!">    case 4:cwrsi4(_k,ec_dec_uint(_dec,ncwrs4(_k)),_y);break;
    default:
    {
#endif
      VARDECL(opus_uint32,u);
      SAVE_STACK;
      ALLOC(u,_k+2U,opus_uint32);
      cwrsi(_n,_k,ec_dec_uint(_dec,ncwrs_urow(_n,_k,u)),_y,u);
      RESTORE_STACK;
#ifndef SMALL_FOOTPRINT
    }
    break;
  }
#endif
}
</div></div></div></div> <!----></div></div>
</div>

</div>

<script>
//&lt;![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/xnorpx/opus/edit/5a6912d46449cb77e799f6c18f31b3108c5b3780/-/celt/cwrs.c'


//]]&gt;
</script>

</main>
</div>


</div>
</div>
<div class="top-nav-responsive layout-page content-wrapper-margin">
<div class="cloak-startup">
<div><div data-testid="mobile-overlay" class="mobile-overlay"></div> <div><div class="gl-h-full gl-w-full"><div><header class="gl-display-flex gl-align-items-center gl-py-4 gl-pl-4"><h1 class="gl-m-0 gl-font-size-h2 gl-reset-color gl-mr-auto">Menu</h1> <a aria-label="Search" data-qa-selector="menu_item_link" data-qa-title="Search" href="/search?project_id=116" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-ml-3 btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="search-icon" role="img" aria-hidden="true" class="gl-icon s16"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#search"/></svg> <!----></span></span></a> <!----></header> <div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column gl-h-full"><div data-testid="menu-section" class=""><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block">
        Explore
      </strong><a aria-label="Projects" data-qa-selector="menu_item_link" data-qa-title="Projects" href="/explore" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="project-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#project"/></svg> 
      Projects
      <!----></span></span></a><a aria-label="Groups" data-qa-selector="menu_item_link" data-qa-title="Groups" href="/explore/groups" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="group-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#group"/></svg> 
      Groups
      <!----></span></span></a><a aria-label="Snippets" data-qa-selector="menu_item_link" data-qa-title="Snippets" href="/explore/snippets" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg xmlns="http://www.w3.org/2000/svg" data-testid="snippet-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-02e23cfb3d83e7293d7b4d2b457f8cd4cb75d3c78cfbedc946bf90bf97c2ed73.svg#snippet"/></svg> 
      Snippets
      <!----></span></span></a></div></div></div></div></div></div>
</div>
</div>



<script>
//&lt;![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img =&gt; {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') &gt; -1 &amp;&amp; imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded');
    img.dataset.qa_selector = 'js_lazy_loaded_content';
  });
}

//]]&gt;
</script>
<script>
//&lt;![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]&gt;
</script>




<div></div><div></div></body></html>