<html class="" lang="en"><head prefix="og: http://ogp.me/ns#">
<meta charset="utf-8">
<title>Source/cmAddLibraryCommand.cxx · v3.21.1 · CMake / CMake · GitLab</title>
<link rel="preload" href="/assets/application_utilities-08432cf9120e4223aaf60df81aa67b3a688203198905c5ee86fc3c7e2133dd8b.css" as="style" type="text/css">
<link rel="preload" href="/assets/application-b1bf30dd8b5a69c9d3a8daa3c88da77db3707a1e61063616e599f10b3a23547e.css" as="style" type="text/css">
<link rel="preload" href="/assets/highlight/themes/white-557ba28a0d83a177dd5f4cdaa59e208f666e026683c63c59f494ece39cb34f98.css" as="style" type="text/css">

<meta content="IE=edge" http-equiv="X-UA-Compatible">
<script>
//<![CDATA[
var gl = window.gl || {};
gl.startup_calls = null;
gl.startup_graphql_calls = [{"query":"query getBlobInfo(\n  $projectPath: ID!\n  $filePath: String!\n  $ref: String!\n  $shouldFetchRawText: Boolean!\n) {\n  project(fullPath: $projectPath) {\n    __typename\n    id\n    repository {\n      __typename\n      empty\n      blobs(paths: [$filePath], ref: $ref) {\n        __typename\n        nodes {\n          __typename\n          id\n          webPath\n          name\n          size\n          rawSize\n          rawTextBlob @include(if: $shouldFetchRawText)\n          fileType\n          language\n          path\n          blamePath\n          editBlobPath\n          gitpodBlobUrl\n          ideEditPath\n          forkAndEditPath\n          ideForkAndEditPath\n          codeNavigationPath\n          projectBlobPathRoot\n          forkAndViewPath\n          environmentFormattedExternalUrl\n          environmentExternalUrlForRouteMap\n          canModifyBlob\n          canCurrentUserPushToBranch\n          archived\n          storedExternally\n          externalStorage\n          externalStorageUrl\n          rawPath\n          replacePath\n          pipelineEditorPath\n          simpleViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n          richViewer {\n            fileType\n            tooLarge\n            type\n            renderError\n          }\n        }\n      }\n    }\n  }\n}\n","variables":{"projectPath":"cmake/cmake","ref":"v3.21.1","filePath":"Source/cmAddLibraryCommand.cxx","shouldFetchRawText":true}}];

