<script>
  import T2 from "../components/T2.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
  <title>Projetos | Matheus Avellar</title>
</svelte:head>

<main>
  <section>
    <T2> Projetos </T2>
    <article>
      <figure style="background-image:url(/preview/lab.png);background-position-y:-70px"></figure>
      <h3> avellab </h3>
      <p>
        Projetos experimentais que eu faço no meu tempo livre. Pode ser
        considerado um portfólio!
      </p>
      <article class="links">
        <p>
          <svg class="icon"><use href="#world"/></svg>
          <a href="https://lab.avl.la/">lab.avl.la</a>
        </p>
      </article>
    </article>
    <article>
      <figure style="background-image:url(/preview/troca-grana.png)"></figure>
      <h3> Troca Grana </h3>
      <p>
        Pequeno jogo infantil para crianças aprenderem e treinarem a somar
        valores presentes em cédulas do real. Foi mencionado no <a href="https://www.cp2.g12.br/blog/labtijuca1/2019/11/21/sistema-monetario/"
        rel="noopener noreferrer">blog do Colégio Pedro II</a>.
      </p>
      <article class="links">
        <p>
          <svg class="icon"><use href="#world"/></svg>
          <a href="https://avellar.ml/trocagrana/">avellar.ml/trocagrana</a>
        </p>
      </article>
    </article>
    <article>
      <figure style="background-image:url(/preview/o-amendoim.png)"></figure>
      <h3> O Amendoim </h3>
      <p>
        Blogzinho em que eu faço pesquisas e escrevo sobre coisas que eu
        descubro.
      </p>
      <article class="links">
        <p>
          <svg class="icon"><use href="#world"/></svg>
          <a href="https://o.amendo.im/">o.amendo.im</a>
        </p>
      </article>
    </article>
    <article>
      <figure style="background-image:url(/preview/amendoim.png)"></figure>
      <h3> amendo.im </h3>
      <p>
        Site inspirado no famoso <a href="http://pudim.com.br/"
        rel="noopener noreferrer">pudim.com.br</a>, porém com temática de
        amendoim.
      </p>
      <article class="links">
        <p>
          <svg class="icon"><use href="#world"/></svg>
          <a href="https://amendo.im/">amendo.im</a>
        </p>
      </article>
    </article>
  </section>
  <div hidden>
    <svg>
      <path id="world" d="M17.9,17.39C17.64,16.59 16.89,16 16,16H15V13A1,1 0 0,0 14,12H8V10H10A1,1 0 0,0 11,9V7H13A2,2 0 0,0 15,5V4.59C17.93,5.77 20,8.64 20,12C20,14.08 19.2,15.97 17.9,17.39M11,19.93C7.05,19.44 4,16.08 4,12C4,11.38 4.08,10.78 4.21,10.21L9,15V16A2,2 0 0,0 11,18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z" />
      <path id="code" d="M12.89,3L14.85,3.4L11.11,21L9.15,20.6L12.89,3M19.59,12L16,8.41V5.58L22.42,12L16,18.41V15.58L19.59,12M1.58,12L8,5.58V8.41L4.41,12L8,15.58V18.41L1.58,12Z" />
    </svg>
  </div>
</main>
<Footer/>

<style>
article {
  padding-left: 1rem;
  margin: 2.5rem 0;
}
article + article {
  margin-top: 1rem;
}
h3 {
  font-size: 1.2rem;
}
strong {
  font-weight: 500;
}
figure {
  background-size: cover;
  height: 7.5rem;
  width: 20rem;
  border: 2px solid #ddd;
  border-radius: 4px;
  margin: 0 0 0.5rem -2px;
  padding: 0;
  background-position: center;
  background-repeat: no-repeat;

  background-color: #f2f2f2;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='40' height='40' viewBox='0 0 40 40'%3E%3Cg fill-rule='evenodd'%3E%3Cg fill='%23dfdfdf' fill-opacity='1'%3E%3Cpath d='M0 38.59l2.83-2.83 1.41 1.41L1.41 40H0v-1.41zM0 1.4l2.83 2.83 1.41-1.41L1.41 0H0v1.41zM38.59 40l-2.83-2.83 1.41-1.41L40 38.59V40h-1.41zM40 1.41l-2.83 2.83-1.41-1.41L38.59 0H40v1.41zM20 18.6l2.83-2.83 1.41 1.41L21.41 20l2.83 2.83-1.41 1.41L20 21.41l-2.83 2.83-1.41-1.41L18.59 20l-2.83-2.83 1.41-1.41L20 18.59z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.links {
  margin-top: 1rem;
  padding: 0;
}
.links a[href] {
  vertical-align: middle;
}
.icon {
  fill: #444;
  fill: var(--black);
  height: 24px;
  width: 24px;
  vertical-align: middle;
  box-sizing: border-box;
}
</style>