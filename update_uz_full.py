import re

STANDINGS = [
    (1, "Neftchi Fergana", "Fergana", 19, 35, 45),
    (2, "Pakhtakor", "Tashkent", 19, 13, 40),
    (3, "Navbahor", "Namangan", 19, 14, 37),
    (4, "Buxoro", "Bukhara", 19, 8, 34),
    (5, "OKMK", "Olmaliq", 20, 3, 32),
    (6, "Lokomotiv", "Tashkent", 19, 6, 31),
    (7, "Andijon", "Andijon", 19, 4, 27),
    (8, "Dinamo Samarqand", "Samarkand", 19, -1, 26),
    (9, "Nasaf", "Qarshi", 19, 2, 25),
    (10, "Sogdiana", "Jizzax", 19, -7, 24),
    (11, "Qizilqum", "Navoiy", 19, -9, 23),
    (12, "Surkhon", "Termiz", 19, -10, 20),
    (13, "Xorazm", "Urganch", 20, -12, 20),
    (14, "Kokand 1912", "Kokand", 19, -9, 19),
    (15, "Bunyodkor", "Tashkent", 19, -11, 19),
    (16, "Mash'al", "Muborak", 19, -26, 4),
]

# (team, wiki_en_o_None, web_o_None, sofascore_url)
LINKS = {
    "Neftchi Fergana": ("https://en.wikipedia.org/wiki/FC_Neftchi_Fergana", "https://fcneftchi.uz", "https://www.sofascore.com/football/team/neftchi-fargona/36256"),
    "Pakhtakor": ("https://en.wikipedia.org/wiki/Pakhtakor_FC", "https://www.pakhtakor.uz", "https://www.sofascore.com/football/team/pakhtakor-tashkent/34310"),
    "Navbahor": ("https://en.wikipedia.org/wiki/PFC_Navbahor_Namangan", "https://pfcnavbahor.uz", "https://www.sofascore.com/football/team/navbahor-namangan/40263"),
    "Buxoro": ("https://en.wikipedia.org/wiki/FC_Bukhara", None, "https://www.sofascore.com/football/team/fc-buxoro/48613"),
    "OKMK": ("https://en.wikipedia.org/wiki/FC_AGMK", None, "https://www.sofascore.com/football/team/fc-agmk/40268"),
    "Lokomotiv": ("https://en.wikipedia.org/wiki/PFC_Lokomotiv_Tashkent", "https://lokomotiv.uz", "https://www.sofascore.com/football/team/lokomotiv-tashkent/40261"),
    "Andijon": (None, None, "https://www.sofascore.com/football/team/pfk-andijon/40267"),
    "Dinamo Samarqand": ("https://en.wikipedia.org/wiki/FC_Dinamo_Samarqand", "https://www.fcdinamo.uz", "https://www.sofascore.com/football/team/dinamo-samarqand/40259"),
    "Nasaf": ("https://en.wikipedia.org/wiki/FC_Nasaf", "https://www.fcnasaf.uz", "https://www.sofascore.com/football/team/nasaf-qarshi/34017"),
    "Sogdiana": ("https://en.wikipedia.org/wiki/FC_Sogdiana", "https://www.fcsogdiana.uz", "https://www.sofascore.com/football/team/fc-sogdiana-jizzakh/48614"),
    "Qizilqum": (None, None, "https://www.sofascore.com/football/team/pfk-qizilqum/40265"),
    "Surkhon": ("https://en.wikipedia.org/wiki/FC_Surkhon", None, "https://www.sofascore.com/football/team/surkhon-termez/287019"),
    "Xorazm": (None, None, "https://www.sofascore.com/football/team/pfk-xorazm/40260"),
    "Kokand 1912": (None, None, "https://www.sofascore.com/football/team/fk-kokand-1912/191273"),
    "Bunyodkor": ("https://en.wikipedia.org/wiki/FC_Bunyodkor", None, "https://www.sofascore.com/football/team/fc-bunyodkor/23481"),
    "Mash'al": (None, None, "https://www.sofascore.com/football/team/mash-al-mubarek/40264"),
}