if (gl.startup_calls && window.fetch) {
  Object.keys(gl.startup_calls).forEach(apiCall => {
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
if (gl.startup_graphql_calls && window.fetch) {
  const headers = {"X-CSRF-Token":"ijVTfoyYja4+Lrou3lpx2CNbJAI0dHYejp2wvLa+rraBl/sNXrT6CyjoXROpprZZR3n6Cj3T70IN3Cua6fpkXw==","x-gitlab-feature-category":"source_code_management"};
  const url = `https://gitlab.kitware.com/api/graphql`

  const opts = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...headers,
    }
  };

  gl.startup_graphql_calls = gl.startup_graphql_calls.map(call => ({
    ...call,
    fetchCall: fetch(url, {
      ...opts,
      credentials: 'same-origin',
      body: JSON.stringify(call)
    })
  }))
}


//]]>
</script>
<link rel="prefetch" href="/assets/webpack/monaco.04ffd3e0.chunk.js">
<link rel="shortcut icon" type="image/png" href="/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" id="favicon" data-original-href="/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png">
<style>
@keyframes blinking-dot{0%{opacity:1}25%{opacity:0.4}75%{opacity:0.4}100%{opacity:1}}@keyframes blinking-scroll-button{0%{opacity:0.2}50%{opacity:1}100%{opacity:0.2}}@keyframes gl-spinner-rotate{0%{transform:rotate(0)}100%{transform:rotate(360deg)}}body.ui-indigo{--gl-theme-accent: #6666c4}body.ui-indigo .navbar-gitlab{background-color:#292961}body.ui-indigo .navbar-gitlab .navbar-collapse{color:#d1d1f0}body.ui-indigo .navbar-gitlab .container-fluid .navbar-toggler{border-left:1px solid #6868b9;color:#d1d1f0}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>a:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>a:focus,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>button:hover,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li>button:focus,body.ui-indigo .navbar-gitlab .navbar-nav>li>a:hover,body.ui-indigo .navbar-gitlab .navbar-nav>li>a:focus,body.ui-indigo .navbar-gitlab .navbar-nav>li>button:hover,body.ui-indigo .navbar-gitlab .navbar-nav>li>button:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.active>a,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.active>button,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.dropdown.show>a,body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.dropdown.show>button,body.ui-indigo .navbar-gitlab .navbar-nav>li.active>a,body.ui-indigo .navbar-gitlab .navbar-nav>li.active>button,body.ui-indigo .navbar-gitlab .navbar-nav>li.dropdown.show>a,body.ui-indigo .navbar-gitlab .navbar-nav>li.dropdown.show>button{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .navbar-sub-nav>li.line-separator,body.ui-indigo .navbar-gitlab .navbar-nav>li.line-separator{border-left:1px solid rgba(209,209,240,0.2)}body.ui-indigo .navbar-gitlab .navbar-sub-nav{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li{color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li.header-search-new{color:#303030}body.ui-indigo .navbar-gitlab .nav>li>a .notification-dot{border:2px solid #292961}body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle .notification-dot{background-color:#d1d1f0}body.ui-indigo .navbar-gitlab .nav>li>a.header-user-dropdown-toggle .header-user-avatar{border-color:#d1d1f0}@media (min-width: 576px){body.ui-indigo .navbar-gitlab .nav>li>a:hover,body.ui-indigo .navbar-gitlab .nav>li>a:focus{background-color:rgba(209,209,240,0.2)}}body.ui-indigo .navbar-gitlab .nav>li>a:hover svg,body.ui-indigo .navbar-gitlab .nav>li>a:focus svg{fill:currentColor}body.ui-indigo .navbar-gitlab .nav>li>a:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav>li>a:focus .notification-dot{will-change:border-color, background-color;border-color:#4a4a82}body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle:hover .notification-dot,body.ui-indigo .navbar-gitlab .nav>li>a.header-help-dropdown-toggle:focus .notification-dot{background-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a{color:#292961;background-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a:hover svg,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a:hover svg{fill:#292961}body.ui-indigo .navbar-gitlab .nav>li.active>a .notification-dot,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a .notification-dot{border-color:#fff}body.ui-indigo .navbar-gitlab .nav>li.active>a.header-help-dropdown-toggle .notification-dot,body.ui-indigo .navbar-gitlab .nav>li.dropdown.show>a.header-help-dropdown-toggle .notification-dot{background-color:#292961}body.ui-indigo .navbar-gitlab .nav>li .impersonated-user svg,body.ui-indigo .navbar-gitlab .nav>li .impersonated-user:hover svg{fill:#292961}body.ui-indigo .navbar .title>a:hover,body.ui-indigo .navbar .title>a:focus{background-color:rgba(209,209,240,0.2)}body.ui-indigo .header-search{background-color:rgba(209,209,240,0.2) !important;border-radius:4px}body.ui-indigo .header-search:hover{background-color:rgba(209,209,240,0.3) !important}body.ui-indigo .header-search svg.gl-search-box-by-type-search-icon{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input{background-color:transparent;color:rgba(209,209,240,0.8);box-shadow:inset 0 0 0 1px rgba(209,209,240,0.4)}body.ui-indigo .header-search input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .header-search input:focus::placeholder,body.ui-indigo .header-search input:active::placeholder{color:#868686}body.ui-indigo .header-search .keyboard-shortcut-helper{color:#d1d1f0;background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form{background-color:rgba(209,209,240,0.2)}body.ui-indigo .search form:hover{background-color:rgba(209,209,240,0.3)}body.ui-indigo .search .search-input::placeholder{color:rgba(209,209,240,0.8)}body.ui-indigo .search .search-input-wrap .search-icon,body.ui-indigo .search .search-input-wrap .clear-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .search.search-active form{background-color:#fff}body.ui-indigo .search.search-active .search-input-wrap .search-icon{fill:rgba(209,209,240,0.8)}body.ui-indigo .nav-sidebar li.active>a{color:#303030}body.ui-indigo .nav-sidebar .fly-out-top-item a,body.ui-indigo .nav-sidebar .fly-out-top-item a:hover,body.ui-indigo .nav-sidebar .fly-out-top-item.active a,body.ui-indigo .nav-sidebar .fly-out-top-item .fly-out-top-item-container{background-color:var(--gray-100, #f0f0f0);color:var(--gray-900, #303030)}body.ui-indigo .branch-header-title{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active{color:#4b4ba3}body.ui-indigo .ide-sidebar-link.active.is-right{box-shadow:inset -3px 0 #4b4ba3}

*,*::before,*::after{box-sizing:border-box}html{font-family:sans-serif;line-height:1.15}aside,header{display:block}body{margin:0;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:1rem;font-weight:400;line-height:1.5;color:#303030;text-align:left;background-color:#fff}ul{margin-top:0;margin-bottom:1rem}ul ul{margin-bottom:0}strong{font-weight:bolder}a{color:#1f75cb;text-decoration:none;background-color:transparent}a:not([href]):not([class]){color:inherit;text-decoration:none}kbd{font-family:"Menlo", "DejaVu Sans Mono", "Liberation Mono", "Consolas", "Ubuntu Mono", "Courier New", "andale mono", "lucida console", monospace;font-size:1em}img{vertical-align:middle;border-style:none}svg{overflow:hidden;vertical-align:middle}button{border-radius:0}input,button{margin:0;font-family:inherit;font-size:inherit;line-height:inherit}button,input{overflow:visible}button{text-transform:none}[role="button"]{cursor:pointer}button:not(:disabled),[type="button"]:not(:disabled){cursor:pointer}button::-moz-focus-inner,[type="button"]::-moz-focus-inner{padding:0;border-style:none}[type="search"]{outline-offset:-2px}.list-unstyled{padding-left:0;list-style:none}kbd{padding:0.2rem 0.4rem;font-size:90%;color:#fff;background-color:#303030;border-radius:0.2rem}kbd kbd{padding:0;font-size:100%;font-weight:600}.container-fluid{width:100%;padding-right:15px;padding-left:15px;margin-right:auto;margin-left:auto}.form-control{display:block;width:100%;height:34px;padding:0.375rem 0.75rem;font-size:0.875rem;font-weight:400;line-height:1.5;color:#303030;background-color:#fff;background-clip:padding-box;border:1px solid #868686;border-radius:0.25rem}.form-control:-moz-focusring{color:transparent;text-shadow:0 0 0 #303030}.form-control::placeholder{color:#5e5e5e;opacity:1}.form-control:disabled{background-color:#fafafa;opacity:1}.form-inline{display:flex;flex-flow:row wrap;align-items:center}@media (min-width: 576px){.form-inline .form-control{display:inline-block;width:auto;vertical-align:middle}}.btn{display:inline-block;font-weight:400;color:#303030;text-align:center;vertical-align:middle;-webkit-user-select:none;user-select:none;background-color:transparent;border:1px solid transparent;padding:0.375rem 0.75rem;font-size:1rem;line-height:20px;border-radius:0.25rem}.btn:disabled{opacity:0.65}.btn:not(:disabled):not(.disabled){cursor:pointer}.collapse:not(.show){display:none}.dropdown{position:relative}.dropdown-menu{position:absolute;top:100%;left:0;z-index:1000;display:none;float:left;min-width:10rem;padding:0.5rem 0;margin:0.125rem 0 0;font-size:1rem;color:#303030;text-align:left;list-style:none;background-color:#fff;background-clip:padding-box;border:1px solid rgba(0,0,0,0.15);border-radius:0.25rem}.nav{display:flex;flex-wrap:wrap;padding-left:0;margin-bottom:0;list-style:none}.navbar{position:relative;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;padding:0.25rem 0.5rem}.navbar .container-fluid{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between}.navbar-nav{display:flex;flex-direction:column;padding-left:0;margin-bottom:0;list-style:none}.navbar-nav .dropdown-menu{position:static;float:none}.navbar-collapse{flex-basis:100%;flex-grow:1;align-items:center}.navbar-toggler{padding:0.25rem 0.75rem;font-size:1.25rem;line-height:1;background-color:transparent;border:1px solid transparent;border-radius:0.25rem}@media (max-width: 575.98px){.navbar-expand-sm>.container-fluid{padding-right:0;padding-left:0}}@media (min-width: 576px){.navbar-expand-sm{flex-flow:row nowrap;justify-content:flex-start}.navbar-expand-sm .navbar-nav{flex-direction:row}.navbar-expand-sm .navbar-nav .dropdown-menu{position:absolute}.navbar-expand-sm>.container-fluid{flex-wrap:nowrap}.navbar-expand-sm .navbar-collapse{display:flex !important;flex-basis:auto}.navbar-expand-sm .navbar-toggler{display:none}}.badge{display:inline-block;padding:0.25em 0.4em;font-size:75%;font-weight:600;line-height:1;text-align:center;white-space:nowrap;vertical-align:baseline;border-radius:0.25rem}.badge:empty{display:none}.btn .badge{position:relative;top:-1px}.badge-pill{padding-right:0.6em;padding-left:0.6em;border-radius:10rem}.badge-success{color:#fff;background-color:#108548}.badge-info{color:#fff;background-color:#1f75cb}.badge-warning{color:#fff;background-color:#ab6100}.rounded-circle{border-radius:50% !important}.d-none{display:none !important}.d-block{display:block !important}@media (min-width: 576px){.d-sm-none{display:none !important}.d-sm-inline-block{display:inline-block !important}}@media (min-width: 768px){.d-md-block{display:block !important}}@media (min-width: 992px){.d-lg-none{display:none !important}}.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0, 0, 0, 0);white-space:nowrap;border:0}.gl-avatar{border-width:1px;border-style:solid;border-color:rgba(0,0,0,0.08);overflow:hidden;flex-shrink:0}.gl-avatar-s24{width:1.5rem;height:1.5rem;font-size:0.75rem;line-height:1rem;border-radius:0.25rem}.gl-avatar-circle{border-radius:50%}.gl-badge{display:inline-flex;align-items:center;font-size:0.75rem;font-weight:400;line-height:1rem;padding-top:0.25rem;padding-bottom:0.25rem;padding-left:0.5rem;padding-right:0.5rem}.gl-badge.sm{padding-top:0;padding-bottom:0}.gl-badge.badge-info{background-color:#cbe2f9;color:#0b5cad}a.gl-badge.badge-info.active,a.gl-badge.badge-info:active{color:#033464;background-color:#9dc7f1}a.gl-badge.badge-info:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-badge.badge-success{background-color:#c3e6cd;color:#24663b}a.gl-badge.badge-success.active,a.gl-badge.badge-success:active{color:#0a4020;background-color:#91d4a8}a.gl-badge.badge-success:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-badge.badge-warning{background-color:#f5d9a8;color:#8f4700}a.gl-badge.badge-warning.active,a.gl-badge.badge-warning:active{color:#5c2900;background-color:#e9be74}a.gl-badge.badge-warning:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.gl-button .gl-badge{top:0}.gl-form-input,.gl-form-input.form-control{background-color:#fff;font-family:-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans", Ubuntu, Cantarell, "Helvetica Neue", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-size:0.875rem;line-height:1rem;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;height:auto;color:#303030;box-shadow:inset 0 0 0 1px #868686;border-style:none;-webkit-appearance:none;appearance:none;-moz-appearance:none}.gl-form-input:disabled,.gl-form-input:not(.form-control-plaintext):not([type="color"]):read-only,.gl-form-input.form-control:disabled,.gl-form-input.form-control:not(.form-control-plaintext):not([type="color"]):read-only{background-color:#f5f5f5;box-shadow:inset 0 0 0 1px #dbdbdb}.gl-form-input:disabled,.gl-form-input.form-control:disabled{cursor:not-allowed;color:#666}.gl-form-input::placeholder,.gl-form-input.form-control::placeholder{color:#868686}.gl-icon{fill:currentColor}.gl-icon.s12{width:12px;height:12px}.gl-icon.s16{width:16px;height:16px}.gl-icon.s32{width:32px;height:32px}.gl-link{font-size:0.875rem;color:#1f75cb}.gl-link:active{color:#0b5cad}.gl-link:active{text-decoration:underline;outline:2px solid #428fdc;outline-offset:2px}.gl-button{display:inline-flex}.gl-button:not(.btn-link):active{text-decoration:none}.gl-button.gl-button{border-width:0;padding-top:0.5rem;padding-bottom:0.5rem;padding-left:0.75rem;padding-right:0.75rem;background-color:transparent;line-height:1rem;color:#303030;fill:currentColor;box-shadow:inset 0 0 0 1px #bfbfbf;justify-content:center;align-items:center;font-size:0.875rem;border-radius:0.25rem}.gl-button.gl-button.btn-default{background-color:#fff}.gl-button.gl-button.btn-default:active,.gl-button.gl-button.btn-default.active{box-shadow:inset 0 0 0 1px #5e5e5e, 0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none;background-color:#dbdbdb}.gl-button.gl-button.btn-default:active .gl-icon,.gl-button.gl-button.btn-default.active .gl-icon{color:#303030}.gl-button.gl-button.btn-default .gl-icon{color:#666}.gl-search-box-by-type-search-icon{margin:0.5rem;color:#666;width:1rem;position:absolute}.gl-search-box-by-type{display:flex;position:relative}.gl-search-box-by-type-input,.gl-search-box-by-type-input.gl-form-input{height:2rem;padding-right:2rem;padding-left:1.75rem}body{font-size:0.875rem}button,html [type="button"],[role="button"]{cursor:pointer}strong{font-weight:bold}svg{vertical-align:baseline}.form-control,.search form{font-size:0.875rem}.hidden{display:none !important;visibility:hidden !important}.hide{display:none}.badge:not(.gl-badge){padding:4px 5px;font-size:12px;font-style:normal;font-weight:400;display:inline-block}.divider{height:0;margin:4px 0;overflow:hidden;border-top:1px solid #dbdbdb}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left{color:#666}html{overflow-y:scroll}.btn{border-radius:4px;font-size:0.875rem;font-weight:400;padding:6px 10px;background-color:#fff;border-color:#dbdbdb;color:#303030;color:#303030;white-space:nowrap}.btn:active{background-color:#f0f0f0;box-shadow:none}.btn:active,.btn.active{background-color:#eaeaea;border-color:#e3e3e3;color:#303030}.btn svg{height:15px;width:15px}.btn svg:not(:last-child){margin-right:5px}.badge.badge-pill:not(.gl-badge){font-weight:400;background-color:rgba(0,0,0,0.07);color:#525252;vertical-align:baseline}.gl-font-sm{font-size:12px}.dropdown{position:relative}.dropdown-menu-toggle:active{box-shadow:0 0 0 1px #fff, 0 0 0 3px #428fdc;outline:none}.search-input-container .dropdown-menu{margin-top:11px}.dropdown-menu-toggle{padding:6px 8px 6px 10px;background-color:#fff;color:#303030;font-size:14px;text-align:left;border:1px solid #dbdbdb;border-radius:0.25rem;white-space:nowrap}.dropdown-menu-toggle.no-outline{outline:0}.dropdown-menu-toggle.dropdown-menu-toggle{justify-content:flex-start;overflow:hidden;padding-right:25px;position:relative;text-overflow:ellipsis;width:160px}.dropdown-menu{display:none;position:absolute;width:auto;top:100%;z-index:300;min-width:240px;max-width:500px;margin-top:4px;margin-bottom:24px;font-size:0.875rem;font-weight:400;padding:8px 0;background-color:#fff;border:1px solid #dbdbdb;border-radius:0.25rem;box-shadow:0 2px 4px rgba(0,0,0,0.1)}.dropdown-menu ul{margin:0;padding:0}.dropdown-menu li{display:block;text-align:left;list-style:none}.dropdown-menu li>a,.dropdown-menu li button{background:transparent;border:0;border-radius:0;box-shadow:none;display:block;font-weight:400;position:relative;padding:8px 12px;color:#303030;line-height:16px;white-space:normal;overflow:hidden;text-align:left;width:100%}.dropdown-menu li>a:active,.dropdown-menu li button:active{background-color:#eee;color:#303030;outline:0;text-decoration:none}.dropdown-menu li>a:active,.dropdown-menu li button:active{box-shadow:inset 0 0 0 2px #428fdc, inset 0 0 0 3px #fff, inset 0 0 0 1px #fff;outline:none}.dropdown-menu .divider{height:1px;margin:0.25rem 0;padding:0;background-color:#dbdbdb}.dropdown-menu .badge.badge-pill+span:not(.badge):not(.badge-pill){margin-right:40px}@media (max-width: 575.98px){.navbar-gitlab li.dropdown{position:static}.navbar-gitlab li.dropdown.user-counter{margin-left:8px !important}.navbar-gitlab li.dropdown.user-counter>a{padding:0 4px !important}header.navbar-gitlab .dropdown .dropdown-menu{width:100%;min-width:100%}}@media (max-width: 767.98px){.dropdown-menu-toggle.dropdown-menu-toggle{width:100%}}input{border-radius:0.25rem;color:#303030;background-color:#fff}.form-control{border-radius:4px;padding:6px 10px}.form-control::placeholder{color:#868686}kbd{display:inline-block;padding:3px 5px;font-size:0.6875rem;line-height:10px;color:var(--gray-700, #525252);vertical-align:middle;background-color:var(--gray-10, #f5f5f5);border-width:1px;border-style:solid;border-color:var(--gray-100, #dbdbdb) var(--gray-100, #dbdbdb) var(--gray-200, #bfbfbf);border-image:none;border-radius:3px;box-shadow:0 -1px 0 var(--gray-200, #bfbfbf) inset}.navbar-gitlab{padding:0 16px;z-index:1000;margin-bottom:0;min-height:var(--header-height, 48px);border:0;position:fixed;top:0;left:0;right:0;border-radius:0}.navbar-gitlab .close-icon{display:none}.navbar-gitlab .header-content{width:100%;display:flex;justify-content:space-between;position:relative;min-height:var(--header-height, 48px);padding-left:0}.navbar-gitlab .header-content .title{padding-right:0;color:currentColor;display:flex;position:relative;margin:0;font-size:18px;vertical-align:top;white-space:nowrap}.navbar-gitlab .header-content .title img{height:24px}.navbar-gitlab .header-content .title a:not(.canary-badge){display:flex;align-items:center;padding:2px 8px;margin:4px 2px 4px -8px;border-radius:4px}.navbar-gitlab .header-content .title a:not(.canary-badge):active{box-shadow:0 0 0 1px rgba(0,0,0,0.6),0 0 0 3px #63a6e9;outline:none}.navbar-gitlab .header-content .navbar-collapse>ul.nav>li:not(.d-none){margin:0 2px}.navbar-gitlab .navbar-collapse{flex:0 0 auto;border-top:0;padding:0}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse{flex:1 1 auto}}.navbar-gitlab .navbar-collapse .nav{flex-wrap:nowrap}@media (max-width: 575.98px){.navbar-gitlab .navbar-collapse .nav>li:not(.d-none) a{margin-left:0}}.navbar-gitlab .container-fluid{padding:0}.navbar-gitlab .container-fluid .user-counter svg{margin-right:3px}.navbar-gitlab .container-fluid .navbar-toggler{position:relative;right:-10px;border-radius:0;min-width:45px;padding:0;margin:8px 8px 8px 0;font-size:14px;text-align:center;color:currentColor}.navbar-gitlab .container-fluid .navbar-toggler.active{color:currentColor;background-color:transparent}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .navbar-nav{display:flex;padding-right:10px;flex-direction:row}}.navbar-gitlab .container-fluid .navbar-nav li .badge.badge-pill:not(.gl-badge){box-shadow:none;font-weight:600}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav>li.header-user{padding-left:10px}}.navbar-gitlab .container-fluid .nav>li>a{will-change:color;margin:4px 0;padding:6px 8px;height:32px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid .nav>li>a{padding:0}}.navbar-gitlab .container-fluid .nav>li>a.header-user-dropdown-toggle{margin-left:2px}.navbar-gitlab .container-fluid .nav>li>a.header-user-dropdown-toggle .header-user-avatar{margin-right:0}.navbar-gitlab .container-fluid .nav>li .header-new-dropdown-toggle{margin-right:0}.navbar-sub-nav>li>a,.navbar-sub-nav>li>button,.navbar-nav>li>a,.navbar-nav>li>button{display:flex;align-items:center;justify-content:center;padding:6px 8px;margin:4px 2px;font-size:12px;color:currentColor;border-radius:4px;height:32px;font-weight:600}.navbar-sub-nav>li>a:active,.navbar-sub-nav>li>button:active,.navbar-nav>li>a:active,.navbar-nav>li>button:active{box-shadow:0 0 0 1px rgba(0,0,0,0.6),0 0 0 3px #63a6e9;outline:none}.navbar-sub-nav>li .top-nav-toggle,.navbar-sub-nav>li>button,.navbar-nav>li .top-nav-toggle,.navbar-nav>li>button{background:transparent;border:0}.navbar-sub-nav .dropdown-menu,.navbar-nav .dropdown-menu{position:absolute}.navbar-sub-nav{display:flex;align-items:center;height:100%;margin:0 0 0 6px}.caret-down,.btn .caret-down{top:0;height:11px;width:11px;margin-left:4px;fill:currentColor}.header-user .dropdown-menu,.header-new .dropdown-menu{margin-top:4px}.btn-sign-in{background-color:#ebebfa;color:#292961;font-weight:600;line-height:18px;margin:4px 0 4px 2px}@media (max-width: 575.98px){.navbar-gitlab .container-fluid{font-size:18px}.navbar-gitlab .container-fluid .navbar-nav{table-layout:fixed;width:100%;margin:0;text-align:right}.navbar-gitlab .container-fluid .navbar-collapse{margin-left:-8px;margin-right:-10px}.navbar-gitlab .container-fluid .navbar-collapse .nav>li:not(.d-none){flex:1}.header-user-dropdown-toggle{text-align:center}.header-user-avatar{float:none}}.header-user-avatar{float:left;margin-right:5px;border-radius:50%;border:1px solid #f5f5f5}.notification-dot{background-color:#d99530;height:12px;width:12px;pointer-events:none;visibility:hidden;top:3px}.tanuki-logo .tanuki{fill:#e24329}.tanuki-logo .left-cheek,.tanuki-logo .right-cheek{fill:#fc6d26}.tanuki-logo .chin{fill:#fca326}.context-header{position:relative;margin-right:2px;width:256px}.context-header>a,.context-header>button{font-weight:600;display:flex;width:100%;align-items:center;padding:10px 16px 10px 10px;color:#303030;background-color:transparent;border:0;text-align:left}.context-header .avatar-container{flex:0 0 32px;background-color:#fff}.context-header .sidebar-context-title{overflow:hidden;text-overflow:ellipsis;color:#303030}@media (min-width: 768px){.page-with-contextual-sidebar{padding-left:56px}}@media (min-width: 1200px){.page-with-contextual-sidebar{padding-left:256px}}@media (min-width: 768px){.page-with-icon-sidebar{padding-left:56px}}.nav-sidebar{position:fixed;bottom:0;left:0;z-index:600;width:256px;top:var(--header-height, 48px);background-color:#f5f5f5;border-right:1px solid #e9e9e9;transform:translate3d(0, 0, 0)}.nav-sidebar.sidebar-collapsed-desktop{width:56px}.nav-sidebar.sidebar-collapsed-desktop .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar.sidebar-collapsed-desktop .badge.badge-pill:not(.fly-out-badge),.nav-sidebar.sidebar-collapsed-desktop .nav-item-name,.nav-sidebar.sidebar-collapsed-desktop .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar.sidebar-collapsed-desktop .sidebar-top-level-items>li>a{min-height:unset}.nav-sidebar.sidebar-collapsed-desktop .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar.sidebar-collapsed-desktop .avatar-container{margin:0 auto}.nav-sidebar.sidebar-collapsed-desktop li.active:not(.fly-out-top-item)>a{background-color:rgba(41,41,97,0.08)}.nav-sidebar a{text-decoration:none;color:#303030}.nav-sidebar li{white-space:nowrap}.nav-sidebar li .nav-item-name{flex:1;overflow:hidden;text-overflow:ellipsis}.nav-sidebar li>a,.nav-sidebar li>.fly-out-top-item-container{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 8px}.nav-sidebar li.active>a{font-weight:600}.nav-sidebar li.active:not(.fly-out-top-item)>a:not(.has-sub-items){background-color:rgba(0,0,0,0.08)}.nav-sidebar ul{padding-left:0;list-style:none}@media (max-width: 767.98px){.nav-sidebar{left:-256px}}.nav-sidebar .nav-icon-container{display:flex;margin-right:8px}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:-0.25rem;margin-bottom:-0.25rem;margin-top:0;position:relative;color:#fff;background:var(--black, #000)}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a strong,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container strong{font-weight:400}.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item.active a::before,.nav-sidebar a:not(.has-sub-items)+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container::before{position:absolute;content:"";display:block;top:50%;left:-0.25rem;margin-top:-0.25rem;width:0;height:0;border-top:0.25rem solid transparent;border-bottom:0.25rem solid transparent;border-right:0.25rem solid #000;border-right-color:var(--black, #000)}@media (min-width: 576px){.nav-sidebar a.has-sub-items+.sidebar-sub-level-items{min-width:150px}}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item{display:none}.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item.active a,.nav-sidebar a.has-sub-items+.sidebar-sub-level-items .fly-out-top-item .fly-out-top-item-container{margin-left:0;margin-right:0;padding-left:1rem;padding-right:1rem;cursor:default;pointer-events:none;font-size:0.75rem;margin-top:0;border-bottom-left-radius:0;border-bottom-right-radius:0}@media (min-width: 768px) and (max-width: 1199px){.nav-sidebar:not(.sidebar-expanded-mobile){width:56px}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-sidebar-inner-scroll{overflow-x:hidden}.nav-sidebar:not(.sidebar-expanded-mobile) .badge.badge-pill:not(.fly-out-badge),.nav-sidebar:not(.sidebar-expanded-mobile) .nav-item-name,.nav-sidebar:not(.sidebar-expanded-mobile) .collapse-text{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items>li>a{min-height:unset}.nav-sidebar:not(.sidebar-expanded-mobile) .fly-out-top-item:not(.divider){display:block !important}.nav-sidebar:not(.sidebar-expanded-mobile) .avatar-container{margin:0 auto}.nav-sidebar:not(.sidebar-expanded-mobile) li.active:not(.fly-out-top-item)>a{background-color:rgba(41,41,97,0.08)}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:60px;width:56px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:10px 4px}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header{height:auto}.nav-sidebar:not(.sidebar-expanded-mobile) .context-header a{padding:0.25rem}.nav-sidebar:not(.sidebar-expanded-mobile) .sidebar-top-level-items>li .sidebar-sub-level-items:not(.flyout-list){display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .nav-icon-container{margin-right:0}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button{width:55px;padding:0 21px}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .collapse-text{display:none}.nav-sidebar:not(.sidebar-expanded-mobile) .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}}.nav-sidebar-inner-scroll{height:100%;width:100%;overflow-x:hidden;overflow-y:auto}.nav-sidebar-inner-scroll>div.context-header{margin-top:0.25rem}.nav-sidebar-inner-scroll>div.context-header a{padding-left:0.75rem;padding-right:0.75rem;padding-top:0.5rem;padding-bottom:0.5rem;display:flex;align-items:center;border-radius:0.25rem;width:auto;line-height:1rem;margin:1px 8px;padding:0.25rem;margin-bottom:0.25rem;margin-top:0.125rem}.nav-sidebar-inner-scroll>div.context-header a .avatar-container{font-weight:400;flex:none}.sidebar-top-level-items{margin-bottom:60px}.sidebar-top-level-items .context-header a{padding:0.25rem;margin-bottom:0.25rem;margin-top:0.125rem}.sidebar-top-level-items .context-header a .avatar-container{font-weight:400;flex:none}.sidebar-top-level-items>li.active .sidebar-sub-level-items:not(.is-fly-out-only){display:block}.sidebar-top-level-items li>a.gl-link{color:#303030}.sidebar-top-level-items li>a.gl-link:active{text-decoration:none}.sidebar-sub-level-items{padding-top:0;padding-bottom:0;display:none}.sidebar-sub-level-items:not(.fly-out-list) li>a{padding-left:2.25rem}.toggle-sidebar-button,.close-nav-button{height:48px;padding:0 16px;background-color:#fafafa;border:0;color:#666;display:flex;align-items:center;background-color:#f5f5f5;position:fixed;bottom:0;width:255px}.toggle-sidebar-button .collapse-text,.toggle-sidebar-button .icon-chevron-double-lg-left,.close-nav-button .collapse-text,.close-nav-button .icon-chevron-double-lg-left{color:inherit}.collapse-text{white-space:nowrap;overflow:hidden}.sidebar-collapsed-desktop .context-header{height:60px;width:56px}.sidebar-collapsed-desktop .context-header a{padding:10px 4px}.sidebar-collapsed-desktop .sidebar-context-title{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.sidebar-collapsed-desktop .context-header{height:auto}.sidebar-collapsed-desktop .context-header a{padding:0.25rem}.sidebar-collapsed-desktop .sidebar-top-level-items>li .sidebar-sub-level-items:not(.flyout-list){display:none}.sidebar-collapsed-desktop .nav-icon-container{margin-right:0}.sidebar-collapsed-desktop .toggle-sidebar-button{width:55px;padding:0 21px}.sidebar-collapsed-desktop .toggle-sidebar-button .collapse-text{display:none}.sidebar-collapsed-desktop .toggle-sidebar-button .icon-chevron-double-lg-left{transform:rotate(180deg);margin:0}.close-nav-button{display:none}@media (max-width: 767.98px){.close-nav-button{display:flex}.toggle-sidebar-button{display:none}}input::-moz-placeholder{color:#868686;opacity:1}input::-ms-input-placeholder{color:#868686}input:-ms-input-placeholder{color:#868686}svg{fill:currentColor}svg.s12{width:12px;height:12px}svg.s16{width:16px;height:16px}svg.s32{width:32px;height:32px}svg.s12{vertical-align:-1px}svg.s16{vertical-align:-3px}.header-content .header-search-new{max-width:640px}.header-search{min-width:320px}@media (min-width: 768px) and (max-width: 1199.98px){.header-search{min-width:200px}}.header-search .keyboard-shortcut-helper{transform:translateY(calc(50% - 2px));box-shadow:none;border-color:transparent}.search{margin:0 8px}.search form{display:block;margin:0;padding:4px;width:200px;line-height:24px;height:32px;border:0;border-radius:4px}@media (min-width: 1200px){.search form{width:320px}}.search .search-input{border:0;font-size:14px;padding:0 20px 0 0;margin-left:5px;line-height:25px;width:98%;color:#fff;background:none}.search .search-input-container{display:flex;position:relative}.search .search-input-wrap{width:100%}.search .search-input-wrap .search-icon,.search .search-input-wrap .clear-icon{position:absolute;right:5px;top:4px}.search .search-input-wrap .search-icon{-webkit-user-select:none;user-select:none}.search .search-input-wrap .clear-icon{display:none}.search .search-input-wrap .dropdown{position:static}.search .search-input-wrap .dropdown-menu{left:-5px;max-height:400px;overflow:auto}@media (min-width: 1200px){.search .search-input-wrap .dropdown-menu{width:320px}}.search .identicon{flex-basis:16px;flex-shrink:0;margin-right:4px}.avatar,.avatar-container{float:left;margin-right:16px;border-radius:50%}.avatar.s16,.avatar-container.s16{width:16px;height:16px;margin-right:8px}.avatar.s32,.avatar-container.s32{width:32px;height:32px;margin-right:8px}.avatar{transition-property:none;width:40px;height:40px;padding:0;background:#fdfdfd;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(31,31,31,0.1)}.avatar.avatar-tile{border-radius:0;border:0}.identicon{text-align:center;vertical-align:top;color:#303030;background-color:#f0f0f0}.identicon.s16{font-size:10px;line-height:16px}.identicon.s32{font-size:14px;line-height:32px}.identicon.bg1{background-color:#fcf1ef}.identicon.bg2{background-color:#f4f0ff}.identicon.bg3{background-color:#f1f1ff}.identicon.bg4{background-color:#e9f3fc}.identicon.bg5{background-color:#ecf4ee}.identicon.bg6{background-color:#fdf1dd}.identicon.bg7{background-color:#f0f0f0}.avatar-container{overflow:hidden;display:flex}.avatar-container a{width:100%;height:100%;display:flex;text-decoration:none}.avatar-container .avatar{border-radius:0;border:0;height:auto;width:100%;margin:0;align-self:center}.rect-avatar{border-radius:2px}.rect-avatar.s16{border-radius:2px}.rect-avatar.s16 .avatar{border-radius:2px}.rect-avatar.s32{border-radius:4px}.rect-avatar.s32 .avatar{border-radius:4px}.tab-width-8{tab-size:8}.gl-sr-only{border:0;clip:rect(0, 0, 0, 0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;white-space:nowrap;width:1px}.gl-border-none\!{border-style:none !important}.gl-display-none{display:none}.gl-display-flex{display:flex}@media (min-width: 576px){.gl-sm-display-block{display:block}}@media (min-width: 992px){.gl-lg-display-block{display:block}}.gl-display-inline-block\!{display:inline-block !important}.gl-align-items-center{align-items:center}.gl-align-items-stretch{align-items:stretch}.gl-flex-grow-1{flex-grow:1}.gl-justify-content-end{justify-content:flex-end}.gl-relative{position:relative}.gl-absolute{position:absolute}.gl-top-0{top:0}.gl-right-3{right:0.5rem}.gl-w-full{width:100%}.gl-px-3{padding-left:0.5rem;padding-right:0.5rem}.gl-pr-2{padding-right:0.25rem}.gl-pt-0{padding-top:0}.gl-mr-auto{margin-right:auto}.gl-mr-3{margin-right:0.5rem}.gl-ml-n2{margin-left:-0.25rem}.gl-ml-3{margin-left:0.5rem}.gl-mx-0\!{margin-left:0 !important;margin-right:0 !important}.gl-text-right{text-align:right}.gl-white-space-nowrap{white-space:nowrap}.gl-font-sm{font-size:0.75rem}.gl-font-weight-bold{font-weight:600}.gl-z-index-1{z-index:1}.cloak-startup,.content-wrapper>.alert-wrapper,#content-body,.modal-dialog{display:none}

</style>


<link rel="stylesheet" media="all" href="/assets/application-b1bf30dd8b5a69c9d3a8daa3c88da77db3707a1e61063616e599f10b3a23547e.css" data-startupcss="loaded">
<link rel="stylesheet" media="all" href="/assets/page_bundles/tree-32d554a904034ce1522164c6cde7f4a819d1fd1bd6a4a91dd4aa9fb5c906e09b.css" data-startupcss="loaded">
<link rel="stylesheet" media="all" href="/assets/application_utilities-08432cf9120e4223aaf60df81aa67b3a688203198905c5ee86fc3c7e2133dd8b.css" data-startupcss="loaded">


<link rel="stylesheet" media="all" href="/assets/highlight/themes/white-557ba28a0d83a177dd5f4cdaa59e208f666e026683c63c59f494ece39cb34f98.css" data-startupcss="loaded">
<script>
//<![CDATA[
document.querySelectorAll('link[media="print"]').forEach(linkTag => {
  linkTag.setAttribute('data-startupcss', 'loading');
  const startupLinkLoadedEvent = new CustomEvent('CSSStartupLinkLoaded');
  linkTag.addEventListener('load',function(){this.media='all';this.setAttribute('data-startupcss', 'loaded');document.dispatchEvent(startupLinkLoadedEvent);},{once: true});
})

//]]>
</script>

<script>
//<![CDATA[
window.gon={};gon.api_version="v4";gon.default_avatar_url="https://gitlab.kitware.com/assets/no_avatar-849f9c04a3a0d0cea2424ae97b27447dc64a7dbfae83c036c45b403392f0e8ba.png";gon.max_file_size=10;gon.asset_host=null;gon.webpack_public_path="/assets/webpack/";gon.relative_url_root="";gon.user_color_scheme="white";gon.markdown_surround_selection=null;gon.markdown_automatic_lists=null;gon.recaptcha_api_server_url="https://www.google.com/recaptcha/api.js";gon.recaptcha_sitekey="6LcWbB0TAAAAAGSoGydnzoJiVZU8WePQoQnQLZNA";gon.gitlab_url="https://gitlab.kitware.com";gon.revision="2165c18956e";gon.feature_category="source_code_management";gon.gitlab_logo="/assets/gitlab_logo-2957169c8ef64c58616a1ac3f4fc626e8a35ce4eb3ed31bb0d873712f2a041a0.png";gon.secure=true;gon.sprite_icons="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg";gon.sprite_file_icons="/assets/file_icons-958d18a1c33aa82a81e2eb1ffbffc33131d501c41ad95838a70b089e5ffbd7a0.svg";gon.emoji_sprites_css_path="/assets/emoji_sprites-e1b1ba2d7a86a445dcb1110d1b6e7dd0200ecaa993a445df77a07537dbf8f475.css";gon.select2_css_path="/assets/lazy_bundles/select2-972cb11866a2afb07749efdf63c646325d6ad61bac72ad794042166dcbecfc81.css";gon.gridstack_css_path="/assets/lazy_bundles/gridstack-f9e005145f1f29d3fd436ec6eda8b264c017ee47886472841ed47e32332518ff.css";gon.test_env=false;gon.disable_animations=null;gon.suggested_label_colors={"#009966":"Green-cyan","#8fbc8f":"Dark sea green","#3cb371":"Medium sea green","#00b140":"Green screen","#013220":"Dark green","#6699cc":"Blue-gray","#0000ff":"Blue","#e6e6fa":"Lavender","#9400d3":"Dark violet","#330066":"Deep violet","#808080":"Gray","#36454f":"Charcoal grey","#f7e7ce":"Champagne","#c21e56":"Rose red","#cc338b":"Magenta-pink","#dc143c":"Crimson","#ff0000":"Red","#cd5b45":"Dark coral","#eee600":"Titanium yellow","#ed9121":"Carrot orange","#c39953":"Aztec Gold"};gon.first_day_of_week=0;gon.time_display_relative=true;gon.ee=false;gon.jh=false;gon.dot_com=false;gon.features={"usageDataApi":true,"securityAutoFix":false,"newHeaderSearch":true,"sourceEditorToolbar":false,"integrationSlackAppNotifications":false,"highlightJs":true,"fileLineBlame":false};
//]]>
</script>





<script src="/assets/webpack/runtime.6f3b887d.bundle.js" defer="defer"></script>
<script src="/assets/webpack/main.22dd5191.chunk.js" defer="defer"></script>
<script src="/assets/webpack/graphql.a062ade3.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-IssuablePopoverBundle-pages.admin.application_settings-pages.admin.application_settings.ci_c-31b97f17.23133b7c.chunk.js" defer="defer"></script>
<script src="/assets/webpack/4.6771e92c.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.boards-pages.groups.details-pages.groups.show-pages.projects-pages.projects.act-3d5f7af1.1d2033e5.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.groups.new-pages.ide-pages.projects-pages.projects.activity-pages.projects.alert_manag-45a4e2db.a0ce58a7.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects-pages.projects.activity-pages.projects.alert_management.details-pages.project-5c8668c1.02698ee8.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-jira_connect_app-pages.admin.application_settings-pages.admin.application_settings.ci_cd-pag-0f601fa8.ea616498.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.edit-pages.projects.sni-dd84f7c7.fb6a9877.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.snippets.show-pages.projects.tre-25c821a4.d5afca47.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blob.show-pages.projects.show-pages.projects.tree.show.c0aa6746.chunk.js" defer="defer"></script>
<script src="/assets/webpack/commons-pages.projects.blame.show-pages.projects.blob.show.88ecfb9b.chunk.js" defer="defer"></script>
<script src="/assets/webpack/pages.projects.blob.show.b91f4f58.chunk.js" defer="defer"></script>

<meta content="object" property="og:type">
<meta content="GitLab" property="og:site_name">
<meta content="Source/cmAddLibraryCommand.cxx · v3.21.1 · CMake / CMake · GitLab" property="og:title">
<meta content="CMake, the cross-platform, open-source build system." property="og:description">
<meta content="https://gitlab.kitware.com/uploads/-/system/project/avatar/541/cmakelogo-centered.png" property="og:image">
<meta content="64" property="og:image:width">
<meta content="64" property="og:image:height">
<meta content="https://gitlab.kitware.com/cmake/cmake/-/blob/v3.21.1/Source/cmAddLibraryCommand.cxx" property="og:url">
<meta content="summary" property="twitter:card">
<meta content="Source/cmAddLibraryCommand.cxx · v3.21.1 · CMake / CMake · GitLab" property="twitter:title">
<meta content="CMake, the cross-platform, open-source build system." property="twitter:description">
<meta content="https://gitlab.kitware.com/uploads/-/system/project/avatar/541/cmakelogo-centered.png" property="twitter:image">

<meta content="CMake, the cross-platform, open-source build system." name="description">
<link href="/-/manifest.json" rel="manifest">
<meta content="width=device-width, initial-scale=1, maximum-scale=1" name="viewport">
<meta content="#292961" name="theme-color">
<meta name="csrf-param" content="authenticity_token">
<meta name="csrf-token" content="nbRTIKr0hfT3wm6D7bSNMcLTQrraqGPlYjuM2BjWwmiWFvtTeNjyUeEEib6aSEqwpvGcstMP+rnhehf+R5IIgQ==">
<meta name="csp-nonce">
<meta name="action-cable-url" content="/-/cable">
<link rel="apple-touch-icon" type="image/x-icon" href="/assets/apple-touch-icon-b049d4bc0dd9626f31db825d61880737befc7835982586d015bded10b4435460.png">
<link href="/search/opensearch.xml" rel="search" title="Search GitLab" type="application/opensearchdescription+xml">





<script charset="utf-8" src="/assets/webpack/hello.1902693f.chunk.js"></script><script charset="utf-8" src="/assets/webpack/727.ac41a851.chunk.js"></script><script charset="utf-8" src="/assets/webpack/vendors-globalSearch-top_nav.65cc19f9.chunk.js"></script><script charset="utf-8" src="/assets/webpack/vendors-top_nav.adcff1c4.chunk.js"></script><script charset="utf-8" src="/assets/webpack/top_nav.700b73f4.chunk.js"></script><script charset="utf-8" src="/assets/webpack/IssuablePopoverBundle.a37804a3.chunk.js"></script><script charset="utf-8" src="/assets/webpack/90.5683da81.chunk.js"></script><script charset="utf-8" src="/assets/webpack/hl-cpp.12674090.chunk.js"></script></head>

<body class="ui-indigo tab-width-8 gl-browser-chrome gl-platform-windows page-initialised" data-find-file="/cmake/cmake/-/find_file/v3.21.1" data-group="cmake" data-namespace-id="415" data-page="projects:blob:show" data-page-type-id="v3.21.1/Source/cmAddLibraryCommand.cxx" data-project="cmake" data-project-id="541">

<script>
//<![CDATA[
gl = window.gl || {};
gl.client = {"isChrome":true,"isWindows":true};


//]]>
</script>



<header class="navbar navbar-gitlab navbar-expand-sm js-navbar" data-qa-selector="navbar">
<a class="gl-sr-only gl-accessibility" href="#content-body">Skip to content</a>
<div class="container-fluid">
<div class="header-content js-header-content">
<div class="title-container hide-when-top-nav-responsive-open gl-transition-medium gl-display-flex gl-align-items-stretch gl-pt-0 gl-mr-3">
<div class="title">
<span class="gl-sr-only">GitLab</span>
<a title="Dashboard" id="logo" class="has-tooltip" href="/"><svg class="tanuki-logo" width="25" height="24" viewBox="0 0 25 24" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path class="tanuki-shape tanuki" d="m24.507 9.5-.034-.09L21.082.562a.896.896 0 0 0-1.694.091l-2.29 7.01H7.825L5.535.653a.898.898 0 0 0-1.694-.09L.451 9.411.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 2.56 1.935 1.554 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z" fill="#E24329"></path>
  <path class="tanuki-shape right-cheek" d="m24.507 9.5-.034-.09a11.44 11.44 0 0 0-4.56 2.051l-7.447 5.632 4.742 3.584 5.197-3.89.014-.01A6.297 6.297 0 0 0 24.507 9.5Z" fill="#FC6D26"></path>
  <path class="tanuki-shape chin" d="m7.707 20.677 2.56 1.935 1.555 1.176a1.051 1.051 0 0 0 1.268 0l1.555-1.176 2.56-1.935-4.743-3.584-4.755 3.584Z" fill="#FCA326"></path>
  <path class="tanuki-shape left-cheek" d="M5.01 11.461a11.43 11.43 0 0 0-4.56-2.05L.416 9.5a6.297 6.297 0 0 0 2.09 7.278l.012.01.03.022 5.16 3.867 4.745-3.584-7.444-5.632Z" fill="#FC6D26"></path>
</svg>

</a></div>
<div class="gl-display-flex gl-align-items-center">
</div>
<div class="gl-display-none gl-sm-display-block">
<ul class="nav navbar-sub-nav"><li class="nav-item b-nav-dropdown dropdown gl-new-dropdown" data-qa-selector="navbar_dropdown" data-qa-title="Menu" id="__BVID__56"><a role="button" aria-haspopup="true" aria-expanded="false" href="#" target="_self" class="nav-link dropdown-toggle top-nav-toggle js-top-nav-dropdown-toggle gl-px-3! dropdown-toggle-no-caret" id="__BVID__56__BV_toggle_"><svg data-testid="hamburger-icon" role="img" aria-hidden="true" class="gl-icon s16"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#hamburger"></use></svg> <!----></a><ul tabindex="-1" class="dropdown-menu gl-mt-3! gl-max-w-none! gl-max-h-none! gl-sm-w-auto! js-top-nav-dropdown-menu" aria-labelledby="__BVID__56__BV_toggle_"> <li role="presentation"><form tabindex="-1" class="b-dropdown-form gl-p-0"><div class="gl-display-flex gl-align-items-stretch"><div data-testid="menu-sidebar" class="gl-w-grid-size-30 gl-flex-shrink-0 gl-bg-gray-10 gl-p-3 gl-w-full"><div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column"><div data-testid="menu-section" class=""><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block">
        Explore
      </strong><a aria-label="Projects" data-qa-selector="menu_item_link" data-qa-title="Projects" href="/explore" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-shadow-none! gl-font-weight-bold! active gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="project-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#project"></use></svg> 
      Projects
      <!----></span></span></a><a aria-label="Groups" data-qa-selector="menu_item_link" data-qa-title="Groups" href="/explore/groups" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="group-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#group"></use></svg> 
      Groups
      <!----></span></span></a><a aria-label="Snippets" data-qa-selector="menu_item_link" data-qa-title="Snippets" href="/explore/snippets" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="snippet-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#snippet"></use></svg> 
      Snippets
      <!----></span></span></a></div></div></div> <div data-testid="menu-subview" data-qa-selector="menu_subview_container" class="gl-w-grid-size-40 gl-overflow-hidden gl-p-3" style="display: none;"></div></div></form></li></ul></li></ul>
<div class="hidden">
<a class="dashboard-shortcuts-projects" href="/explore">Projects
</a><a class="dashboard-shortcuts-groups" href="/explore/groups">Groups
</a><a class="dashboard-shortcuts-snippets" href="/explore/snippets">Snippets
</a></div>

</div>
</div>
<div class="navbar-collapse gl-transition-medium collapse gl-mr-auto global-search-container hide-when-top-nav-responsive-open">
<ul class="nav navbar-nav gl-w-full gl-align-items-center">
<li class="nav-item header-search-new gl-display-none gl-lg-display-block gl-w-full">
<div class="header-search is-not-active gl-relative gl-w-full" data-autocomplete-path="/search/autocomplete" data-issues-path="/dashboard/issues" data-mr-path="/dashboard/merge_requests" data-search-context="{&quot;group&quot;:{&quot;id&quot;:415,&quot;name&quot;:&quot;CMake&quot;,&quot;full_name&quot;:&quot;CMake&quot;},&quot;group_metadata&quot;:{&quot;group_path&quot;:&quot;cmake&quot;,&quot;name&quot;:&quot;CMake&quot;,&quot;issues_path&quot;:&quot;/groups/cmake/-/issues&quot;,&quot;mr_path&quot;:&quot;/groups/cmake/-/merge_requests&quot;},&quot;project&quot;:{&quot;id&quot;:541,&quot;name&quot;:&quot;CMake&quot;},&quot;project_metadata&quot;:{&quot;project_path&quot;:&quot;cmake&quot;,&quot;name&quot;:&quot;CMake&quot;,&quot;issues_path&quot;:&quot;/cmake/cmake/-/issues&quot;,&quot;mr_path&quot;:&quot;/cmake/cmake/-/merge_requests&quot;,&quot;issues_disabled&quot;:false},&quot;scope&quot;:null,&quot;code_search&quot;:true,&quot;ref&quot;:&quot;v3.21.1&quot;,&quot;for_snippets&quot;:false}" data-search-path="/search" id="js-header-search">
<form action="/search" accept-charset="UTF-8" method="get"><div class="gl-search-box-by-type">
<svg class="s16 gl-search-box-by-type-search-icon gl-icon" data-testid="search-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#search"></use></svg>
<input autocomplete="off" class="form-control gl-form-input gl-search-box-by-type-input" data-qa-selector="search_box" id="search" name="search" placeholder="Search GitLab" type="text">
</div>
<input type="hidden" name="group_id" id="group_id" value="415" autocomplete="off">
<input type="hidden" name="project_id" id="project_id" value="541" autocomplete="off">
<input type="hidden" name="scope" id="scope" autocomplete="off">
<input type="hidden" name="search_code" id="search_code" value="true" autocomplete="off">
<input type="hidden" name="snippets" id="snippets" value="false" autocomplete="off">
<input type="hidden" name="repository_ref" id="repository_ref" value="v3.21.1" autocomplete="off">
<input type="hidden" name="nav_source" id="nav_source" value="navbar" autocomplete="off">
<kbd class="gl-absolute gl-right-3 gl-top-0 keyboard-shortcut-helper gl-z-index-1 has-tooltip" data-html="true" data-placement="bottom" title="Use the shortcut key <kbd>/</kbd> to start a search">
/
</kbd>
</form></div>

</li>
<li class="nav-item d-none d-sm-inline-block d-lg-none">
<a title="Search" aria-label="Search" data-toggle="tooltip" data-placement="bottom" data-container="body" href="/search?project_id=541"><svg class="s16" data-testid="search-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#search"></use></svg>
</a></li>
</ul>
</div>
<div class="navbar-collapse gl-transition-medium collapse">
<ul class="nav navbar-nav gl-w-full gl-align-items-center gl-justify-content-end">
<li class="nav-item header-help dropdown d-none d-md-block" data-track-action="click_question_mark_link" data-track-experiment="cross_stage_fdm" data-track-label="main_navigation" data-track-property="navigation">
<a class="header-help-dropdown-toggle gl-relative" data-toggle="dropdown" href="/help"><span class="gl-sr-only">
Help
</span>
<svg class="s16" data-testid="question-o-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#question-o"></use></svg>
<span class="notification-dot rounded-circle gl-absolute"></span>
<svg class="s16 caret-down" data-testid="chevron-down-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#chevron-down"></use></svg>
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
<li class="nav-item">
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
<svg class="s16" data-testid="hamburger-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#hamburger"></use></svg>
</span>
<svg class="s12 close-icon" data-testid="close-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#close"></use></svg>
</button>
</div>
</div>
</header>

<div class="layout-page hide-when-top-nav-responsive-open page-with-contextual-sidebar">
<aside aria-label="Project navigation" class="nav-sidebar js-sidebar-collapsed">
<div class="nav-sidebar-inner-scroll">
<ul class="sidebar-top-level-items" data-qa-selector="project_sidebar">
<li data-track-label="scope_menu" data-container="body" data-placement="right" class="context-header has-tooltip" title="CMake"><a aria-label="CMake" class="shortcuts-project rspec-project-link gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project scope" href="/cmake/cmake"><span class="avatar-container rect-avatar s32 project_avatar">
<img alt="CMake" class="avatar avatar-tile s32 js-lazy-loaded qa-js-lazy-loaded" width="32" height="32" src="/uploads/-/system/project/avatar/541/cmakelogo-centered.png?width=32" loading="lazy">
</span>
<span class="sidebar-context-title">
CMake
</span>
</a></li>
<li data-track-label="project_information_menu" class="home"><a aria-label="Project information" class="shortcuts-project-information has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Project information" href="/cmake/cmake/activity"><span class="nav-icon-container">
<svg class="s16" data-testid="project-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#project"></use></svg>
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
<li data-track-label="activity" class=""><a aria-label="Activity" class="shortcuts-project-activity gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Activity" href="/cmake/cmake/activity"><span>
Activity
</span>
</a></li><li data-track-label="labels" class=""><a aria-label="Labels" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Labels" href="/cmake/cmake/-/labels"><span>
Labels
</span>
</a></li><li data-track-label="members" class=""><a aria-label="Members" id="js-onboarding-members-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Members" href="/cmake/cmake/-/project_members"><span>
Members
</span>
</a></li>
</ul>

</li><li data-track-label="repository_menu" class="active"><a aria-label="Repository" class="shortcuts-tree has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Repository" href="/cmake/cmake/-/tree/v3.21.1"><span class="nav-icon-container">
<svg class="s16" data-testid="doc-text-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#doc-text"></use></svg>
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
<li data-track-label="files" class="active"><a aria-label="Files" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Files" href="/cmake/cmake/-/tree/v3.21.1"><span>
Files
</span>
</a></li><li data-track-label="commits" class=""><a aria-label="Commits" id="js-onboarding-commits-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Commits" href="/cmake/cmake/-/commits/v3.21.1"><span>
Commits
</span>
</a></li><li data-track-label="branches" class=""><a aria-label="Branches" id="js-onboarding-branches-link" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Branches" href="/cmake/cmake/-/branches"><span>
Branches
</span>
</a></li><li data-track-label="tags" class=""><a aria-label="Tags" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Tags" href="/cmake/cmake/-/tags"><span>
Tags
</span>
</a></li><li data-track-label="contributors" class=""><a aria-label="Contributors" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Contributors" href="/cmake/cmake/-/graphs/v3.21.1"><span>
Contributors
</span>
</a></li><li data-track-label="graphs" class=""><a aria-label="Graph" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Graph" href="/cmake/cmake/-/network/v3.21.1"><span>
Graph
</span>
</a></li><li data-track-label="compare" class=""><a aria-label="Compare" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Compare" href="/cmake/cmake/-/compare?from=master&amp;to=v3.21.1"><span>
Compare
</span>
</a></li>
</ul>

</li><li data-track-label="issues_menu" class=""><a aria-label="Issues" class="shortcuts-issues has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Issues" href="/cmake/cmake/-/issues"><span class="nav-icon-container">
<svg class="s16" data-testid="issues-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#issues"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-issues-link">
Issues
</span>
<span class="gl-badge badge badge-pill badge-info sm count issue_counter">4,034
</span></a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Issues
</strong>
<span class="gl-badge badge badge-pill badge-info sm count fly-out-badge issue_counter">4,034
</span></span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="issue_list" class=""><a aria-label="Issues" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="List" href="/cmake/cmake/-/issues"><span>
List
</span>
</a></li><li data-track-label="boards" class=""><a aria-label="Boards" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Boards" href="/cmake/cmake/-/boards"><span>
Boards
</span>
</a></li><li data-track-label="service_desk" class=""><a aria-label="Service Desk" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Service Desk" href="/cmake/cmake/-/issues/service_desk"><span>
Service Desk
</span>
</a></li><li data-track-label="milestones" class=""><a aria-label="Milestones" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Milestones" href="/cmake/cmake/-/milestones"><span>
Milestones
</span>
</a></li>
</ul>

</li><li data-track-label="merge_requests_menu" class=""><a aria-label="Merge requests" class="shortcuts-merge_requests gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Merge requests" href="/cmake/cmake/-/merge_requests"><span class="nav-icon-container">
<svg class="s16" data-testid="git-merge-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#git-merge"></use></svg>
</span>
<span class="nav-item-name" id="js-onboarding-mr-link">
Merge requests
</span>
<span class="gl-badge badge badge-pill badge-info sm count merge_counter js-merge-counter">12
</span></a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Merge requests
</strong>
<span class="gl-badge badge badge-pill badge-info sm count fly-out-badge merge_counter js-merge-counter">12
</span></span>
</li></ul>

</li><li data-track-label="ci_cd_menu" class=""><a aria-label="CI/CD" class="shortcuts-pipelines rspec-link-pipelines has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="CI/CD" href="/cmake/cmake/-/pipelines"><span class="nav-icon-container">
<svg class="s16" data-testid="rocket-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#rocket"></use></svg>
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
<li data-track-label="pipelines" class=""><a aria-label="Pipelines" class="shortcuts-pipelines gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Pipelines" href="/cmake/cmake/-/pipelines"><span>
Pipelines
</span>
</a></li><li data-track-label="jobs" class=""><a aria-label="Jobs" class="shortcuts-builds gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Jobs" href="/cmake/cmake/-/jobs"><span>
Jobs
</span>
</a></li><li data-track-label="pipeline_schedules" class=""><a aria-label="Schedules" class="shortcuts-builds gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Schedules" href="/cmake/cmake/-/pipeline_schedules"><span>
Schedules
</span>
</a></li>
</ul>

</li><li data-track-label="deployments_menu" class=""><a aria-label="Deployments" class="shortcuts-deployments has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Deployments" href="/cmake/cmake/-/releases"><span class="nav-icon-container">
<svg class="s16" data-testid="deployments-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#deployments"></use></svg>
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
<li data-track-label="releases" class=""><a aria-label="Releases" class="shortcuts-deployments-releases gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Releases" href="/cmake/cmake/-/releases"><span>
Releases
</span>
</a></li>
</ul>

</li><li data-track-label="packages_registries_menu" class=""><a aria-label="Packages and registries" class="has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Packages and registries" href="/cmake/cmake/container_registry"><span class="nav-icon-container">
<svg class="s16" data-testid="package-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#package"></use></svg>
</span>
<span class="nav-item-name">
Packages and registries
</span>
</a><ul class="sidebar-sub-level-items">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
Packages and registries
</strong>
</span>
</li><li class="divider fly-out-top-item"></li>
<li data-track-label="container_registry" class=""><a aria-label="Container Registry" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Container Registry" href="/cmake/cmake/container_registry"><span>
Container Registry
</span>
</a></li>
</ul>

</li><li data-track-label="analytics_menu" class=""><a aria-label="Analytics" class="shortcuts-analytics has-sub-items gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="Analytics" href="/cmake/cmake/-/value_stream_analytics"><span class="nav-icon-container">
<svg class="s16" data-testid="chart-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#chart"></use></svg>
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
<li data-track-label="cycle_analytics" class=""><a aria-label="Value stream" class="shortcuts-project-cycle-analytics gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Value stream" href="/cmake/cmake/-/value_stream_analytics"><span>
Value stream
</span>
</a></li><li data-track-label="ci_cd_analytics" class=""><a aria-label="CI/CD" class="gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="CI/CD" href="/cmake/cmake/-/pipelines/charts"><span>
CI/CD
</span>
</a></li><li data-track-label="repository_analytics" class=""><a aria-label="Repository" class="shortcuts-repository-charts gl-link" data-qa-selector="sidebar_menu_item_link" data-qa-menu-item="Repository" href="/cmake/cmake/-/graphs/v3.21.1/charts"><span>
Repository
</span>
</a></li>
</ul>

</li><li data-track-label="external_wiki_menu" class=""><a aria-label="External wiki" target="_blank" rel="noopener noreferrer" class="shortcuts-external_wiki gl-link" data-qa-selector="sidebar_menu_link" data-qa-menu-item="External wiki" href="https://gitlab.kitware.com/cmake/community/wikis/home"><span class="nav-icon-container">
<svg class="s16" data-testid="external-link-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#external-link"></use></svg>
</span>
<span class="nav-item-name">
External wiki
</span>
</a><ul class="sidebar-sub-level-items is-fly-out-only">
<li class="fly-out-top-item"><span class="fly-out-top-item-container">
<strong class="fly-out-top-item-name">
External wiki
</strong>
</span>
</li></ul>

</li>
<li class="hidden">
<a aria-label="Activity" class="shortcuts-project-activity gl-link" href="/cmake/cmake/activity">Activity
</a></li>
<li class="hidden">
<a aria-label="Graph" class="shortcuts-network gl-link" href="/cmake/cmake/-/network/v3.21.1">Graph
</a></li>
<li class="hidden">
<a aria-label="Create a new issue" class="shortcuts-new-issue gl-link" href="/cmake/cmake/-/issues/new">Create a new issue
</a></li>
<li class="hidden">
<a aria-label="Jobs" class="shortcuts-builds gl-link" href="/cmake/cmake/-/jobs">Jobs
</a></li>
<li class="hidden">
<a aria-label="Commits" class="shortcuts-commits gl-link" href="/cmake/cmake/-/commits/master">Commits
</a></li>
<li class="hidden">
<a aria-label="Issue Boards" class="shortcuts-issue-boards gl-link" href="/cmake/cmake/-/boards">Issue Boards
</a></li>

</ul>
<a class="toggle-sidebar-button js-toggle-sidebar rspec-toggle-sidebar" role="button" title="Toggle sidebar" type="button">
<svg class="s12 icon-chevron-double-lg-left" data-testid="chevron-double-lg-left-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#chevron-double-lg-left"></use></svg>
<span class="collapse-text gl-ml-3">Collapse sidebar</span>
</a>
<button name="button" type="button" class="close-nav-button"><svg class="s16" data-testid="close-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#close"></use></svg>
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
<svg class="s18" data-testid="sidebar-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#sidebar"></use></svg>
</button><div class="breadcrumbs-links" data-qa-selector="breadcrumb_links_content" data-testid="breadcrumb-links">
<ul class="list-unstyled breadcrumbs-list js-breadcrumbs-list">
<li><a class="group-path breadcrumb-item-text js-breadcrumb-item-text " href="/cmake"><img alt="CMake" class="avatar-tile js-lazy-loaded qa-js-lazy-loaded" width="15" height="15" src="/uploads/-/system/group/avatar/415/cmakelogo-centered.png?width=15" loading="lazy">CMake</a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#chevron-lg-right"></use></svg></li> <li><a href="/cmake/cmake"><img alt="CMake" class="avatar-tile js-lazy-loaded qa-js-lazy-loaded" width="15" height="15" src="/uploads/-/system/project/avatar/541/cmakelogo-centered.png?width=15" loading="lazy"><span class="breadcrumb-item-text js-breadcrumb-item-text">CMake</span></a><svg class="s8 breadcrumbs-list-angle" data-testid="chevron-lg-right-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#chevron-lg-right"></use></svg></li>

<li data-qa-selector="breadcrumb_current_link" data-testid="breadcrumb-current-link">
<a href="/cmake/cmake/-/blob/v3.21.1/Source/cmAddLibraryCommand.cxx">Repository</a>
</li>
</ul>
</div>
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"CMake","item":"https://gitlab.kitware.com/cmake"},{"@type":"ListItem","position":2,"name":"CMake","item":"https://gitlab.kitware.com/cmake/cmake"},{"@type":"ListItem","position":3,"name":"Repository","item":"https://gitlab.kitware.com/cmake/cmake/-/blob/v3.21.1/Source/cmAddLibraryCommand.cxx"}]}

