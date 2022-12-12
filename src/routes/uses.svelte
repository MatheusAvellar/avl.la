<script>
  import T2 from "../components/T2.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
  <title>/uses – Coisas que eu uso | Matheus Avellar</title>
</svelte:head>

<main>
  <section>
    <T2> Programação </T2>
    <article>
      <h3> Editor de Texto </h3>
      <p> <a href="https://www.sublimetext.com/3">Sublime Text 3</a>
        – melhor que o VS Code
      </p>
      <p> Tema <a href="https://github.com/Briles/gruvbox">Gruvbox Dark</a>
        – é um mimo
      </p>
      <p> Fonte <a href="https://typeof.net/Iosevka/">Iosevka</a> (com ligaturas) –
        antes disso, <a href="https://github.com/tonsky/FiraCode">Fira Code</a> e, antes ainda,
        <a href="http://terminus-font.sourceforge.net/">Terminus</a>
        <br>
        <span style="color:#bbb;font-size:.65em">2 <em>ESPAÇOS</em>, não tabs!</span>
      </p>
    </article>
  </section>
  <section>
    <T2> Pessoal </T2>
    <article>
      <h3> Navegador </h3>
      <p> <a href="https://www.google.com/chrome/beta/">Chrome Beta</a>
        – porque eu sou hipster
      </p>
      <p> (anteriormente <a href="https://www.google.com/chrome/canary/">Chrome Canary</a>, porque
        eu era ainda mais hipster, mas a instabilidade atrapalhava demais
        minha vida)
      </p>
    </article>
    <article>
      <h3> Gerenciamento de Contas </h3>
      <p> <a href="https://bitwarden.com/">Bitwarden</a>
        – password manager open-source e 100% de graça :)
      </p>
      <p> <a href="https://authy.com/">Authy</a>
        – 2FA com suporte a múltiplos dispositivos, feature que me fez migrar do
        Google Authenticator para ele
      </p>
    </article>
  </section>
  <section>
    <T2> Hardware </T2>
    <article>
      <h3> Celular </h3>
      <p> <a href="https://store.google.com/us/product/pixel_6">Google Pixel 6</a>
        – o preço abaixou bastante quando lançou o 7, então valeu a pena
      </p>
    </article>
    <article>
      <h3> Mesa Digitalizadora </h3>
      <p> <a href="https://www.wacom.com/pt-br/products/one-by-wacom">Wacom One</a>
        (CTL-472) – não é a melhor do mundo, mas estava na promoção, e acho que
        valeu o preço
      </p>
    </article>
  </section>
    <T2> Misc. </T2>
    <article>
      <h3> Software </h3>
      <p> <a href="https://github.com/microsoft/PowerToys">Microsoft PowerToys</a> –
        só o Power Rename e o Image Resizer já fazem valer a instalação
      </p>
      <p> <a href="https://github.com/samhocevar/wincompose">WinCompose</a> –
        incrivelmente útil para escrever símbolos rapidamente (letras gregas,
        —, →, ×, etc)
      </p>
      <p> <a href="https://getsharex.com/">ShareX</a> –
        melhor programa para tirar prints da tela que existe
      </p>
      <p> <a href="https://freefilesync.org/">FreeFileSync</a> –
        programa ótimo para facilitar backups
      </p>
    </article>
    <article>
      <h3> Extensões para o Navegador </h3>
      <p> <a href="https://chrome.google.com/webstore/detail/aomidfkchockcldhbkggjokdkkebmdll">Redirect Path</a> –
        explicita redirecionamentos de páginas, headers HTTP, status
      </p>
      <p> <a href="https://chrome.google.com/webstore/detail/jghecgabfgfdldnmbfkhmffcabddioke">Volume Master</a> –
        permite o aumento do volume de uma aba para até 600%
      </p>
      <p> <a href="https://chrome.google.com/webstore/detail/amoldiondpmjdnllknhklocndiibkcoe">Twemex</a> –
        aumenta a funcionalidade da barra lateral do Twitter Web
      </p>
      <p> <a href="https://gist.github.com/MatheusAvellar/4655d5b21c5cdc91e6edfff0aed13003">twitter-alt.css</a> –
        Código CSS, adaptado por mim, para permitir a visualização de alt text no Twitter Web
      </p>
    </article>
    <article>
      <h3> Outros </h3>
      <p>
        <a href="http://www.michieldb.nl/other/cursors/">Posy's Cursor Black</a>
        – um redesign do cursor padrão do Windows 10
      </p>
    </article>
  <section>
  </section>
</main>
<Footer/>

<style>
article {
  padding-left: 1rem;
  margin: 1rem 0;
}
article + article {
  margin-top: 1rem;
}
h3 {
  font-size: 1.2rem;
}
</style>