DESC_ES = {
    "Neftchi Fergana": "Fundado en 1962, apodado \"los Tigres\"; financiado por la refinería petrolera de Fergana. Seis veces campeón de Uzbekistán, y campeón vigente tras revalidar el título de 2025.",
    "Pakhtakor": "Fundado en 1956, el club más laureado de Uzbekistán con diferencia. Su nombre significa \"cultivador de algodón\", en referencia a la herencia agrícola del país.",
    "Navbahor": "Fundado en 1978, con sede en Namangan, en el corazón del valle de Fergana. Su nombre significa \"nueva primavera\"; uno de los tres clubes que ha disputado todas las temporadas de la liga desde la independencia.",
    "Buxoro": "Club de la histórica ciudad de Bujará, una de las más antiguas de Asia Central.",
    "OKMK": "Fundado en 2004, propiedad del complejo minero-metalúrgico de Olmaliq (de ahí sus siglas); apodados \"los Mineros\".",
    "Lokomotiv": "Fundado en 2002, propiedad de las Ferrocarriles de Uzbekistán (Uzbek Railways).",
    "Andijon": "Club de la ciudad de Andiyán, en el extremo oriental del valle de Fergana.",
    "Dinamo Samarqand": "Uno de los clubes más antiguos de Uzbekistán, fundado en 1960; ha cambiado de nombre en numerosas ocasiones a lo largo de su historia.",
    "Nasaf": "Fundado en 1986 en Qarshi, apodados \"los Dragones\"; uno de los clubes más importantes del país en las últimas dos décadas.",
    "Sogdiana": "Fundado en 1970 en Jizzax, toma su nombre de la antigua región histórica de Sogdiana.",
    "Qizilqum": "Club de Navoiy, en el centro del país, cerca del desierto de Kyzylkum que da nombre al equipo.",
    "Surkhon": "Fundado en 1968 en Termez, ciudad fronteriza con Afganistán, en el extremo sur de Uzbekistán.",
    "Xorazm": "Representa a Urganch, en la región de Corasmia (Xorazm), junto al delta del río Amu Daria.",
    "Kokand 1912": "Club de la histórica ciudad de Kokand; el \"1912\" de su nombre remite a los orígenes del club en el fútbol de la época del Imperio ruso.",
    "Bunyodkor": "Fundado en 2005 en Tashkent como proyecto de gran ambición: llegó a fichar a Rivaldo y contratar a Zico y Luiz Felipe Scolari como entrenadores.",
    "Mash'al": "Representa a Muborak, localidad ligada a la industria del gas natural, en la región de Kashkadarya.",
}
DESC_EN = {
    "Neftchi Fergana": "Founded in 1962, nicknamed \"the Tigers\"; financed by the Fergana oil refinery. Six-time champions of Uzbekistan, and reigning champions after defending their 2025 title.",
    "Pakhtakor": "Founded in 1956, by far the most successful club in Uzbekistan. Their name means \"cotton grower\", reflecting the country's agricultural heritage.",
    "Navbahor": "Founded in 1978, based in Namangan, in the heart of the Fergana Valley. Their name means \"new spring\"; one of only three clubs to have played every season of the league since independence.",
    "Buxoro": "Club from the historic city of Bukhara, one of the oldest cities in Central Asia.",
    "OKMK": "Founded in 2004, owned by the Olmaliq mining and metallurgical complex (hence the initials); nicknamed \"the Miners\".",
    "Lokomotiv": "Founded in 2002, owned by Uzbek Railways.",
    "Andijon": "Club from the city of Andijan, at the eastern edge of the Fergana Valley.",
    "Dinamo Samarqand": "One of Uzbekistan's oldest clubs, founded in 1960; has changed name numerous times throughout its history.",
    "Nasaf": "Founded in 1986 in Qarshi, nicknamed \"the Dragons\"; one of the country's leading clubs over the last two decades.",
    "Sogdiana": "Founded in 1970 in Jizzakh, named after the ancient historical region of Sogdia.",
    "Qizilqum": "Club from Navoiy, in the centre of the country, near the Kyzylkum desert the team is named after.",
    "Surkhon": "Founded in 1968 in Termez, a border city with Afghanistan at Uzbekistan's southern tip.",
    "Xorazm": "Represents Urgench, in the historic Khorezm region, by the delta of the Amu Darya river.",
    "Kokand 1912": "Club from the historic city of Kokand; the \"1912\" in the name points back to the club's origins in football under the Russian Empire.",
    "Bunyodkor": "Founded in 2005 in Tashkent as a high-ambition project: once signed Rivaldo and hired Zico and Luiz Felipe Scolari as coaches.",
    "Mash'al": "Represents Muborak, a town tied to the natural gas industry, in the Kashkadarya region.",
}