</script>

</div>
</nav>

</div>
<div class="container-fluid container-limited project-highlight-puc">
<main class="content" id="content-body" itemscope="" itemtype="http://schema.org/SoftwareSourceCode">
<div class="flash-container flash-container-page sticky" data-qa-selector="flash_container">
</div>



<div class="js-signature-container" data-signatures-path="/cmake/cmake/-/commits/4d46b1401f9d1624fa5afc3995844d7aebc7ccf4/signatures?limit=1"></div>

<div class="tree-holder" id="tree-holder">
<div class="nav-block">
<div class="tree-ref-container">
<div class="tree-ref-holder">
<form class="project-refs-form" action="/cmake/cmake/-/refs/switch" accept-charset="UTF-8" method="get"><input type="hidden" name="destination" id="destination" value="blob" autocomplete="off">
<div class="dropdown">
<button class="dropdown-menu-toggle js-project-refs-dropdown" type="button" data-toggle="dropdown" data-selected="v3.21.1" data-ref="v3.21.1" data-refs-url="/cmake/cmake/refs?sort=updated_desc" data-field-name="ref" data-submit-form-on-click="true" data-visit="true" data-qa-selector="branches_dropdown" data-testid="branches-select"><span class="dropdown-toggle-text ">v3.21.1</span><svg class="s16 dropdown-menu-toggle-icon gl-top-3" data-testid="chevron-down-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#chevron-down"></use></svg></button>
<div class="dropdown-menu dropdown-menu-selectable git-revision-dropdown dropdown-menu-paging" data-qa-selector="branches_dropdown_content">
<div class="dropdown-page-one">
<div class="dropdown-title gl-display-flex"><span class="gl-ml-auto">Switch branch/tag</span><button class="dropdown-title-button dropdown-menu-close gl-ml-auto" aria-label="Close" type="button"><svg class="s16 dropdown-menu-close-icon" data-testid="close-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#close"></use></svg></button></div>
<div class="dropdown-input"><input type="search" data-qa-selector="dropdown_input_field" class="dropdown-input-field" placeholder="Search branches and tags" autocomplete="off"><svg class="s16 dropdown-input-search" data-testid="search-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#search"></use></svg><svg class="s16 dropdown-input-clear js-dropdown-input-clear" data-testid="close-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#close"></use></svg></div>
<div class="dropdown-content"></div>
<div class="dropdown-loading"><div class="gl-spinner-container gl-mt-7" role="status"><span class="gl-spinner gl-spinner-dark gl-spinner-md gl-vertical-align-text-bottom!" aria-label="Loading"></span></div></div>
</div>
</div>
</div>
</form>
</div>
<ul class="breadcrumb repo-breadcrumb">
<li class="breadcrumb-item">
<a href="/cmake/cmake/-/tree/v3.21.1">cmake
</a></li>
<li class="breadcrumb-item">
<a href="/cmake/cmake/-/tree/v3.21.1/Source">Source</a>
</li>
<li class="breadcrumb-item">
<a href="/cmake/cmake/-/blob/v3.21.1/Source/cmAddLibraryCommand.cxx"><strong>cmAddLibraryCommand.cxx</strong>
</a></li>
</ul>
</div>
<div class="tree-controls gl-children-ml-sm-3"><a class="gl-button btn btn-default shortcuts-find-file" rel="nofollow" href="/cmake/cmake/-/find_file/v3.21.1">Find file
</a><a class="gl-button btn btn-default js-blob-blame-link" href="/cmake/cmake/-/blame/v3.21.1/Source/cmAddLibraryCommand.cxx#L224-231" data-original-href="/cmake/cmake/-/blame/v3.21.1/Source/cmAddLibraryCommand.cxx">Blame</a><a class="gl-button btn btn-default" href="/cmake/cmake/-/commits/v3.21.1/Source/cmAddLibraryCommand.cxx">History</a><a class="gl-button btn btn-default js-data-file-blob-permalink-url" href="/cmake/cmake/-/blob/f7cf69e34a1607e8ea2b6d10fef6a6058377c24e/Source/cmAddLibraryCommand.cxx#L224-231" data-original-href="/cmake/cmake/-/blob/f7cf69e34a1607e8ea2b6d10fef6a6058377c24e/Source/cmAddLibraryCommand.cxx">Permalink</a></div>
</div>

