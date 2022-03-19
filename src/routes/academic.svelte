<script>
  import T2 from "../components/T2.svelte";
  import Hr from "../components/Hr.svelte";
  import Footer from "../components/Footer.svelte";
</script>

<svelte:head>
  <title>Acadêmico | Matheus Avellar</title>
</svelte:head>

<main>
  <section>
    <T2> Trabalhos </T2>
    <article>
      <h3 id="2022tcc"> 2022 – Trabalho de Conclusão de Curso </h3>
      <p class="description">
        Desenvolvimento de prova de conceito de uma plataforma de análise de
        qualidade de dados para conjuntos de dados arbitrários. Ferramenta
        feita com uso de
        <a href="https://svelte.dev/">Svelte</a>,
        <a href="https://nodejs.org/">NodeJS</a> e
        <a href="https://sqlite.org/">SQLite</a>.
        Trabalho defendido e aprovado em 11/mar/2022.
      </p>
      <p>
        <a href="/files/matheusavellar-tcc-monografia.pdf">Monografia</a> (1.19&nbsp;MB)
      </p>
      <p>
        <a href="/files/matheusavellar-tcc-slides.pdf">Apresentação</a> (4.15&nbsp;MB)
      </p>
      <fieldset>
        <legend>Citação</legend>
        <cite>
          BARROS, Matheus Avellar. <b>Desenvolvimento de uma plataforma de qualidade
          de dados agnóstica a dados</b>. Orientador: Geraldo Zimbrão da Silva.
          2022. 46 f. Trabalho de Conclusão de Curso (Bacharelado em Ciência da
          Computação) – Universidade Federal do Rio de Janeiro, Rio de Janeiro,
          2022.

        </cite>
      </fieldset>
    </article>
    <article>
      <h3 id="2019ic"> 2019 – Iniciação Científica </h3>
      <p class="description">
        Projeto de desenvolvimento de um quiz, em <a href="https://svelte.dev/">Svelte</a>,
        com o tema de Economia Circular. Apresentado na Jornada de Iniciação
        Científica (JIC) 2019.
      </p>
      <p>
        <a href="/files/matheusavellar-paper-jic.pdf">Paper</a> (586&nbsp;KB)
      </p>
      <p>
        <a href="/files/matheusavellar-certificado-jic.pdf">Certificado</a>* (889&nbsp;KB)
      </p>
      <p>
        <small>* Com nome digitado incorretamente, infelizmente</small>
      </p>
      <fieldset>
        <legend>Citação</legend>
        <cite>
          BARROS, M. A.; XAVIER, L. H. S. M. Development of a quiz on circular
          economy. In: Anais da Jornada de Iniciação Científica, 27. Rio de
          Janeiro: CETEM/MCTIC, 2019. Disponível em: <a href="http://mineralis.cetem.gov.br/handle/cetem/2271">http://mineralis.cetem.gov.br/handle/cetem/2271</a>
        </cite>
      </fieldset>
    </article>
  </section>
  <Hr/>
  <section>
    <T2> Extras </T2>
    <article>
      <h3> Monitoria de Computação </h3>
      <p class="description">
        Fui oficialmente monitor da disciplina de Computação I no curso de
        Ciência da Computação na UFRJ do primeiro semestre de 2020 ao segundo
        semestre de 2021, e extraoficialmente no primeiro semestre de 2022.
      </p>
      <p>
        <a href="/files/matheusavellar-declaracao-monitoria-2020.pdf">Declaração</a> (2020)<br>
        <a href="/files/matheusavellar-declaracao-monitoria-2021.1.pdf">Declaração</a> (2021.1)
      </p>
    </article>
    <article>
      <h3> GRIS </h3>
      <p class="description">
        Integrante do Grupo de Respostas à<sup>[sic]</sup> Incidentes de Segurança
        (GRIS) de janeiro/2018 a janeiro/2019.
      </p>
      <p>
        <a href="/files/matheusavellar-certificado-gris.pdf">Certificado</a>
      </p>
    </article>
  </section>
  <Hr/>
  <section>
    <T2> Links </T2>
    <article>
      <h3> Lattes </h3>
      <p>
        <a title="Lattes"
           class="icon-link"
           href="http://lattes.cnpq.br/5654545419711746"
           style="background-image:url(data:image/png;base64,R0lGODlhEQAQAPcAAP////7+/v///v7+/f79+v38/fz8+/v7+f//q/r59vj39vj49vn6yPr45P//d//9iv/8cv/1pv70nPXtzv/vhOvr6f/tifnn2//tfffqo+nm9vntdv/pgd3n6fHqhOrf6evgxObivfnkbv/gfv7hbt/e1fbmP+PfpP7dZN/czerVmtzWvt3VoNvQxN/UiOjPmtPVmdnPstfPtNrTgNDPx/PRR8zPxvHNVtTSfdzKqufSPerMZu/NRe/KPujJU9LGpdvEqO7KM9fHc+zHMcrEvM3CsMHEt8zCoby+19TAgNPBfMDBsMe/l7vBn9a/XcbDUN+9MMK4n8G5h8a3gMy4WNKzdLyypsO2cL+yl7e3crOzl7exm7ezgtGyOrivlrSvo7ixe7qxc7mvisKnpK2unLGqr7eqlb6vV6yroKyqnLaphcGpZL2oecSnOaWpiLykcMSkX8OkU7CijZSqgqWjlrehX7ebl7ufT6eckK6fYKCcnayeYaSbg6SbiJmejLqbOrCZVqaWm8GZG6CWiq+YVLOZH6iTZ7yTKZ2XSZqQhrKTIbOSMJ6TSqKULqCUNaGSK6mREZeOWKuLOJ+KQ5OOL6iHHp2FR5+EMoiFVpN/EJ98EH93ipl0Uop1VoF3UJN0HI9yMox1H4NyPHV2P3lsen1vQ4NndoJxD3l0CHJphXZrTYZlVX5nWXVsQ3dikIRrDXlsFnRtCGtqNXZjX2ppL3xiNXZhOU1jgm9dPG9bO29dJW9dG21WLl9WTGtWFXNUAXZSBmlTGGFRDltMQGVHDmJCAE0/QkY6gz47dlo9AkFAHEg3ZFY5ADE6a080PUU7G0UxOjMyOTUyFTotPkQoPC8wKTcsKzYoOTQoSS0nQzokLB4eSywXLSwZJB4aGA8CKwAAOAAAIwMAGQAACgAABwAAAwAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH5BAQUAP8ALAAAAAARABAAAAj/AAEIDECDDhorX8jMcdOCgMCHANL46aDhw4UJDGBEAtMAYh9PJZCU+ZFBQgQEQmCFEWjAS7A8gVypeeAAAgYOFtqcijEAgC5RuLSZUuEBx4wNJG7wgGQJgBZhhqCdW/WiVLRqlEQcEgTlU45RsRhhK8fKDjdw4aS5mPQrSKU3tFAhymZu1phu38QpO6GK2RBFhGq9WmNs3DQlf4j5epLFW7IeiwBxAhbH1rlzj0ygGEHlWTlQNTJNAVJM0h1ewxzp8AHHGTlqVbqECgGg1S4nSczw6ZTL2rZrbHZoqgMggA1Zja70WnYMWbNbTSgUugRCgMAlmMQkIpVqkx4jLM7sH1kBEUAFIngGyYlyhIkULinKCyygYEGRLVhkJDgAMSAAOw==)">
            lattes.cnpq.br/5654545419711746
        </a>
      </p>
    </article>
    <article>
      <h3> ORCID iD </h3>
      <p>
        <a id="orcid" title="ORCID"
           class="icon-link"
           itemprop="sameAs"
           content="https://orcid.org/0000-0003-2810-8710"
           href="https://orcid.org/0000-0003-2810-8710"
           target="orcid.widget"
           style="background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAALVBMVEVHcEymzjmmzjmmzjmmzjmmzjmmzjn///+SwCnT55y82mus0UXe7bXj8MH0+ebg+QDqAAAABnRSTlMAIL9gz+/edokRAAAAYklEQVQI12NgYDBKS1NmAAKRNCBwZGBgDKtsS0tLFWBgSQMx0hwYzNI62tK2pSUzqKVVtpfXbktiSAMy2tYdS4MwssqgjLQyJBE1iJokoHawrmSggWDgALQCRAOtgFsKcwYACXguQwgn0jwAAAAASUVORK5CYII=)">
          orcid.org/0000-0003-2810-8710
        </a>
      </p>
    </article>
  </section>
