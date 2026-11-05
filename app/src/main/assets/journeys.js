/* Optional, timeless memory trails. Progress is derived from actual saved entries. */
(()=>{'use strict';
const PATHS=[
 {id:'together',tag:'együtt',icon:'people',name:'Akikhez tartozom',prompt:'Kihez kapcsolódik egy emlék, amit szeretnél megőrizni?',hint:'Egy közös mondat, szokás vagy apró találkozás.',goal:3},
 {id:'senses',tag:'érzékek',icon:'flower',name:'Öt érzék ösvénye',prompt:'Milyen hangot, illatot, ízt vagy színt őriz egy pillanatod?',hint:'Nem kell mind az öt: egyetlen részlet is elég.',goal:3},
 {id:'roots',tag:'gyökereim',icon:'house',name:'A gyökereim',prompt:'Melyik régi helyet vagy családi szokást adnád tovább?',hint:'Egy régi szoba, egy történet, egy ismerős mozdulat.',goal:3},
 {id:'small',tag:'apró pillanat',icon:'cup',name:'Hétköznapi kincsek',prompt:'Melyik hétköznapi pillanatot lenne jó később újraolvasni?',hint:'Egy tea, egy séta vagy valami egészen egyszerű.',goal:3},
 {id:'discovery',tag:'felfedezés',icon:'compass',name:'Felfedező szemmel',prompt:'Mit láttál, tanultál vagy próbáltál ki először?',hint:'Egy kis felfedezés is lehet fontos.',goal:3},
 {id:'courage',tag:'bátorság',icon:'lantern',name:'Ami megtartott',prompt:'Mi vagy ki segített át egy nehezebb pillanaton?',hint:'Csak annyit írj le, amennyi most kényelmes. Kihagyhatod.',goal:3},
 {id:'nature',tag:'természet',icon:'tree',name:'Kint a világban',prompt:'Melyik természeti pillanatot vinnéd magaddal?',hint:'Egy fa árnyéka, eső az ablakon, egy madár hangja.',goal:3},
 {id:'words',tag:'egy mondat',icon:'book',name:'Továbbadott szavak',prompt:'Melyik mondatot vagy tanácsot őriznéd meg szó szerint?',hint:'Lehet saját gondolatod vagy valaki más mondata.',goal:3}
];
const THEMES=[{id:'meadow',name:'Tavaszi tisztás',min:0,desc:'Új hajtások, meleg napfény.'},{id:'dusk',name:'Alkonyi kert',min:30,desc:'Borostyánfény és rózsaszín ég.'},{id:'stars',name:'Csillagliget',min:70,desc:'Szentjánosbogarak az éjszakában.'},{id:'autumn',name:'Aranylevelű liget',min:150,desc:'Aranyló lomb és őszi bogyók.'}];
const ALBUMS=[{id:'family',name:'Emberek és kapcsolatok',icon:'people',terms:['család','barátok','együtt']},{id:'nature',name:'Kint a világban',icon:'tree',terms:['természet','utazás','felfedezés']},{id:'roots',name:'Otthon és gyökerek',icon:'house',terms:['otthon','gyökereim','ünnep']},{id:'senses',name:'Érzékek és részletek',icon:'flower',terms:['érzékek','íz','illat','hang']},{id:'small',name:'Hétköznapi kincsek',icon:'cup',terms:['apró pillanat','apró öröm','hála','nevetés']},{id:'words',name:'Szavak és tanulás',icon:'book',terms:['egy mondat','tanulás','bátorság']}];
const norm=s=>s.toLocaleLowerCase('hu-HU').normalize('NFD').replace(/[\u0300-\u036f]/g,''),has=(e,tag)=>e.tags.some(t=>norm(t)===norm(tag));
function recorded(e){return e.recordedDay||e.createdAt.slice(0,10)}
function albumEntries(entries,id){const album=ALBUMS.find(a=>a.id===id);return album?entries.filter(e=>album.terms.some(t=>has(e,t))||(id==='family'&&e.people.trim())):[]}
function progress(entries){const days=new Set(entries.map(recorded)),leaves=days.size*10,paths=PATHS.map(p=>({...p,count:entries.filter(e=>has(e,p.tag)).length})),people=new Set(entries.map(e=>norm(e.people.trim())).filter(Boolean));const badges=[
 ['first','Az első levél','Egy megőrzött emlék.','leaf',entries.length>=1],
 ['return','Visszatérő mesélő','Három különböző írással töltött nap.','sun',days.size>=3],
 ['week','Hét emlékező nap','Hét különböző napon írtál. Nem kell egymást követniük.','stars',days.size>=7],
 ['ten','Tíz kincs','Tíz megőrzött pillanat.','book',entries.length>=10],
 ['twentyfive','Lombkorona','Huszonöt megőrzött emlék.','tree',entries.length>=25],
 ['fifty','Történetliget','Ötven megőrzött emlék.','house',entries.length>=50],
 ['favorite','Szívhez közel','Kiemeltél egy kedvenc emléket.','heart',entries.some(e=>e.favorite)],
 ['past','A múlt őrzője','Egy korábbi nap emlékét is leírtad.','lantern',entries.some(e=>e.date<recorded(e))],
 ['detail','Apró részletek őre','Egy emlékhez külön részletet is írtál.','flower',entries.some(e=>e.detail.trim())],
 ['people','Kapcsolatok kertje','Három különböző megadott név vagy névcsoport.','people',people.size>=3],
 ['paths','Ösvényjáró','Három különböző ösvény jelölőszavával írtál.','compass',paths.filter(p=>p.count>0).length>=3],
 ['trail','Egy ösvény otthonra talál','Egy ösvényen három emléket őriztél meg.','ribbon',paths.some(p=>p.count>=p.goal)]
 ].map(([id,name,desc,icon,unlocked])=>({id,name,desc,icon,unlocked}));
 return{days:days.size,leaves,paths,badges,themes:THEMES.map(t=>({...t,unlocked:leaves>=t.min})),unlocked:badges.filter(b=>b.unlocked).length};}
function effectiveTheme(entries,selected){return progress(entries).themes.find(t=>t.id===selected&&t.unlocked)?.id||'meadow'}
function category(e){return ALBUMS.find(a=>albumEntries([e],a.id).length)?.icon||({joy:'sun',calm:'leaf',moved:'heart',hard:'lantern',mixed:'stars'}[e.mood])||'book'}
window.MemoryJourney={PATHS,THEMES,ALBUMS,progress,albumEntries,effectiveTheme,category,has};})();