<div class="info-well d-none d-sm-block">
<div class="well-segment">
<ul class="blob-commit-info">
<li class="commit flex-row js-toggle-container" id="commit-4d46b140">
<div class="avatar-cell d-none d-sm-block">
<a href="/craig.scott"><img alt="Craig Scott's avatar" src="https://secure.gravatar.com/avatar/196507edbb408bad2f2a08e33222bac7?s=80&amp;d=identicon" class="avatar s40 d-none d-sm-inline-block" title="Craig Scott"></a>
</div>
<div class="commit-detail flex-list gl-display-flex gl-justify-content-space-between gl-align-items-flex-start gl-flex-grow-1 gl-min-w-0">
<div class="commit-content" data-qa-selector="commit_content">
<a class="commit-row-message item-title js-onboarding-commit-item " href="/cmake/cmake/-/commit/4d46b1401f9d1624fa5afc3995844d7aebc7ccf4">add_library(): Allow imported object libraries with multi-arch</a>
<span class="commit-row-message d-inline d-sm-none">
·
4d46b140
</span>
<button aria-label="Toggle commit description" class="gl-button btn btn-default button-ellipsis-horizontal btn-sm gl-ml-2 text-expander js-toggle-button" data-container="body" data-toggle="tooltip" title="Toggle commit description">
<svg class="s12" data-testid="ellipsis_h-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#ellipsis_h"></use></svg>
</button>
<div class="committer">
<a class="commit-author-link js-user-link" data-user-id="800" href="/craig.scott">Craig Scott</a> authored <time class="js-timeago" title="Feb 4, 2021 5:30pm GMT+0800" datetime="2021-02-04T09:30:49Z" data-toggle="tooltip" data-placement="bottom" data-container="body">1 year ago</time>
</div>