</main>
<Footer/>

<style>
.icon-link {
  background-repeat: no-repeat;
  background-size: 16px;
  background-position: 0 center;
  padding-left: 25px;
}
.description {
  margin-bottom: .5em;
}
article {
  padding-left: 1rem;
  margin: 1rem 0;
}
article + article {
  margin-top: 2rem;
}
h3 {
  margin-bottom: .5rem;
  font-size: 1.3rem;
}
a[href$=".pdf"] {
  background-size: 24px;
  padding-left: 24px;
  background-position: 0 -3px;
  background-repeat: no-repeat;
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYBAMAAAASWSDLAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAkUExURUdwTGpqamhoaGlpaWZmZmlpaWlpaWlpaWlpaWlpaWlpaWlpac/vUjUAAAALdFJOUwCA44ck3Eh3S8S7YtfOCgAAAFRJREFUGNNjYCALNO0GAzUwRxvC2QTm7IYCApyNDK4CLIEM0hAOO7NAgSH7agiHmVlggyDzbLiyDYIwZdy7BQwMuXfDOSyB3LtJsRTFoUnIXiAZAACWmERvB+tIYwAAAABJRU5ErkJggg==);
}

fieldset {
  margin-top: 1em;
  border: 1px solid #acacac;
  border: 1px solid var(--hard-highlight, #acacac);
  border-radius: 3px;
}
legend {
  text-transform: uppercase;
  font-size: 0.8rem;
  color: #acacac;
  color: var(--hard-highlight, #acacac);
  user-select: none;
  padding: 0 .5rem;
}
cite {
  font-style: normal;
}
cite > b {
  font-weight: 500;
}
sup {
  color: #acacac;
}
</style>