def zone(pos):
    if pos <= 2: return ' class="zone-qualify"'
    if pos == 16: return ' class="zone-relegate"'
    return ""

def std_rows(lang):
    out = []
    for pos, team, city, pj, diff, pts in STANDINGS:
        d = f"+{diff}" if diff > 0 else str(diff)
        out.append(f"<tr{zone(pos)}><td>{pos}</td><td>{team}</td><td>{city}</td><td>{pj}</td><td>{d}</td><td>{pts}</td></tr>")
    return "\n          ".join(out)

def teams_list(lang):
    desc_map = DESC_ES if lang == "es" else DESC_EN
    label_web = "Web oficial" if lang == "es" else "Official site"
    out = []
    for pos, team, city, pj, diff, pts in STANDINGS:
        wiki, web, sofa = LINKS[team]
        desc = desc_map[team]
        links = []
        if wiki:
            links.append(f'<a href="{wiki}" target="_blank" rel="noopener">Wikipedia (EN)</a>')
        links.append(f'<a href="{sofa}" target="_blank" rel="noopener">Sofascore</a>')
        if web:
            links.append(f'<a href="{web}" target="_blank" rel="noopener">{label_web}</a>')
        links_html = "\n          ".join(links)
        out.append(
            f'<li><span class="team-name">{team}</span><span class="team-city">{city}</span>'
            f'<p class="team-desc">{desc}</p>'
            f'<div class="team-links">\n          {links_html}\n          </div></li>'
        )
    return "\n        ".join(out)

TABLE_ES = f"""<div class="table-wrap">
      <table>
        <thead><tr><th>Pos</th><th>Equipo</th><th>Ciudad</th><th>PJ</th><th>Dif</th><th>Pts</th></tr></thead>
        <tbody>
          {std_rows("es")}
        </tbody>
      </table>
      </div>
      <div class="zone-legend">
        <span><span class="swatch qualify"></span>AFC (1: Champions League Elite · 2: Champions League 2)</span>
        <span><span class="swatch relegate"></span>Descenso directo (más playoff de descenso en las posiciones 12-15)</span>
      </div>
      <p class="note">Clasificación extraída de Sofascore (jornada 19-20 de 2026). Verificar contra pfl.uz antes de publicar: cambia cada semana.</p>"""

TABLE_EN = f"""<div class="table-wrap">
      <table>
        <thead><tr><th>Pos</th><th>Team</th><th>City</th><th>P</th><th>Diff</th><th>Pts</th></tr></thead>
        <tbody>
          {std_rows("en")}
        </tbody>
      </table>
      </div>
      <div class="zone-legend">
        <span><span class="swatch qualify"></span>AFC (1: Champions League Elite · 2: Champions League 2)</span>
        <span><span class="swatch relegate"></span>Direct relegation (plus a relegation playoff for positions 12-15)</span>
      </div>
      <p class="note">Standings pulled from Sofascore (matchday 19-20 of 2026). Verify against pfl.uz before publishing — it changes weekly.</p>"""

for path, lang, table in [("es/ligas/uzbekistan.html", "es", TABLE_ES), ("en/leagues/uzbekistan.html", "en", TABLE_EN)]:
    with open(path, encoding="utf-8") as f:
        content = f.read()

    content, n1 = re.subn(
        r'<div class="table-wrap"><table>\s*<thead><tr><th>Pos</th>.*?</table>\s*</div>\s*<div class="zone-legend">.*?</div>\s*<p class="note">Datos a jornada 19.*?</p>',
        table, content, count=1, flags=re.DOTALL
    )
    content, n2 = re.subn(
        r'<ul class="team-grid">.*?</ul>',
        f'<ul class="team-grid">\n        {teams_list(lang)}\n      </ul>',
        content, count=1, flags=re.DOTALL
    )
    assert n1 == 1 and n2 == 1, (path, n1, n2)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(path, "actualizado")