<pre class="commit-row-description gl-mb-3 gl-white-space-pre-line js-toggle-content">Fixes: <a href="/cmake/cmake/-/issues/21276" data-reference-type="issue" data-original="#21276" data-link="false" data-link-reference="false" data-project="541" data-issue="85042" data-project-path="cmake/cmake" data-iid="21276" data-issue-type="issue" data-container="body" data-placement="top" title="Xcode: Imported object libraries break configuration when building an iOS project" class="gfm gfm-issue" data-popover-listener-added="true">#21276</a></pre>
</div>
<div class="commit-actions flex-row">

<div class="js-commit-pipeline-status" data-endpoint="/cmake/cmake/-/commit/4d46b1401f9d1624fa5afc3995844d7aebc7ccf4/pipelines?ref=v3.21.1"></div>
<div class="commit-sha-group btn-group d-none d-sm-flex">
<div class="label label-monospace monospace">
4d46b140
</div>
<button class="btn gl-button btn btn-default btn-icon" data-toggle="tooltip" data-placement="bottom" data-container="body" data-title="Copy commit SHA" data-class="gl-button btn btn-default btn-icon" data-clipboard-text="4d46b1401f9d1624fa5afc3995844d7aebc7ccf4" type="button" title="Copy commit SHA" aria-label="Copy commit SHA" aria-live="polite"><svg class="s16 gl-icon" data-testid="copy-to-clipboard-icon"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#copy-to-clipboard"></use></svg></button>

</div>
</div>
</div>
</li>

</ul>
</div>
<div data-blob-path="Source/cmAddLibraryCommand.cxx" data-branch="v3.21.1" data-project-path="cmake/cmake" id="js-code-owners"></div>

