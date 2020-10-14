<script>
  import Nav from "../components/Nav.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
  <title>Matheus Avellar</title>
</svelte:head>

<main>
  <section class="column">
    <p> Olá! </p>
    <p> Bem vindo a um dos meus cantinhos na internet! </p>
    <p>
      Se é o que você procura, veja aqui meu
      <a href="/files/cv-matheusavellar-pt.pdf">currículo</a>.
    </p>
    <p>
      Para dar uma olhada em alguns de meus projetos, visite
      <a href="/projetos">/projetos</a>.
    </p>
    <p>
      Para ver minhas realizações acadêmicas, <a href="/academic">/academic</a>.
    </p>
    <p>
      Se você quer bisbilhotar o que eu uso, <a href="/uses">/uses</a>.
    </p>
    <p>
      <br>
      De qualquer forma, espero que goste!
    </p>
  </section>
  <section>
    <p>
      Esse site ainda está em construção. Algumas coisas talvez mudem sem aviso!
    </p>
  </section>
</main>
<Footer/>

<style>
section {
  margin-bottom: 2rem;
}
.column {
  columns: 2;
  column-rule: 1px solid var(--black);
  column-gap: 3rem;
}
@media screen and (max-width: 800px) {
  .column {
    columns: unset;
  }
  .column p+p {
    margin-top: .5rem;
  }
}
</style>