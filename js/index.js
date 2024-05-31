const teamsData = [
    {
      "name": "Argentinos",
      "image": "1-q08j6Xb9MFCyF0ui4ef1rt5LvBp38ge",
      "id": "argentinos",
      "vs": "platense",
      "description": "Jugaron 77 veces. Argentinos ganó 21 veces. Platense ganó 26 veces. Empataron 30 veces. Platense lleva una diferencia de 5 partidos."
    },
    {
      "name": "Atletico Tucuman",
      "image": "1NIGE5aORycKimhVB6zV3N6dcpSlFycjb",
      "id": "atleticotucuman",
      "vs": "sanmartin",
      "description": "Jugaron 12 veces. Atl Tucuman ganó 5 veces. San Martin (T) ganó 3 veces. Empataron 4 veces. Atl Tucuman lleva una diferencia de 2 partidos."
    },
    {
      "name": "Banfield",
      "image": "1IipMIRe9C0XEQRVIdtU4SzqBNajphW6p",
      "id": "banfield",
      "vs": "lanus",
      "description": "Jugaron 83 veces. Banfield ganó 34 veces. Lanus ganó 26 veces. Empataron 23 veces. Banfield lleva una diferencia de 8 partidos."
    },
    {
      "name": "Belgrano",
      "image": "1Hksz-05khaZ9E8fS-tjUZg6y8uETpVCj",
      "id": "belgrano",
      "vs": "talleres",
      "description": "Jugaron 23 veces. Belgrano ganó 5 veces. Talleres (C) ganó 5 veces. Empataron 13 veces. Estan empatados en el historial."
    },
    {
      "name": "Boca",
      "image": "16UeRLSvU1yZJYHn4Bu1T7Qv8fbTbGi1N",
      "id": "boca",
      "vs": "river",
      "description": "Jugaron 205 veces. Boca Juniors ganó 75 veces. River Plate ganó 67 veces. Empataron 63 veces. Boca Juniors lleva una diferencia de 8 partidos."
    },
    {
      "name": "Defensa y Justicia",
      "image": "1TUyYG0aWwlA1EnfMVFJ3x6AqUiBQ0F74",
      "id": "defensa",
      "vs": "quilmes",
      "description": "Jugaron 4 veces. Def y Justicia ganó 2 veces. Quilmes ganó 1 veces. Empataron 1 veces. Def y Justicia lleva una diferencia de 1 partidos."
    },
    {
      "name": "Estudiantes",
      "image": "169VTQzS8VUsLKnY0CNVMSg5vS5SkoIlr",
      "id": "estudiantes",
      "vs": "gimnasia",
      "description": "Jugaron 164 veces. Estudiantes (LP) ganó 59 veces. Gimnasia (LP) ganó 46 veces. Empataron 59 veces. Estudiantes (LP) lleva una diferencia de 13 partidos."
    },
    {
      "name": "Gimnasia",
      "image": "1XkwNtxnM_KuJwoXOyI_4QO7t9oN6Qodc",
      "id": "gimnasia",
      "vs": "estudiantes",
      "description": "Jugaron 164 veces. Estudiantes (LP) ganó 59 veces. Gimnasia (LP) ganó 46 veces. Empataron 59 veces. Estudiantes (LP) lleva una diferencia de 13 partidos."
    },
    {
      "name": "Huracan",
      "image": "1EracduvJjPSuAuqDuj04V-fOaSTzNoRu",
      "id": "huracan",
      "vs": "sanlorenzo",
      "description": "Jugaron 166 veces. Huracan ganó 44 veces. San Lorenzo ganó 78 veces. Empataron 44 veces. San Lorenzo lleva una diferencia de 34 partidos."
    },
    {
      "name": "Independiente",
      "image": "1BPSIciRKRzKPo5WSDfMXjFscCpg9VPEW",
      "id": "independiente",
      "vs": "racing",
      "description": "Jugaron 196 veces. Independiente ganó 76 veces. Racing Club ganó 54 veces. Empataron 66 veces. Independiente lleva una diferencia de 22 partidos."
    },
    {
      "name": "Lanus",
      "image": "1p7YzzcX1115O_JdB_dLElGk3NuL9vWL1",
      "id": "lanus",
      "vs": "banfield",
      "description": "Jugaron 83 veces. Banfield ganó 34 veces. Lanus ganó 26 veces. Empataron 23 veces. Banfield lleva una diferencia de 8 partidos."
    },
    {
      "name": "Newells",
      "image": "1rS5zma6BOKcxkxIn3zpqZ8NA-VCBqfqk",
      "id": "newells",
      "vs": "rosariocentral",
      "description": "Jugaron 175 veces. Rosario Central ganó 53 veces. Newells ganó 43 veces. Empataron 79 veces. Rosario Central lleva una diferencia de 10 partidos."
    },
    {
      "name": "Platense",
      "image": "1JXC1w9mfeZW63QNYw6xGSHazhfGn9WiO",
      "id": "platense",
      "vs": "argentinos",
      "description": "Jugaron 77 veces. Argentinos ganó 21 veces. Platense ganó 26 veces. Empataron 30 veces. Platense lleva una diferencia de 5 partidos."
    },
    {
      "name": "Racing",
      "image": "1Nd_Y_Kphc9A9ikxRt2-Bx0aiVp8BfbMC",
      "id": "racing",
      "vs": "independiente",
      "description": "Jugaron 196 veces. Independiente ganó 76 veces. Racing Club ganó 54 veces. Empataron 66 veces. Independiente lleva una diferencia de 22 partidos."
    },
    {
      "name": "River",
      "image": "1_cpItHzt0ubH1HiNsvf7LmbW2JbbvIie",
      "id": "river",
      "vs": "boca",
      "description": "Jugaron 205 veces. Boca Juniors ganó 75 veces. River Plate ganó 67 veces. Empataron 63 veces. Boca Juniors lleva una diferencia de 8 partidos."
    },
    {
      "name": "Rosario Central",
      "image": "1qHW7MMqSkjO6tb5aLAbTqT9IUWRaONTd",
      "id": "rosariocentral",
      "vs": "newells",
      "description": "Jugaron 175 veces. Rosario Central ganó 53 veces. Newells ganó 43 veces. Empataron 79 veces. Rosario Central lleva una diferencia de 10 partidos."
    },
    {
      "name": "San Lorenzo",
      "image": "1GZ6lJsi806Ku08Eb__ZKzlpYt7wjThGU",
      "id": "sanlorenzo",
      "vs": "huracan",
      "description": "Jugaron 166 veces. Huracan ganó 44 veces. San Lorenzo ganó 78 veces. Empataron 44 veces. San Lorenzo lleva una diferencia de 34 partidos."
    },
    {
      "name": "Talleres",
      "image": "17AA0UWGGiMQkLrQyT6DooiCbHGJbNQlx",
      "id": "talleres",
      "vs": "belgrano",
      "description": "Jugaron 23 veces. Belgrano ganó 5 veces. Talleres (C) ganó 5 veces. Empataron 13 veces. Estan empatados en el historial."
    },
    {
      "name": "Union",
      "image": "1NIpHan8V7-IGeBCwozOqTVChzb3HMU94",
      "id": "union",
      "vs": "colon",
      "description": "Jugaron 58 veces. Union ganó 17 veces. Colon ganó 13 veces. Empataron 28 veces. Union lleva una diferencia de 4 partidos."
    },
    {
      "name": "Velez",
      "image": "1-4Q-t0HYnHbaJjr8-kqvUKHEP6BJEs9b",
      "id": "velez",
      "vs": "ferro",
      "description": "Jugaron 136 veces. Velez ganó 52 veces. Ferro ganó 45 veces. Empataron 39 veces. Velez lleva una diferencia de 7 partidos."
    },
    {
      "name": "San Martin",
      "image": "1X-4akFRvezNReXRDDPqmY9Uu8Lm1E_47",
      "id": "sanmartin",
      "vs": "atleticotucuman",
      "description": "Jugaron 12 veces. Atl Tucuman ganó 5 veces. San Martin (T) ganó 3 veces. Empataron 4 veces. Atl Tucuman lleva una diferencia de 2 partidos."
    },
    {
        "name": "Quilmes",
        "image": "1iZ5yRsn5w7FEmJ9isGZYJO2jvOzqOtSc",
        "id": "quilmes",
        "vs": "defensa",
        "description": "Jugaron 4 veces. Def y Justicia ganó 2 veces. Quilmes ganó 1 veces. Empataron 1 veces. Def y Justicia lleva una diferencia de 1 partidos."
      },
      {
        "name": "Colon",
        "image": "1Krgbfze7rMIbmbXYgzpV8jSdLr20Uo4q",
        "id": "colon",
        "vs": "union",
        "description": "Jugaron 58 veces. Union ganó 17 veces. Colon ganó 13 veces. Empataron 28 veces. Union lleva una diferencia de 4 partidos."
      },
      {
        "name": "Ferro Carril Oeste",
        "image": "1dg9jpeOSeh019KVbPaurYOQ2stZAUh3c",
        "id": "ferro",
        "vs": "velez",
        "description": "Jugaron 136 veces. Velez ganó 52 veces. Ferro ganó 45 veces. Empataron 39 veces. Velez lleva una diferencia de 7 partidos."
      }
  ]
  // Función para generar las tarjetas de los equipos
function generateTeamCards() {
  const container = document.getElementById('teams-container');
  teamsData.forEach(team => {
      const teamCard = document.createElement('div');
      teamCard.className = 'team-card';
      
      const teamLink = document.createElement('a');
      teamLink.href = `partido.html?id=${team.id}`;
      
      const teamImage = document.createElement('img');
      teamImage.src = `https://lh3.googleusercontent.com/d/${team.image}=s311`;
      teamImage.alt = team.name;
      
      const teamName = document.createElement('p');
      teamName.textContent = team.name;
      
      teamLink.appendChild(teamImage);
      teamLink.appendChild(teamName);
      teamCard.appendChild(teamLink);
      container.appendChild(teamCard);
  });
}

// Ejecuta la función al cargar la página
window.onload = generateTeamCards;