</div>
<div class="blob-content-holder" id="blob-content-holder">
<div><!----> <div class="file-holder"><div class="js-file-title file-title-flex-parent"><div class="gl-display-flex"><!----> <div class="file-header-content d-flex align-items-center lh-100"> <span aria-hidden="true"><svg class="s16 gl-mr-3"><use xlink:href="/assets/file_icons-958d18a1c33aa82a81e2eb1ffbffc33131d501c41ad95838a70b089e5ffbd7a0.svg#cpp"></use></svg></span> <strong data-qa-selector="file_title_content" class="file-title-name mr-1 js-blob-header-filepath">cmAddLibraryCommand.cxx</strong> <button id="clipboard-button-2" title="Copy file path" data-clipboard-text="{&quot;text&quot;:&quot;Source/cmAddLibraryCommand.cxx&quot;,&quot;gfm&quot;:&quot;`Source/cmAddLibraryCommand.cxx`&quot;}" data-clipboard-handle-tooltip="false" aria-label="Copy file path" aria-live="polite" type="button" class="btn btn-default btn-md gl-button btn-default-tertiary btn-icon btn-clipboard btn-transparent lh-100 position-static"><!----> <svg data-testid="copy-to-clipboard-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#copy-to-clipboard"></use></svg>  <!----></button> <small class="gl-mr-3">9.51 KiB</small> <!----></div></div> <div class="gl-display-flex gl-flex-wrap file-actions"><!----> <div class="gl-sm-ml-3 gl-mr-3"><div class="dropdown b-dropdown gl-new-dropdown btn-group" data-qa-selector="action_dropdown" split-href="/-/ide/project/cmake/cmake/edit/v3.21.1/-/Source/cmAddLibraryCommand.cxx" id="__BVID__19"><a href="/-/ide/project/cmake/cmake/edit/v3.21.1/-/Source/cmAddLibraryCommand.cxx" target="_self" class="btn btn-confirm btn-md gl-button split-content-button" id="__BVID__19__BV_button_"><span data-qa-selector="web_ide_button" data-track-action="click_consolidated_edit_ide" data-track-label="web_ide" class="gl-new-dropdown-button-text">
      Open in Web IDE
    </span></a><button aria-haspopup="true" aria-expanded="false" type="button" class="btn dropdown-toggle btn-confirm btn-md gl-button gl-dropdown-toggle dropdown-toggle-split" id="__BVID__19__BV_toggle_"><span class="sr-only">Toggle dropdown</span></button><ul role="menu" tabindex="-1" class="dropdown-menu" aria-labelledby="__BVID__19__BV_button_"><div class="gl-new-dropdown-inner"><!----> <!----> <div class="gl-new-dropdown-contents"><!---->  <li role="presentation" class="gl-new-dropdown-item"><button data-qa-selector="webide_menu_item" data-testid="action_webide" role="menuitem" type="button" class="dropdown-item"><svg data-testid="dropdown-item-checkbox" role="img" aria-hidden="true" class="gl-icon s16 gl-new-dropdown-item-check-icon gl-mt-3 gl-align-self-start"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#mobile-issue-close"></use></svg> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary"><span class="gl-font-weight-bold">Open in Web IDE</span></p> <p class="gl-new-dropdown-item-text-secondary">Quickly and easily edit multiple files in your project.</p></div> <!----></button></li> <li role="presentation" class="gl-new-dropdown-divider"><hr role="separator" aria-orientation="horizontal" class="dropdown-divider"></li><li role="presentation" class="gl-new-dropdown-item"><button data-qa-selector="edit_menu_item" data-testid="action_edit" role="menuitem" type="button" class="dropdown-item"><svg data-testid="dropdown-item-checkbox" role="img" aria-hidden="true" class="gl-icon s16 gl-new-dropdown-item-check-icon gl-visibility-hidden gl-mt-3 gl-align-self-start"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#mobile-issue-close"></use></svg> <!----> <!----> <div class="gl-new-dropdown-item-text-wrapper"><p class="gl-new-dropdown-item-text-primary"><span class="gl-font-weight-bold">Edit</span></p> <p class="gl-new-dropdown-item-text-secondary">Edit this file only.</p></div> <!----></button></li> <!----></div> <!----></div></ul></div> <!----> <!----> <!----></div> <!----> <div data-qa-selector="default_actions_container" role="group" class="btn-group"><button aria-label="Copy file contents" title="Copy file contents" data-testid="copyContentsButton" data-qa-selector="copy_contents_button" type="button" class="btn js-copy-blob-source-btn btn-default btn-md gl-button btn-icon"><!----> <svg data-testid="copy-to-clipboard-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#copy-to-clipboard"></use></svg>  <!----></button> <a aria-label="Open raw" title="Open raw" href="/cmake/cmake/-/raw/v3.21.1/Source/cmAddLibraryCommand.cxx" rel="noopener" target="_blank" class="btn btn-default btn-md gl-button btn-icon"><!----> <svg data-testid="doc-code-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#doc-code"></use></svg>  <!----></a> <a aria-label="Download" title="Download" href="https://gitlab.kitware.com/cmake/cmake/-/raw/v3.21.1/Source/cmAddLibraryCommand.cxx?inline=false" rel="noopener" target="_blank" class="btn btn-default btn-md gl-button btn-icon"><!----> <svg data-testid="download-icon" role="img" aria-hidden="true" class="gl-button-icon gl-icon s16"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#download"></use></svg>  <!----></a> <!----></div></div></div> <!----> <div data-type="simple" data-path="Source/cmAddLibraryCommand.cxx" data-qa-selector="blob_viewer_file_content" class="file-content code js-syntax-highlight blob-content gl-display-flex gl-flex-direction-column gl-overflow-auto blob-viewer white"><div><div><div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L1" href="#L1" data-line-number="1" class="gl-user-select-none gl-shadow-none! file-line-num">
      1
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC1" lang="cpp" data-testid="content" class="line"><span class="hljs-comment"><span class="hljs-comment">/*</span><span class="hljs-comment"> Distributed under the </span><span class="hljs-comment">OSI-approved BSD 3-Clause License.  See accompanying</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L2" href="#L2" data-line-number="2" class="gl-user-select-none gl-shadow-none! file-line-num">
      2
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC2" lang="cpp" data-testid="content" class="line"><span class="hljs-comment">   file Copyright.txt or https://cmake.org/licensing for details.  */</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L3" href="#L3" data-line-number="3" class="gl-user-select-none gl-shadow-none! file-line-num">
      3
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC3" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmAddLibraryCommand.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L4" href="#L4" data-line-number="4" class="gl-user-select-none gl-shadow-none! file-line-num">
      4
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC4" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L5" href="#L5" data-line-number="5" class="gl-user-select-none gl-shadow-none! file-line-num">
      5
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC5" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmExecutionStatus.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L6" href="#L6" data-line-number="6" class="gl-user-select-none gl-shadow-none! file-line-num">
      6
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC6" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmGeneratorExpression.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L7" href="#L7" data-line-number="7" class="gl-user-select-none gl-shadow-none! file-line-num">
      7
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC7" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmGlobalGenerator.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L8" href="#L8" data-line-number="8" class="gl-user-select-none gl-shadow-none! file-line-num">
      8
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC8" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmMakefile.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L9" href="#L9" data-line-number="9" class="gl-user-select-none gl-shadow-none! file-line-num">
      9
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC9" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmMessageType.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L10" href="#L10" data-line-number="10" class="gl-user-select-none gl-shadow-none! file-line-num">
      10
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC10" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmPolicies.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L11" href="#L11" data-line-number="11" class="gl-user-select-none gl-shadow-none! file-line-num">
      11
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC11" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmState.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L12" href="#L12" data-line-number="12" class="gl-user-select-none gl-shadow-none! file-line-num">
      12
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC12" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmStateTypes.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L13" href="#L13" data-line-number="13" class="gl-user-select-none gl-shadow-none! file-line-num">
      13
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC13" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmStringAlgorithms.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L14" href="#L14" data-line-number="14" class="gl-user-select-none gl-shadow-none! file-line-num">
      14
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC14" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-meta"><span class="hljs-meta">#</span><span class="hljs-keyword">include</span><span class="hljs-meta"> </span><span class="hljs-string">"cmTarget.h"</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L15" href="#L15" data-line-number="15" class="gl-user-select-none gl-shadow-none! file-line-num">
      15
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC15" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L16" href="#L16" data-line-number="16" class="gl-user-select-none gl-shadow-none! file-line-num">
      16
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC16" lang="cpp" data-testid="content" class="line"><span class=""></span><span class="hljs-function"><span class="hljs-type">bool</span><span class="hljs-function"> </span><span class="hljs-title">cmAddLibraryCommand</span><span class="hljs-params"><span class="hljs-params">(std::</span><span class="hljs-params">vector&lt;std::string&gt; </span><span class="hljs-type">const</span><span class="hljs-params">&amp; args,</span></span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L17" href="#L17" data-line-number="17" class="gl-user-select-none gl-shadow-none! file-line-num">
      17
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC17" lang="cpp" data-testid="content" class="line"><span class="hljs-params">                         cmExecutionStatus&amp; status)</span><span class="hljs-function"></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L18" href="#L18" data-line-number="18" class="gl-user-select-none gl-shadow-none! file-line-num">
      18
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC18" lang="cpp" data-testid="content" class="line"><span class="hljs-function"></span><span class="">{</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L19" href="#L19" data-line-number="19" class="gl-user-select-none gl-shadow-none! file-line-num">
      19
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC19" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(args.</span><span class="hljs-built_in">empty</span><span class="">()</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L20" href="#L20" data-line-number="20" class="gl-user-select-none gl-shadow-none! file-line-num">
      20
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC20" lang="cpp" data-testid="content" class="line"><span class="">    status.</span><span class="hljs-built_in">SetError</span><span class="">(</span><span class="hljs-string">"called with incorrect number of arguments"</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L21" href="#L21" data-line-number="21" class="gl-user-select-none gl-shadow-none! file-line-num">
      21
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC21" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L22" href="#L22" data-line-number="22" class="gl-user-select-none gl-shadow-none! file-line-num">
      22
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC22" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L23" href="#L23" data-line-number="23" class="gl-user-select-none gl-shadow-none! file-line-num">
      23
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC23" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L24" href="#L24" data-line-number="24" class="gl-user-select-none gl-shadow-none! file-line-num">
      24
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC24" lang="cpp" data-testid="content" class="line"><span class="">  cmMakefile&amp; mf </span><span class="">= status.</span><span class="hljs-built_in">GetMakefile</span><span class="">()</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L25" href="#L25" data-line-number="25" class="gl-user-select-none gl-shadow-none! file-line-num">
      25
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC25" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">//</span><span class="hljs-comment"> Library type defaults </span><span class="hljs-comment">to value of BUILD_SHARED_LIBS, if it exists,</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L26" href="#L26" data-line-number="26" class="gl-user-select-none gl-shadow-none! file-line-num">
      26
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC26" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">//</span><span class="hljs-comment"> otherwise it defaults </span><span class="hljs-comment">to static library.</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L27" href="#L27" data-line-number="27" class="gl-user-select-none gl-shadow-none! file-line-num">
      27
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC27" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="">cmStateEnums::</span><span class="">TargetType type </span><span class="">= cmStateEnums::SHARED_LIBRARY;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L28" href="#L28" data-line-number="28" class="gl-user-select-none gl-shadow-none! file-line-num">
      28
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC28" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(</span><span class="hljs-built_in">cmIsOff</span><span class="">(mf.</span><span class="hljs-built_in">GetDefinition</span><span class="">(</span><span class="hljs-string">"BUILD_SHARED_LIBS"</span><span class="">)</span><span class="">)</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L29" href="#L29" data-line-number="29" class="gl-user-select-none gl-shadow-none! file-line-num">
      29
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC29" lang="cpp" data-testid="content" class="line"><span class="">    type </span><span class="">= cmStateEnums::STATIC_LIBRARY;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L30" href="#L30" data-line-number="30" class="gl-user-select-none gl-shadow-none! file-line-num">
      30
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC30" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L31" href="#L31" data-line-number="31" class="gl-user-select-none gl-shadow-none! file-line-num">
      31
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC31" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">bool</span><span class=""> excludeFromAll </span><span class="">= </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L32" href="#L32" data-line-number="32" class="gl-user-select-none gl-shadow-none! file-line-num">
      32
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC32" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">bool</span><span class=""> importTarget </span><span class="">= </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L33" href="#L33" data-line-number="33" class="gl-user-select-none gl-shadow-none! file-line-num">
      33
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC33" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">bool</span><span class=""> importGlobal </span><span class="">= </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L34" href="#L34" data-line-number="34" class="gl-user-select-none gl-shadow-none! file-line-num">
      34
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC34" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L35" href="#L35" data-line-number="35" class="gl-user-select-none gl-shadow-none! file-line-num">
      35
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC35" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">auto</span><span class=""> s </span><span class="">= args.</span><span class="hljs-built_in">begin</span><span class="">()</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L36" href="#L36" data-line-number="36" class="gl-user-select-none gl-shadow-none! file-line-num">
      36
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC36" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L37" href="#L37" data-line-number="37" class="gl-user-select-none gl-shadow-none! file-line-num">
      37
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC37" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="">std::</span><span class="">string </span><span class="hljs-type">const</span><span class="">&amp; libName </span><span class="">= *s;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L38" href="#L38" data-line-number="38" class="gl-user-select-none gl-shadow-none! file-line-num">
      38
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC38" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L39" href="#L39" data-line-number="39" class="gl-user-select-none gl-shadow-none! file-line-num">
      39
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC39" lang="cpp" data-testid="content" class="line"><span class="">  ++s;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L40" href="#L40" data-line-number="40" class="gl-user-select-none gl-shadow-none! file-line-num">
      40
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC40" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L41" href="#L41" data-line-number="41" class="gl-user-select-none gl-shadow-none! file-line-num">
      41
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC41" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">// If</span><span class="hljs-comment"> the second argument </span><span class="hljs-comment">is "SHARED" or "STATIC", then it controls</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L42" href="#L42" data-line-number="42" class="gl-user-select-none gl-shadow-none! file-line-num">
      42
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC42" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">// the type of library.  Otherwise,</span><span class="hljs-comment"> it is treated </span><span class="hljs-comment">as a source or</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L43" href="#L43" data-line-number="43" class="gl-user-select-none gl-shadow-none! file-line-num">
      43
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC43" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">//</span><span class="hljs-comment"> source list name. </span><span class="hljs-comment">There may be two keyword arguments, check for them</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L44" href="#L44" data-line-number="44" class="gl-user-select-none gl-shadow-none! file-line-num">
      44
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC44" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">bool</span><span class=""> haveSpecifiedType </span><span class="">= </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L45" href="#L45" data-line-number="45" class="gl-user-select-none gl-shadow-none! file-line-num">
      45
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC45" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-type">bool</span><span class=""> isAlias </span><span class="">= </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L46" href="#L46" data-line-number="46" class="gl-user-select-none gl-shadow-none! file-line-num">
      46
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC46" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">while</span><span class=""> </span><span class="">(s != args.</span><span class="hljs-built_in">end</span><span class="">()</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L47" href="#L47" data-line-number="47" class="gl-user-select-none gl-shadow-none! file-line-num">
      47
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC47" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="">std::</span><span class="">string libType </span><span class="">= *s;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L48" href="#L48" data-line-number="48" class="gl-user-select-none gl-shadow-none! file-line-num">
      48
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC48" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(libType == </span><span class="hljs-string">"STATIC"</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L49" href="#L49" data-line-number="49" class="gl-user-select-none gl-shadow-none! file-line-num">
      49
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC49" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(type == cmStateEnums::INTERFACE_LIBRARY)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L50" href="#L50" data-line-number="50" class="gl-user-select-none gl-shadow-none! file-line-num">
      50
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC50" lang="cpp" data-testid="content" class="line"><span class="">        status.</span><span class="hljs-built_in">SetError</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L51" href="#L51" data-line-number="51" class="gl-user-select-none gl-shadow-none! file-line-num">
      51
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC51" lang="cpp" data-testid="content" class="line"><span class="">          </span><span class="hljs-string">"INTERFACE library specified with conflicting STATIC type."</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L52" href="#L52" data-line-number="52" class="gl-user-select-none gl-shadow-none! file-line-num">
      52
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC52" lang="cpp" data-testid="content" class="line"><span class="">        </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L53" href="#L53" data-line-number="53" class="gl-user-select-none gl-shadow-none! file-line-num">
      53
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC53" lang="cpp" data-testid="content" class="line"><span class="">      }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L54" href="#L54" data-line-number="54" class="gl-user-select-none gl-shadow-none! file-line-num">
      54
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC54" lang="cpp" data-testid="content" class="line"><span class="">      ++s;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L55" href="#L55" data-line-number="55" class="gl-user-select-none gl-shadow-none! file-line-num">
      55
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC55" lang="cpp" data-testid="content" class="line"><span class="">      type </span><span class="">= cmStateEnums::STATIC_LIBRARY;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L56" href="#L56" data-line-number="56" class="gl-user-select-none gl-shadow-none! file-line-num">
      56
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC56" lang="cpp" data-testid="content" class="line"><span class="">      haveSpecifiedType </span><span class="">= </span><span class="hljs-literal">true</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L57" href="#L57" data-line-number="57" class="gl-user-select-none gl-shadow-none! file-line-num">
      57
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC57" lang="cpp" data-testid="content" class="line"><span class="">    } </span><span class="hljs-keyword">else</span><span class=""> </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(libType == </span><span class="hljs-string">"SHARED"</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L58" href="#L58" data-line-number="58" class="gl-user-select-none gl-shadow-none! file-line-num">
      58
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC58" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(type == cmStateEnums::INTERFACE_LIBRARY)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L59" href="#L59" data-line-number="59" class="gl-user-select-none gl-shadow-none! file-line-num">
      59
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC59" lang="cpp" data-testid="content" class="line"><span class="">        status.</span><span class="hljs-built_in">SetError</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L60" href="#L60" data-line-number="60" class="gl-user-select-none gl-shadow-none! file-line-num">
      60
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC60" lang="cpp" data-testid="content" class="line"><span class="">          </span><span class="hljs-string">"INTERFACE library specified with conflicting SHARED type."</span><span class="">)</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L61" href="#L61" data-line-number="61" class="gl-user-select-none gl-shadow-none! file-line-num">
      61
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC61" lang="cpp" data-testid="content" class="line"><span class="">        </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L62" href="#L62" data-line-number="62" class="gl-user-select-none gl-shadow-none! file-line-num">
      62
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC62" lang="cpp" data-testid="content" class="line"><span class="">      }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L63" href="#L63" data-line-number="63" class="gl-user-select-none gl-shadow-none! file-line-num">
      63
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC63" lang="cpp" data-testid="content" class="line"><span class="">      ++s;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L64" href="#L64" data-line-number="64" class="gl-user-select-none gl-shadow-none! file-line-num">
      64
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC64" lang="cpp" data-testid="content" class="line"><span class="">      type </span><span class="">= cmStateEnums::SHARED_LIBRARY;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L65" href="#L65" data-line-number="65" class="gl-user-select-none gl-shadow-none! file-line-num">
      65
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC65" lang="cpp" data-testid="content" class="line"><span class="">      haveSpecifiedType </span><span class="">= </span><span class="hljs-literal">true</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L66" href="#L66" data-line-number="66" class="gl-user-select-none gl-shadow-none! file-line-num">
      66
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC66" lang="cpp" data-testid="content" class="line"><span class="">    } </span><span class="hljs-keyword">else</span><span class=""> </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(libType == </span><span class="hljs-string">"MODULE"</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L67" href="#L67" data-line-number="67" class="gl-user-select-none gl-shadow-none! file-line-num">
      67
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC67" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(type == cmStateEnums::INTERFACE_LIBRARY)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L68" href="#L68" data-line-number="68" class="gl-user-select-none gl-shadow-none! file-line-num">
      68
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC68" lang="cpp" data-testid="content" class="line"><span class="">        status.</span><span class="hljs-built_in">SetError</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L69" href="#L69" data-line-number="69" class="gl-user-select-none gl-shadow-none! file-line-num">
      69
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC69" lang="cpp" data-testid="content" class="line"><span class="">          </span><span class="hljs-string">"INTERFACE library specified with conflicting MODULE type."</span><span class="">)</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L70" href="#L70" data-line-number="70" class="gl-user-select-none gl-shadow-none! file-line-num">
      70
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC70" lang="cpp" data-testid="content" class="line"><span class="">        </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span></span></code></pre></div></div></div></div> <div><div><div class="gl-display-flex"><div class="gl-display-flex gl-flex-direction-column"><a id="L71" href="#L71" data-line-number="71" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          71
        </a><a id="L72" href="#L72" data-line-number="72" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          72
        </a><a id="L73" href="#L73" data-line-number="73" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          73
        </a><a id="L74" href="#L74" data-line-number="74" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          74
        </a><a id="L75" href="#L75" data-line-number="75" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          75
        </a><a id="L76" href="#L76" data-line-number="76" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          76
        </a><a id="L77" href="#L77" data-line-number="77" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          77
        </a><a id="L78" href="#L78" data-line-number="78" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          78
        </a><a id="L79" href="#L79" data-line-number="79" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          79
        </a><a id="L80" href="#L80" data-line-number="80" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          80
        </a><a id="L81" href="#L81" data-line-number="81" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          81
        </a><a id="L82" href="#L82" data-line-number="82" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          82
        </a><a id="L83" href="#L83" data-line-number="83" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          83
        </a><a id="L84" href="#L84" data-line-number="84" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          84
        </a><a id="L85" href="#L85" data-line-number="85" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          85
        </a><a id="L86" href="#L86" data-line-number="86" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          86
        </a><a id="L87" href="#L87" data-line-number="87" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          87
        </a><a id="L88" href="#L88" data-line-number="88" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          88
        </a><a id="L89" href="#L89" data-line-number="89" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          89
        </a><a id="L90" href="#L90" data-line-number="90" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          90
        </a><a id="L91" href="#L91" data-line-number="91" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          91
        </a><a id="L92" href="#L92" data-line-number="92" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          92
        </a><a id="L93" href="#L93" data-line-number="93" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          93
        </a><a id="L94" href="#L94" data-line-number="94" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          94
        </a><a id="L95" href="#L95" data-line-number="95" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          95
        </a><a id="L96" href="#L96" data-line-number="96" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          96
        </a><a id="L97" href="#L97" data-line-number="97" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          97
        </a><a id="L98" href="#L98" data-line-number="98" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          98
        </a><a id="L99" href="#L99" data-line-number="99" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          99
        </a><a id="L100" href="#L100" data-line-number="100" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          100
        </a><a id="L101" href="#L101" data-line-number="101" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          101
        </a><a id="L102" href="#L102" data-line-number="102" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          102
        </a><a id="L103" href="#L103" data-line-number="103" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          103
        </a><a id="L104" href="#L104" data-line-number="104" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          104
        </a><a id="L105" href="#L105" data-line-number="105" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          105
        </a><a id="L106" href="#L106" data-line-number="106" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          106
        </a><a id="L107" href="#L107" data-line-number="107" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          107
        </a><a id="L108" href="#L108" data-line-number="108" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          108
        </a><a id="L109" href="#L109" data-line-number="109" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          109
        </a><a id="L110" href="#L110" data-line-number="110" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          110
        </a><a id="L111" href="#L111" data-line-number="111" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          111
        </a><a id="L112" href="#L112" data-line-number="112" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          112
        </a><a id="L113" href="#L113" data-line-number="113" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          113
        </a><a id="L114" href="#L114" data-line-number="114" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          114
        </a><a id="L115" href="#L115" data-line-number="115" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          115
        </a><a id="L116" href="#L116" data-line-number="116" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          116
        </a><a id="L117" href="#L117" data-line-number="117" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          117
        </a><a id="L118" href="#L118" data-line-number="118" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          118
        </a><a id="L119" href="#L119" data-line-number="119" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          119
        </a><a id="L120" href="#L120" data-line-number="120" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          120
        </a><a id="L121" href="#L121" data-line-number="121" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          121
        </a><a id="L122" href="#L122" data-line-number="122" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          122
        </a><a id="L123" href="#L123" data-line-number="123" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          123
        </a><a id="L124" href="#L124" data-line-number="124" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          124
        </a><a id="L125" href="#L125" data-line-number="125" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          125
        </a><a id="L126" href="#L126" data-line-number="126" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          126
        </a><a id="L127" href="#L127" data-line-number="127" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          127
        </a><a id="L128" href="#L128" data-line-number="128" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          128
        </a><a id="L129" href="#L129" data-line-number="129" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          129
        </a><a id="L130" href="#L130" data-line-number="130" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          130
        </a><a id="L131" href="#L131" data-line-number="131" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          131
        </a><a id="L132" href="#L132" data-line-number="132" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          132
        </a><a id="L133" href="#L133" data-line-number="133" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          133
        </a><a id="L134" href="#L134" data-line-number="134" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          134
        </a><a id="L135" href="#L135" data-line-number="135" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          135
        </a><a id="L136" href="#L136" data-line-number="136" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          136
        </a><a id="L137" href="#L137" data-line-number="137" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          137
        </a><a id="L138" href="#L138" data-line-number="138" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          138
        </a><a id="L139" href="#L139" data-line-number="139" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          139
        </a><a id="L140" href="#L140" data-line-number="140" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          140
        </a></div> <div data-testid="content" class="gl-white-space-pre-wrap! gl-text-transparent">      }
      ++s;
      type = cmStateEnums::MODULE_LIBRARY;
      haveSpecifiedType = true;
    } else if (libType == "OBJECT") {
      if (type == cmStateEnums::INTERFACE_LIBRARY) {
        status.SetError(
          "INTERFACE library specified with conflicting OBJECT type.");
        return false;
      }
      ++s;
      type = cmStateEnums::OBJECT_LIBRARY;
      haveSpecifiedType = true;
    } else if (libType == "UNKNOWN") {
      if (type == cmStateEnums::INTERFACE_LIBRARY) {
        status.SetError(
          "INTERFACE library specified with conflicting UNKNOWN type.");
        return false;
      }
      ++s;
      type = cmStateEnums::UNKNOWN_LIBRARY;
      haveSpecifiedType = true;
    } else if (libType == "ALIAS") {
      if (type == cmStateEnums::INTERFACE_LIBRARY) {
        status.SetError(
          "INTERFACE library specified with conflicting ALIAS type.");
        return false;
      }
      ++s;
      isAlias = true;
    } else if (libType == "INTERFACE") {
      if (haveSpecifiedType) {
        status.SetError(
          "INTERFACE library specified with conflicting/multiple types.");
        return false;
      }
      if (isAlias) {
        status.SetError(
          "INTERFACE library specified with conflicting ALIAS type.");
        return false;
      }
      ++s;
      type = cmStateEnums::INTERFACE_LIBRARY;
      haveSpecifiedType = true;
    } else if (*s == "EXCLUDE_FROM_ALL") {
      ++s;
      excludeFromAll = true;
    } else if (*s == "IMPORTED") {
      ++s;
      importTarget = true;
    } else if (importTarget &amp;&amp; *s == "GLOBAL") {
      ++s;
      importGlobal = true;
    } else if (type == cmStateEnums::INTERFACE_LIBRARY &amp;&amp; *s == "GLOBAL") {
      status.SetError(
        "GLOBAL option may only be used with IMPORTED libraries.");
      return false;
    } else {
      break;
    }
  }

  if (type == cmStateEnums::INTERFACE_LIBRARY) {
    if (importGlobal &amp;&amp; !importTarget) {
      status.SetError(
        "INTERFACE library specified as GLOBAL, but not as IMPORTED.");
      return false;
    }
  }
