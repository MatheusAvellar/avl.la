import * as sapper from "@sapper/app";

sapper.start({
  target: document.body
}).then(() => {
  setTimeout(() => {
    sapper.prefetchRoutes(["/", "/projetos", "/uses", "/academic"]);
  }, 500);
});;