<script>
  import Nav from "../components/Nav.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
  <title>Matheus Avellar</title>
</svelte:head>

<main>
  <section>
    <article class="profile">
      <a href="/eu/photo-500x500.jpg">
        <picture>
          <source media="(max-width: 600px)" srcset="/eu/photo-100x100.jpg">
          <img src="/eu/photo-200x200.jpg" alt="Fotografia de mim em um campo florido.">
        </picture>
      </a>
    </article>
    <article>
      <p> Olá! </p>
      <p> Eu sou o Matheus Avellar, e esse é um dos meus cantinhos na internet! </p>
      <p>
        Se é o que você procura, veja aqui meu
        <a href="/files/cv-matheusavellar-pt.pdf">currículo</a>.
      </p>
    </article>
  </section>
  <section>
    <p>
      Esse site está eternamente em construção. Algumas coisas talvez mudem sem
      aviso!
    </p>
  </section>
</main>
<Footer/>

<style>
section {
  margin-bottom: 2rem;
}
.profile {
  float: right;
  margin: 0 0 1rem 1rem;
}
.profile img {
  border-radius: 8px;
  box-shadow: var(--shadow-elevation-medium);
}
</style>