</div></div></div></div><div><div><div class="gl-display-flex"><div class="gl-display-flex gl-flex-direction-column"><a id="L141" href="#L141" data-line-number="141" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          141
        </a><a id="L142" href="#L142" data-line-number="142" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          142
        </a><a id="L143" href="#L143" data-line-number="143" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          143
        </a><a id="L144" href="#L144" data-line-number="144" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          144
        </a><a id="L145" href="#L145" data-line-number="145" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          145
        </a><a id="L146" href="#L146" data-line-number="146" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          146
        </a><a id="L147" href="#L147" data-line-number="147" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          147
        </a><a id="L148" href="#L148" data-line-number="148" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          148
        </a><a id="L149" href="#L149" data-line-number="149" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          149
        </a><a id="L150" href="#L150" data-line-number="150" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          150
        </a><a id="L151" href="#L151" data-line-number="151" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          151
        </a><a id="L152" href="#L152" data-line-number="152" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          152
        </a><a id="L153" href="#L153" data-line-number="153" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          153
        </a><a id="L154" href="#L154" data-line-number="154" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          154
        </a><a id="L155" href="#L155" data-line-number="155" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          155
        </a><a id="L156" href="#L156" data-line-number="156" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          156
        </a><a id="L157" href="#L157" data-line-number="157" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          157
        </a><a id="L158" href="#L158" data-line-number="158" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          158
        </a><a id="L159" href="#L159" data-line-number="159" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          159
        </a><a id="L160" href="#L160" data-line-number="160" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          160
        </a><a id="L161" href="#L161" data-line-number="161" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          161
        </a><a id="L162" href="#L162" data-line-number="162" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          162
        </a><a id="L163" href="#L163" data-line-number="163" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          163
        </a><a id="L164" href="#L164" data-line-number="164" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          164
        </a><a id="L165" href="#L165" data-line-number="165" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          165
        </a><a id="L166" href="#L166" data-line-number="166" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          166
        </a><a id="L167" href="#L167" data-line-number="167" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          167
        </a><a id="L168" href="#L168" data-line-number="168" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          168
        </a><a id="L169" href="#L169" data-line-number="169" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          169
        </a><a id="L170" href="#L170" data-line-number="170" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          170
        </a><a id="L171" href="#L171" data-line-number="171" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          171
        </a><a id="L172" href="#L172" data-line-number="172" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          172
        </a><a id="L173" href="#L173" data-line-number="173" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          173
        </a><a id="L174" href="#L174" data-line-number="174" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          174
        </a><a id="L175" href="#L175" data-line-number="175" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          175
        </a><a id="L176" href="#L176" data-line-number="176" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          176
        </a><a id="L177" href="#L177" data-line-number="177" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          177
        </a><a id="L178" href="#L178" data-line-number="178" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          178
        </a><a id="L179" href="#L179" data-line-number="179" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          179
        </a><a id="L180" href="#L180" data-line-number="180" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          180
        </a><a id="L181" href="#L181" data-line-number="181" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          181
        </a><a id="L182" href="#L182" data-line-number="182" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          182
        </a><a id="L183" href="#L183" data-line-number="183" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          183
        </a><a id="L184" href="#L184" data-line-number="184" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          184
        </a><a id="L185" href="#L185" data-line-number="185" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          185
        </a><a id="L186" href="#L186" data-line-number="186" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          186
        </a><a id="L187" href="#L187" data-line-number="187" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          187
        </a><a id="L188" href="#L188" data-line-number="188" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          188
        </a><a id="L189" href="#L189" data-line-number="189" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          189
        </a><a id="L190" href="#L190" data-line-number="190" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          190
        </a><a id="L191" href="#L191" data-line-number="191" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          191
        </a><a id="L192" href="#L192" data-line-number="192" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          192
        </a><a id="L193" href="#L193" data-line-number="193" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          193
        </a><a id="L194" href="#L194" data-line-number="194" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          194
        </a><a id="L195" href="#L195" data-line-number="195" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          195
        </a><a id="L196" href="#L196" data-line-number="196" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          196
        </a><a id="L197" href="#L197" data-line-number="197" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          197
        </a><a id="L198" href="#L198" data-line-number="198" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          198
        </a><a id="L199" href="#L199" data-line-number="199" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          199
        </a><a id="L200" href="#L200" data-line-number="200" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          200
        </a><a id="L201" href="#L201" data-line-number="201" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          201
        </a><a id="L202" href="#L202" data-line-number="202" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          202
        </a><a id="L203" href="#L203" data-line-number="203" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          203
        </a><a id="L204" href="#L204" data-line-number="204" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          204
        </a><a id="L205" href="#L205" data-line-number="205" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          205
        </a><a id="L206" href="#L206" data-line-number="206" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          206
        </a><a id="L207" href="#L207" data-line-number="207" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          207
        </a><a id="L208" href="#L208" data-line-number="208" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          208
        </a><a id="L209" href="#L209" data-line-number="209" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          209
        </a><a id="L210" href="#L210" data-line-number="210" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          210
        </a></div> <div data-testid="content" class="gl-white-space-pre-wrap! gl-text-transparent">  bool nameOk = cmGeneratorExpression::IsValidTargetName(libName) &amp;&amp;
    !cmGlobalGenerator::IsReservedTarget(libName);

  if (nameOk &amp;&amp; !importTarget &amp;&amp; !isAlias) {
    nameOk = libName.find(':') == std::string::npos;
  }
  if (!nameOk &amp;&amp; !mf.CheckCMP0037(libName, type)) {
    return false;
  }

  if (isAlias) {
    if (!cmGeneratorExpression::IsValidTargetName(libName)) {
      status.SetError("Invalid name for ALIAS: " + libName);
      return false;
    }
    if (excludeFromAll) {
      status.SetError("EXCLUDE_FROM_ALL with ALIAS makes no sense.");
      return false;
    }
    if (importTarget || importGlobal) {
      status.SetError("IMPORTED with ALIAS is not allowed.");
      return false;
    }
    if (args.size() != 3) {
      status.SetError("ALIAS requires exactly one target argument.");
      return false;
    }

    if (mf.GetPolicyStatus(cmPolicies::CMP0107) == cmPolicies::NEW) {
      // Make sure the target does not already exist.
      if (mf.FindTargetToUse(libName)) {
        status.SetError(cmStrCat(
          "cannot create ALIAS target \"", libName,
          "\" because another target with the same name already exists."));
        return false;
      }
    }

    std::string const&amp; aliasedName = *s;
    if (mf.IsAlias(aliasedName)) {
      status.SetError(cmStrCat("cannot create ALIAS target \"", libName,
                               "\" because target \"", aliasedName,
                               "\" is itself an ALIAS."));
      return false;
    }
    cmTarget* aliasedTarget = mf.FindTargetToUse(aliasedName, true);
    if (!aliasedTarget) {
      status.SetError(cmStrCat("cannot create ALIAS target \"", libName,
                               "\" because target \"", aliasedName,
                               "\" does not already exist."));
      return false;
    }
    cmStateEnums::TargetType aliasedType = aliasedTarget-&gt;GetType();
    if (aliasedType != cmStateEnums::SHARED_LIBRARY &amp;&amp;
        aliasedType != cmStateEnums::STATIC_LIBRARY &amp;&amp;
        aliasedType != cmStateEnums::MODULE_LIBRARY &amp;&amp;
        aliasedType != cmStateEnums::OBJECT_LIBRARY &amp;&amp;
        aliasedType != cmStateEnums::INTERFACE_LIBRARY &amp;&amp;
        !(aliasedType == cmStateEnums::UNKNOWN_LIBRARY &amp;&amp;
          aliasedTarget-&gt;IsImported())) {
      status.SetError(cmStrCat("cannot create ALIAS target \"", libName,
                               "\" because target \"", aliasedName,
                               "\" is not a library."));
      return false;
    }
    mf.AddAlias(libName, aliasedName,
                !aliasedTarget-&gt;IsImported() ||
                  aliasedTarget-&gt;IsImportedGloballyVisible());
    return true;
  }</div></div></div></div><div><div><div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L211" href="#L211" data-line-number="211" class="gl-user-select-none gl-shadow-none! file-line-num">
      211
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC211" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L212" href="#L212" data-line-number="212" class="gl-user-select-none gl-shadow-none! file-line-num">
      212
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC212" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(importTarget &amp;&amp; excludeFromAll)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L213" href="#L213" data-line-number="213" class="gl-user-select-none gl-shadow-none! file-line-num">
      213
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC213" lang="cpp" data-testid="content" class="line"><span class="">    status.</span><span class="hljs-built_in">SetError</span><span class="">(</span><span class="hljs-string">"excludeFromAll with IMPORTED target makes no sense."</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L214" href="#L214" data-line-number="214" class="gl-user-select-none gl-shadow-none! file-line-num">
      214
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC214" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L215" href="#L215" data-line-number="215" class="gl-user-select-none gl-shadow-none! file-line-num">
      215
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC215" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L216" href="#L216" data-line-number="216" class="gl-user-select-none gl-shadow-none! file-line-num">
      216
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC216" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L217" href="#L217" data-line-number="217" class="gl-user-select-none gl-shadow-none! file-line-num">
      217
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC217" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">/* ideally we</span><span class="hljs-comment"> should check whether </span><span class="hljs-comment">for</span><span class="hljs-comment"> the linker language </span><span class="hljs-comment">of the target</span></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L218" href="#L218" data-line-number="218" class="gl-user-select-none gl-shadow-none! file-line-num">
      218
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC218" lang="cpp" data-testid="content" class="line"><span class="hljs-comment">    CMAKE_${LANG}_CREATE_SHARED_LIBRARY</span><span class="hljs-comment"> is defined and </span><span class="hljs-comment">if not default to</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L219" href="#L219" data-line-number="219" class="gl-user-select-none gl-shadow-none! file-line-num">
      219
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC219" lang="cpp" data-testid="content" class="line"><span class="hljs-comment">    STATIC.</span><span class="hljs-comment"> But at this </span><span class="hljs-comment">point we</span><span class="hljs-comment"> know only the </span><span class="hljs-comment">name of the target, but not</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L220" href="#L220" data-line-number="220" class="gl-user-select-none gl-shadow-none! file-line-num">
      220
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC220" lang="cpp" data-testid="content" class="line"><span class="hljs-comment"></span><span class="hljs-comment">    yet its linker </span><span class="hljs-comment">language. */</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L221" href="#L221" data-line-number="221" class="gl-user-select-none gl-shadow-none! file-line-num">
      221
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC221" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(</span><span class="">(type == cmStateEnums::SHARED_LIBRARY ||</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L222" href="#L222" data-line-number="222" class="gl-user-select-none gl-shadow-none! file-line-num">
      222
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC222" lang="cpp" data-testid="content" class="line"><span class="">       type == cmStateEnums::MODULE_LIBRARY)</span><span class=""> &amp;&amp;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L223" href="#L223" data-line-number="223" class="gl-user-select-none gl-shadow-none! file-line-num">
      223
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC223" lang="cpp" data-testid="content" class="line"><span class="">      !mf.</span><span class="hljs-built_in">GetState</span><span class="">()</span><span class="">-&gt;</span><span class="hljs-built_in">GetGlobalPropertyAsBool</span><span class="">(</span><span class="hljs-string">"TARGET_SUPPORTS_SHARED_LIBS"</span><span class="">)</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L224" href="#L224" data-line-number="224" class="gl-user-select-none gl-shadow-none! file-line-num">
      224
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC224" lang="cpp" data-testid="content" class="line hll"><span class="">    mf.</span><span class="hljs-built_in">IssueMessage</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L225" href="#L225" data-line-number="225" class="gl-user-select-none gl-shadow-none! file-line-num">
      225
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC225" lang="cpp" data-testid="content" class="line hll"><span class="">      MessageType::AUTHOR_WARNING,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L226" href="#L226" data-line-number="226" class="gl-user-select-none gl-shadow-none! file-line-num">
      226
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC226" lang="cpp" data-testid="content" class="line hll"><span class="">      </span><span class="hljs-built_in">cmStrCat</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L227" href="#L227" data-line-number="227" class="gl-user-select-none gl-shadow-none! file-line-num">
      227
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC227" lang="cpp" data-testid="content" class="line hll"><span class="">        </span><span class="hljs-string">"ADD_LIBRARY called with "</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L228" href="#L228" data-line-number="228" class="gl-user-select-none gl-shadow-none! file-line-num">
      228
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC228" lang="cpp" data-testid="content" class="line hll"><span class="">        </span><span class="">(type == cmStateEnums::SHARED_LIBRARY ? </span><span class="hljs-string">"SHARED"</span><span class=""> : </span><span class="hljs-string">"MODULE"</span><span class="">)</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L229" href="#L229" data-line-number="229" class="gl-user-select-none gl-shadow-none! file-line-num">
      229
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC229" lang="cpp" data-testid="content" class="line hll"><span class="">        </span><span class="hljs-string">" option but the target platform does not support dynamic linking. "</span><span class="">,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L230" href="#L230" data-line-number="230" class="gl-user-select-none gl-shadow-none! file-line-num">
      230
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC230" lang="cpp" data-testid="content" class="line hll"><span class="">        </span><span class="hljs-string">"Building a STATIC library instead. This may lead to problems."</span><span class="">)</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L231" href="#L231" data-line-number="231" class="gl-user-select-none gl-shadow-none! file-line-num">
      231
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC231" lang="cpp" data-testid="content" class="line hll"><span class="">    type </span><span class="">= cmStateEnums::STATIC_LIBRARY;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L232" href="#L232" data-line-number="232" class="gl-user-select-none gl-shadow-none! file-line-num">
      232
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC232" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L233" href="#L233" data-line-number="233" class="gl-user-select-none gl-shadow-none! file-line-num">
      233
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC233" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L234" href="#L234" data-line-number="234" class="gl-user-select-none gl-shadow-none! file-line-num">
      234
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC234" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">//</span><span class="hljs-comment"> Handle imported target </span><span class="hljs-comment">creation.</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L235" href="#L235" data-line-number="235" class="gl-user-select-none gl-shadow-none! file-line-num">
      235
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC235" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(importTarget)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L236" href="#L236" data-line-number="236" class="gl-user-select-none gl-shadow-none! file-line-num">
      236
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC236" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-comment"><span class="hljs-comment">// The IMPORTED</span><span class="hljs-comment"> signature requires a </span><span class="hljs-comment">type to be specified explicitly.</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L237" href="#L237" data-line-number="237" class="gl-user-select-none gl-shadow-none! file-line-num">
      237
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC237" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(!haveSpecifiedType)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L238" href="#L238" data-line-number="238" class="gl-user-select-none gl-shadow-none! file-line-num">
      238
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC238" lang="cpp" data-testid="content" class="line"><span class="">      status.</span><span class="hljs-built_in">SetError</span><span class="">(</span><span class="hljs-string">"called with IMPORTED argument but no library type."</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L239" href="#L239" data-line-number="239" class="gl-user-select-none gl-shadow-none! file-line-num">
      239
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC239" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L240" href="#L240" data-line-number="240" class="gl-user-select-none gl-shadow-none! file-line-num">
      240
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC240" lang="cpp" data-testid="content" class="line"><span class="">    }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L241" href="#L241" data-line-number="241" class="gl-user-select-none gl-shadow-none! file-line-num">
      241
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC241" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(type == cmStateEnums::INTERFACE_LIBRARY)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L242" href="#L242" data-line-number="242" class="gl-user-select-none gl-shadow-none! file-line-num">
      242
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC242" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(!cmGeneratorExpression::</span><span class="hljs-built_in">IsValidTargetName</span><span class="">(libName)</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L243" href="#L243" data-line-number="243" class="gl-user-select-none gl-shadow-none! file-line-num">
      243
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC243" lang="cpp" data-testid="content" class="line"><span class="">        status.</span><span class="hljs-built_in">SetError</span><span class="">(</span><span class="hljs-built_in">cmStrCat</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L244" href="#L244" data-line-number="244" class="gl-user-select-none gl-shadow-none! file-line-num">
      244
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC244" lang="cpp" data-testid="content" class="line"><span class="">          </span><span class="hljs-string">"Invalid name for IMPORTED INTERFACE library target: "</span><span class="">, libName)</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L245" href="#L245" data-line-number="245" class="gl-user-select-none gl-shadow-none! file-line-num">
      245
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC245" lang="cpp" data-testid="content" class="line"><span class="">        </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L246" href="#L246" data-line-number="246" class="gl-user-select-none gl-shadow-none! file-line-num">
      246
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC246" lang="cpp" data-testid="content" class="line"><span class="">      }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L247" href="#L247" data-line-number="247" class="gl-user-select-none gl-shadow-none! file-line-num">
      247
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC247" lang="cpp" data-testid="content" class="line"><span class="">    }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L248" href="#L248" data-line-number="248" class="gl-user-select-none gl-shadow-none! file-line-num">
      248
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC248" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L249" href="#L249" data-line-number="249" class="gl-user-select-none gl-shadow-none! file-line-num">
      249
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC249" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-comment"><span class="hljs-comment">//</span><span class="hljs-comment"> Make sure the </span><span class="hljs-comment">target</span><span class="hljs-comment"> does not already </span><span class="hljs-comment">exist.</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L250" href="#L250" data-line-number="250" class="gl-user-select-none gl-shadow-none! file-line-num">
      250
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC250" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(mf.</span><span class="hljs-built_in">FindTargetToUse</span><span class="">(libName)</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L251" href="#L251" data-line-number="251" class="gl-user-select-none gl-shadow-none! file-line-num">
      251
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC251" lang="cpp" data-testid="content" class="line"><span class="">      status.</span><span class="hljs-built_in">SetError</span><span class="">(</span><span class="hljs-built_in">cmStrCat</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L252" href="#L252" data-line-number="252" class="gl-user-select-none gl-shadow-none! file-line-num">
      252
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC252" lang="cpp" data-testid="content" class="line"><span class="">        </span><span class="hljs-string"><span class="hljs-string">"cannot create imported target </span><span class="hljs-string">\"</span><span class="hljs-string">"</span></span><span class="">, libName,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L253" href="#L253" data-line-number="253" class="gl-user-select-none gl-shadow-none! file-line-num">
      253
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC253" lang="cpp" data-testid="content" class="line"><span class="">        </span><span class="hljs-string"><span class="hljs-string">"</span><span class="hljs-string">\"</span><span class="hljs-string"> because another target with the same name already exists."</span></span><span class="">)</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L254" href="#L254" data-line-number="254" class="gl-user-select-none gl-shadow-none! file-line-num">
      254
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC254" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L255" href="#L255" data-line-number="255" class="gl-user-select-none gl-shadow-none! file-line-num">
      255
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC255" lang="cpp" data-testid="content" class="line"><span class="">    }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L256" href="#L256" data-line-number="256" class="gl-user-select-none gl-shadow-none! file-line-num">
      256
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC256" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L257" href="#L257" data-line-number="257" class="gl-user-select-none gl-shadow-none! file-line-num">
      257
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC257" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-comment"><span class="hljs-comment">//</span><span class="hljs-comment"> Create the imported </span><span class="hljs-comment">target.</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L258" href="#L258" data-line-number="258" class="gl-user-select-none gl-shadow-none! file-line-num">
      258
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC258" lang="cpp" data-testid="content" class="line"><span class="">    mf.</span><span class="hljs-built_in">AddImportedTarget</span><span class="">(libName, type, importGlobal)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L259" href="#L259" data-line-number="259" class="gl-user-select-none gl-shadow-none! file-line-num">
      259
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC259" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">true</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L260" href="#L260" data-line-number="260" class="gl-user-select-none gl-shadow-none! file-line-num">
      260
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC260" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L261" href="#L261" data-line-number="261" class="gl-user-select-none gl-shadow-none! file-line-num">
      261
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC261" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L262" href="#L262" data-line-number="262" class="gl-user-select-none gl-shadow-none! file-line-num">
      262
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC262" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment"><span class="hljs-comment">// A</span><span class="hljs-comment"> non-imported target may </span><span class="hljs-comment">not have UNKNOWN type.</span></span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L263" href="#L263" data-line-number="263" class="gl-user-select-none gl-shadow-none! file-line-num">
      263
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC263" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(type == cmStateEnums::UNKNOWN_LIBRARY)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L264" href="#L264" data-line-number="264" class="gl-user-select-none gl-shadow-none! file-line-num">
      264
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC264" lang="cpp" data-testid="content" class="line"><span class="">    mf.</span><span class="hljs-built_in">IssueMessage</span><span class="">(</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L265" href="#L265" data-line-number="265" class="gl-user-select-none gl-shadow-none! file-line-num">
      265
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC265" lang="cpp" data-testid="content" class="line"><span class="">      MessageType::FATAL_ERROR,</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L266" href="#L266" data-line-number="266" class="gl-user-select-none gl-shadow-none! file-line-num">
      266
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC266" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-string">"The UNKNOWN library type may be used only for IMPORTED libraries."</span><span class="">)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L267" href="#L267" data-line-number="267" class="gl-user-select-none gl-shadow-none! file-line-num">
      267
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC267" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">true</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L268" href="#L268" data-line-number="268" class="gl-user-select-none gl-shadow-none! file-line-num">
      268
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC268" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L269" href="#L269" data-line-number="269" class="gl-user-select-none gl-shadow-none! file-line-num">
      269
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC269" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L270" href="#L270" data-line-number="270" class="gl-user-select-none gl-shadow-none! file-line-num">
      270
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC270" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-comment">// Enforce name uniqueness.</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L271" href="#L271" data-line-number="271" class="gl-user-select-none gl-shadow-none! file-line-num">
      271
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC271" lang="cpp" data-testid="content" class="line"><span class="">  {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L272" href="#L272" data-line-number="272" class="gl-user-select-none gl-shadow-none! file-line-num">
      272
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC272" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="">std::</span><span class="">string msg;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L273" href="#L273" data-line-number="273" class="gl-user-select-none gl-shadow-none! file-line-num">
      273
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC273" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(!mf.</span><span class="hljs-built_in">EnforceUniqueName</span><span class="">(libName, msg)</span><span class="">)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L274" href="#L274" data-line-number="274" class="gl-user-select-none gl-shadow-none! file-line-num">
      274
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC274" lang="cpp" data-testid="content" class="line"><span class="">      status.</span><span class="hljs-built_in">SetError</span><span class="">(msg)</span><span class="">;</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L275" href="#L275" data-line-number="275" class="gl-user-select-none gl-shadow-none! file-line-num">
      275
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC275" lang="cpp" data-testid="content" class="line"><span class="">      </span><span class="hljs-keyword">return</span><span class=""> </span><span class="hljs-literal">false</span><span class="">;</span><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L276" href="#L276" data-line-number="276" class="gl-user-select-none gl-shadow-none! file-line-num">
      276
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC276" lang="cpp" data-testid="content" class="line"><span class="">    }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L277" href="#L277" data-line-number="277" class="gl-user-select-none gl-shadow-none! file-line-num">
      277
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC277" lang="cpp" data-testid="content" class="line"><span class="">  }</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L278" href="#L278" data-line-number="278" class="gl-user-select-none gl-shadow-none! file-line-num">
      278
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC278" lang="cpp" data-testid="content" class="line"><span class=""></span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L279" href="#L279" data-line-number="279" class="gl-user-select-none gl-shadow-none! file-line-num">
      279
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC279" lang="cpp" data-testid="content" class="line"><span class="">  </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(type == cmStateEnums::INTERFACE_LIBRARY)</span><span class=""> {</span></span></code></pre></div><div class="gl-display-flex"><div class="gl-p-0! gl-absolute gl-z-index-3 diff-line-num gl-border-r gl-display-flex line-links line-numbers"><!----> <a id="L280" href="#L280" data-line-number="280" class="gl-user-select-none gl-shadow-none! file-line-num">
      280
    </a></div> <pre class="gl-p-0! gl-w-full gl-overflow-visible! gl-border-none! code highlight gl-line-height-0"><code><span id="LC280" lang="cpp" data-testid="content" class="line"><span class="">    </span><span class="hljs-keyword">if</span><span class=""> </span><span class="">(!cmGeneratorExpression::</span><span class="hljs-built_in">IsValidTargetName</span><span class="">(libName)</span><span class=""> ||</span></span></code></pre></div></div></div></div><div><div><div class="gl-display-flex"><div class="gl-display-flex gl-flex-direction-column"><a id="L281" href="#L281" data-line-number="281" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          281
        </a><a id="L282" href="#L282" data-line-number="282" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          282
        </a><a id="L283" href="#L283" data-line-number="283" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          283
        </a><a id="L284" href="#L284" data-line-number="284" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          284
        </a><a id="L285" href="#L285" data-line-number="285" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          285
        </a><a id="L286" href="#L286" data-line-number="286" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          286
        </a><a id="L287" href="#L287" data-line-number="287" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          287
        </a><a id="L288" href="#L288" data-line-number="288" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          288
        </a><a id="L289" href="#L289" data-line-number="289" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          289
        </a><a id="L290" href="#L290" data-line-number="290" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          290
        </a><a id="L291" href="#L291" data-line-number="291" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          291
        </a><a id="L292" href="#L292" data-line-number="292" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          292
        </a><a id="L293" href="#L293" data-line-number="293" data-testid="line-number" class="gl-ml-5 gl-text-transparent">
          293
        </a></div> <div data-testid="content" class="gl-white-space-pre-wrap! gl-text-transparent">        libName.find("::") != std::string::npos) {
      status.SetError(
        cmStrCat("Invalid name for INTERFACE library target: ", libName));
      return false;
    }
  }

  std::vector&lt;std::string&gt; srcs(s, args.end());
  mf.AddLibrary(libName, type, srcs, excludeFromAll);

  return true;
}
</div></div></div></div></div> <!----></div></div>
</div>

