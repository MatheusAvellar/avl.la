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
      <p> <a rel="noopener noreferrer"
        href="https://www.sublimetext.com/3">Sublime Text 3</a>
        – melhor que o VS Code
      </p>
      <p> Tema <a rel="noopener noreferrer"
        href="https://github.com/Briles/gruvbox">Gruvbox Dark</a>
        – é um mimo
      </p>
      <p> Fonte <a rel="noopener noreferrer"
        href="https://typeof.net/Iosevka/">Iosevka</a> (com ligaturas) –
        antes disso, <a href="https://github.com/tonsky/FiraCode"
        rel="noopener noreferrer">Fira Code</a> e, antes ainda,
        <a href="http://terminus-font.sourceforge.net/"
        rel="noopener noreferrer">Terminus</a>
        <br>
        <span style="color:#bbb;font-size:.65em">
          2 <em>ESPAÇOS</em>, não tabs!
        </span>
      </p>
    </article>
  </section>
  <section>
    <T2> Pessoal </T2>
    <article>
      <h3> Navegador </h3>
      <p> <a rel="noopener noreferrer"
        href="https://www.google.com/chrome/canary/">Chrome Canary</a>
        – porque eu sou hipster
      </p>
    </article>
    <article>
      <h3> Password Manager </h3>
      <p> <a rel="noopener noreferrer"
        href="https://bitwarden.com/">Bitwarden</a>
        – open-source e 100% de graça :)
      </p>
    </article>
  </section>
  <section>
    <T2> Hardware </T2>
    <article>
      <h3> Celular </h3>
      <p> <a rel="noopener noreferrer"
        href="https://www.mi.com/global/mi-a1">Xiaomi Mi A1</a>
        – bom custo-benefício, Android One, tudo de bom
      </p>
    </article>
    <article>
      <h3> Mesa Digitalizadora </h3>
      <p> <a rel="noopener noreferrer"
        href="https://www.wacom.com/pt-br/products/one-by-wacom">Wacom One</a>
        (CTL-472) – não é a melhor do mundo, mas acho que valeu o preço
      </p>
    </article>
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