</div>

<script>
//<![CDATA[
  window.gl = window.gl || {};
  window.gl.webIDEPath = '/-/ide/project/cmake/cmake/edit/v3.21.1/-/Source/cmAddLibraryCommand.cxx'


//]]>
</script>

</main>
</div>


</div>
</div>
<div class="top-nav-responsive layout-page content-wrapper-margin">
<div class="cloak-startup">
<div><div data-testid="mobile-overlay" class="mobile-overlay"></div> <div><div class="gl-h-full gl-w-full"><div><header class="gl-display-flex gl-align-items-center gl-py-4 gl-pl-4"><h1 class="gl-m-0 gl-font-size-h2 gl-reset-color gl-mr-auto">Menu</h1> <a aria-label="Search" data-qa-selector="menu_item_link" data-qa-title="Search" href="/search?project_id=541" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-ml-3 btn-default btn-md gl-button btn-default-tertiary"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="search-icon" role="img" aria-hidden="true" class="gl-icon s16"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#search"></use></svg> <!----></span></span></a> <!----></header> <div class="gl-display-flex gl-align-items-stretch gl-flex-direction-column gl-h-full"><div data-testid="menu-section" class=""><strong data-testid="menu-header" class="gl-px-4 gl-py-2 gl-text-gray-900 gl-display-block">
        Explore
      </strong><a aria-label="Projects" data-qa-selector="menu_item_link" data-qa-title="Projects" href="/explore" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="project-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#project"></use></svg> 
      Projects
      <!----></span></span></a><a aria-label="Groups" data-qa-selector="menu_item_link" data-qa-title="Groups" href="/explore/groups" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="group-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#group"></use></svg> 
      Groups
      <!----></span></span></a><a aria-label="Snippets" data-qa-selector="menu_item_link" data-qa-title="Snippets" href="/explore/snippets" class="btn top-nav-menu-item gl-display-block gl-pr-3! gl-w-full btn-default btn-md gl-button btn-default-tertiary gl-mt-1" data-testid="menu-item"><!----> <!---->  <span class="gl-button-text"><span class="gl-display-flex"><svg data-testid="snippet-icon" role="img" aria-hidden="true" class="gl-icon s16 gl-mr-3!"><use href="/assets/icons-7dd47f0bd545c11d13acc0f4abc2ce8fac4abbbef0965fde375eb13c62e7f9fd.svg#snippet"></use></svg> 
      Snippets
      <!----></span></span></a></div></div></div></div></div></div>
</div>
</div>



<script>
//<![CDATA[
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img.lazy').forEach(img => {
    img.loading = 'lazy';
    let imgUrl = img.dataset.src;
    // Only adding width + height for avatars for now
    if (imgUrl.indexOf('/avatar/') > -1 && imgUrl.indexOf('?') === -1) {
      const targetWidth = img.getAttribute('width') || img.width;
      imgUrl += `?width=${targetWidth}`;
    }
    img.src = imgUrl;
    img.removeAttribute('data-src');
    img.classList.remove('lazy');
    img.classList.add('js-lazy-loaded', 'qa-js-lazy-loaded');
  });
}

//]]>
</script>
<script>
//<![CDATA[
gl = window.gl || {};
gl.experiments = {};


//]]>
</script>




<div></div><div></div></body></html>