from typing import List
from grafos import Grafo
from pila import Pila

    # grafo_grafo_dioses.insertar_vertice('Themis');
    # grafo_grafo_dioses.insertar_vertice('Minemosyne');
    # grafo_grafo_dioses.insertar_vertice('Hyperion');
    # grafo_grafo_dioses.insertar_vertice('Theia');
    # grafo_grafo_dioses.insertar_vertice('Krios');
    # grafo_grafo_dioses.insertar_vertice('Kronos');
    # grafo_grafo_dioses.insertar_vertice('Rhea');
    # grafo_grafo_dioses.insertar_vertice('Kdios');
    # grafo_grafo_dioses.insertar_vertice('Phoibe');
    # grafo_grafo_dioses.insertar_vertice('Iapetos');
    # grafo_grafo_dioses.insertar_vertice('Okeanos');
    # grafo_grafo_dioses.insertar_vertice('Tedds');

    # grafo_grafo_dioses.insertar_vertice('Helios');
    # grafo_grafo_dioses.insertar_vertice('Eos');
    # grafo_grafo_dioses.insertar_vertice('Selene');

    # grafo_grafo_dioses.insertar_vertice('Prometheus');
    # grafo_grafo_dioses.insertar_vertice('Empimedheus');
    # grafo_grafo_dioses.insertar_vertice('Atlas');
    # grafo_grafo_dioses.insertar_vertice('Pelone');

    # grafo_grafo_dioses.insertar_vertice('Hades');
    # grafo_grafo_dioses.insertar_vertice('Demeter');
    # grafo_grafo_dioses.insertar_vertice('Poseidon');
    # grafo_grafo_dioses.insertar_vertice('Hestia');
    # grafo_grafo_dioses.insertar_vertice('Hera');
    # grafo_grafo_dioses.insertar_vertice('Zeus');
    # grafo_grafo_dioses.insertar_vertice('Leto');
    # grafo_grafo_dioses.insertar_vertice('Maia');

    # grafo_grafo_dioses.insertar_vertice('Ares');
    # grafo_grafo_dioses.insertar_vertice('Hephaistos');

    # grafo_grafo_dioses.insertar_vertice('Apollo');
    # grafo_grafo_dioses.insertar_vertice('Artemis');
    
def inicializar_grafo1(grafo):
    grafo.insertar_vertice('Urano')
    grafo.insertar_vertice('Cronos')
    grafo.insertar_vertice('Rea')
    grafo.insertar_vertice('Zeus')
    grafo.insertar_vertice('Hades')
    grafo.insertar_vertice('Demeter')
    grafo.insertar_vertice('Atenea')
    grafo.insertar_vertice('Apollo')
    grafo.insertar_vertice('Persefone')
    grafo.insertar_vertice('Theia')
    grafo.insertar_vertice('Helios')
    grafo.insertar_vertice('Eos')
    grafo.insertar_vertice('Selene')

    grafo.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})

    grafo.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['pareja']})

    grafo.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Zeus', 'Atenea', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Persefone', data={'relacion': ['padre', 'hijo']})

    grafo.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Demeter', 'Urano', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Apollo', 'Persefone', data={'relacion': ['hermano']})

    grafo.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})
    
def inicializar_grafo(grafo):
    grafo.insertar_vertice('Gaia')
    grafo.insertar_vertice('Urano')
    
    grafo.insertar_vertice('Themis')
    grafo.insertar_vertice('Minemosyne')
    grafo.insertar_vertice('Hyperion')
    grafo.insertar_vertice('Theia')
    grafo.insertar_vertice('Crios')
    grafo.insertar_vertice('Cronos')
    grafo.insertar_vertice('Rhea')
    grafo.insertar_vertice('Kdios')
    grafo.insertar_vertice('Phoibe')
    grafo.insertar_vertice('Iapetos')
    grafo.insertar_vertice('Okeanos')
    grafo.insertar_vertice('Tedds')
    
    grafo.insertar_vertice('Helios')
    grafo.insertar_vertice('Eos')
    grafo.insertar_vertice('Selene')
    grafo.insertar_vertice('Prometheus')
    grafo.insertar_vertice('Epimetheus')
    grafo.insertar_vertice('Atlas')
    grafo.insertar_vertice('Pleione')
    
    grafo.insertar_vertice('Hades')
    grafo.insertar_vertice('Demeter')
    grafo.insertar_vertice('Poseidon')
    grafo.insertar_vertice('Hestia')
    grafo.insertar_vertice('Hera')
    grafo.insertar_vertice('Zeus')
    grafo.insertar_vertice('Leto')
    grafo.insertar_vertice('Semelle')
    grafo.insertar_vertice('Maia')
    
    grafo.insertar_vertice('Persephone')
    grafo.insertar_vertice('Aphrodite')
    grafo.insertar_vertice('Ares')
    grafo.insertar_vertice('Hephaistos')
    grafo.insertar_vertice('Athena')
    grafo.insertar_vertice('Apollo')
    grafo.insertar_vertice('Artemis')
    grafo.insertar_vertice('Dionysos')
    grafo.insertar_vertice('Hermes')
    grafo.insertar_vertice('Penelopeia')
    
    grafo.insertar_vertice('Phobos')
    grafo.insertar_vertice('Deimos')
    grafo.insertar_vertice('Eros')
    grafo.insertar_vertice('Himeros')
    
    grafo.insertar_vertice('Hermaphrodite')
    grafo.insertar_vertice('Pan')
    
    grafo.insertar_arista(1, 'Urano', 'Gaia', data={'relacion': ['hijo', 'madre', 'pareja']})
    
    grafo.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Hyperion', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Crios', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Rhea', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Tedds', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Gaia', 'Themis', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Hyperion', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Theia', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Crios', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Cronos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Rhea', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Iapetos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Okeanos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Tedds', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hyperion', 'Theia', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Hyperion', 'Helios', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Hyperion', 'Eos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Hyperion', 'Selene', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})
    
    grafo.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Okeanos', 'Pleione', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Tedds', 'Pleione', data={'relacion': ['madre', 'hijo']})
    

    grafo.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Poseidon', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Hestia', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Hera', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Rhea', 'Hades', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Demeter', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Poseidon', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Hestia', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Hera', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Zeus', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Kdios', 'Leto', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Phoibe', 'Leto', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Atlas', 'Pleione', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Atlas', 'Maia', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Pleione', 'Maia', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Demeter', 'Zeus', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Demeter', 'Persephone', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Persephone', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hera', 'Zeus', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Hera', 'Ares', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Hera', 'Hephaistos', data={'relacion': ['madre', 'hijo']})
    
    grafo.insertar_arista(1, 'Zeus', 'Ares', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['pareja']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Leto', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Artemis', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Leto', 'Apollo', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Leto', 'Artemis', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Semelle', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Zeus', 'Dionysos', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Semelle', 'Dionysos', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Maia', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Zeus', 'Hermes', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Maia', 'Hermes', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hades', 'Persephone', data={'relacion': ['pareja']})
    
    
    grafo.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Aphrodite', 'Phobos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Aphrodite', 'Deimos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Aphrodite', 'Eros', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Aphrodite', 'Himeros', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Ares', 'Phobos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Ares', 'Deimos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Ares', 'Eros', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Ares', 'Himeros', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Aphrodite', 'Hephaistos', data={'relacion': ['pareja']})
    
    
    grafo.insertar_arista(1, 'Aphrodite', 'Hermes', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Aphrodite', 'Hermaphrodite', data={'relacion': ['madre', 'hijo']})
    
    grafo.insertar_arista(1, 'Hermes', 'Hermaphrodite', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hermes', 'Penelopeia', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Hermes', 'Pan', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Penelopeia', 'Pan', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Themis', 'Minemosyne', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Hyperion', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Theia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Crios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Minemosyne', 'Hyperion', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Theia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Crios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Hyperion', 'Crios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Theia', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Kdios', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Kdios', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Kdios', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Phoibe', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phoibe', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phoibe', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Iapetos', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Iapetos', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Helios', 'Eos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Helios', 'Selene', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Eos', 'Selene', data={'relacion': ['hermano']})
    
    
    grafo.insertar_arista(1, 'Prometheus', 'Epimetheus', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Prometheus', 'Atlas', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Epimetheus', 'Atlas', data={'relacion': ['hermano']})

    
    grafo.insertar_arista(1, 'Hades', 'Demeter', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Poseidon', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Hestia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Hera', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Zeus', data={'relacion': ['hermano']})
    

    grafo.insertar_arista(1, 'Demeter', 'Poseidon', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Demeter', 'Hestia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Demeter', 'Hera', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Poseidon', 'Hestia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Poseidon', 'Hera', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Poseidon', 'Zeus', data={'relacion': ['hermano']})

    grafo.insertar_arista(1, 'Hestia', 'Hera', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hestia', 'Zeus', data={'relacion': ['hermano']})

    
    grafo.insertar_arista(1, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})
    
    
    grafo.insertar_arista(1, 'Apollo', 'Artemis', data={'relacion': ['hermano']})
    
    
    grafo.insertar_arista(1, 'Phobos', 'Deimos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phobos', 'Eros', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phobos', 'Himeros', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Deimos', 'Eros', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Deimos', 'Himeros', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Eros', 'Himeros', data={'relacion': ['hermano']})


#PUNTO A
def cargar_descripcion(grafo):
    pausa = ''
    
    for i in range(grafo.inicio.tamanio()):
        no_pasa_20_palabras = True
        dios = grafo.inicio.obtener_elemento(i)
        while(no_pasa_20_palabras):
            descripcion = input('Agregar descripcion a ' + dios['info'] + ' : ')
            if(len(descripcion.split()) < 3):
                dios['data'] = descripcion
                no_pasa_20_palabras = False
            else:
                print('Error, la descripcion tiene que ser igual o menor a 20 letras')
                pausa = input();
                no_pasa_20_palabras = True

# PUNTO C
def mostrar_hijos(grafo, vertice_dios):
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''
    pausa = '';
    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            
            if (len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][0] == 'padre' or dios_aux['relacion'][0] == 'madre'):
                    print(nombre, ' relacion: ', dios_aux['relacion'])
    else:
        print('El dios ', vertice_dios, ' no se encuentra en el grafo')

# PUNTO D
def mostrar_nombre_padre_madre_hermanos_hijos_de_un_dios(grafo, vertice_dios):
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''
    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        print('nombre dios: ', vertice_dios)
        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            print(nombre, dios_aux['relacion'])

# PUNTO E
def relacion_directa(grafo, ver_origen, ver_destino):
    print('tiene relacion directa:')
    pos = grafo.buscar_arista(ver_origen, ver_destino)
    if(pos != 1):
        pos_aux = grafo.buscar_vertice(ver_origen)
        print(grafo.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))

# PUNTO F
def camino_mas_corto_entre_dos_vertices(grafo, nombre_origen, nombre_destino):
    vertice_origen = grafo.buscar_vertice(nombre_origen)
    vertice_destino = grafo.buscar_vertice(nombre_destino)
    costo = None
    
    if vertice_origen != -1 and vertice_destino != -1:
        camino = grafo.dijkstra(vertice_origen)
        
        while(not camino.pila_vacia()):
            dato = camino.desapilar()
            if(dato[1][0] == nombre_destino):
                if(costo is None):
                    costo = dato[0]
                print('paso por: ', dato[1][0])
                destino = dato[1][1]
                
        print('el costo total del camino es: ', costo)

# PUNTO H
def buscar_nombre_dios_de_x_relacion(grafo, vertice_dios, nombre_relacion):
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''
    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        for i in range(dios['aristas'].tamanio()):
            relacion = dios['aristas'].obtener_elemento(i)['data']['relacion']
            if ((len(relacion) > 1) and (relacion[1] == nombre_relacion)):
                return  dios['aristas'].obtener_elemento(i)['destino']
    else:
        return None

def barrido_del_grafo_mostrando_la_relacion_x(grafo, pos_vertice_dios, nombre_relacion):
    while(pos_vertice_dios < grafo.inicio.tamanio()):
        vertice = grafo.inicio.obtener_elemento(pos_vertice_dios)
        if(not vertice['visitado']):
            vertice['visitado'] = True
            madre_dios = buscar_nombre_dios_de_x_relacion(grafo, vertice['info'], nombre_relacion)
            if madre_dios is not None:
                print(vertice['info'], ' madre: ', madre_dios)
            else:
                print(vertice['info'], ' no tiene madre')
            aristas = 0
            while(aristas < vertice['aristas'].tamanio()):
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = grafo.buscar_vertice(arista['destino'])
                nuevo_vertice = grafo.inicio.obtener_elemento(pos_vertice)
                if(not nuevo_vertice['visitado']):
                    barrido_del_grafo_mostrando_la_relacion_x(grafo, pos_vertice, nombre_relacion)
                aristas += 1
        pos_vertice_dios += 1

# PUNTO I
def falta_elemento(dato, vector, campo):
    for vec in vector:
        if vec[campo] == dato:
            return False
    
    return True

def get_acestros_de_un_dios(grafo, nombre_origen, nombre_dios = '', vec_asestro = [], primera_pasada = True):
    pausa = None
    indice_relacion = 0
    relacion = ''
    pos_origen = grafo.buscar_vertice(nombre_dios)
    nombre = ''
    
    if pos_origen >= 0 and pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if (primera_pasada and len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][0] == 'hijo'):
                    vec_asestro.append({'nombre': nombre, 'relacion' : dios_aux['relacion'][1], 'visitado' : False})
                    
            if (not primera_pasada):
                if len(dios_aux['relacion']) > 1:
                    indice_relacion = 1
                else:
                    indice_relacion = 0
                    
                if dios_aux['relacion'][indice_relacion] == 'hermano':
                    relacion = 'tio'
                elif dios_aux['relacion'][indice_relacion] == 'pareja':
                    relacion = 'madrastra'
                else:
                    relacion = dios_aux['relacion'][indice_relacion]

                if(falta_elemento(nombre, vec_asestro, 'nombre') and nombre != nombre_origen) and relacion != 'hijo':
                    vec_asestro.append({'nombre': nombre, 'relacion' : relacion, 'visitado' : False})

        if(i ==  (dios['aristas'].tamanio() - 1)):
            for ansestro in vec_asestro:
                if((ansestro['relacion'] in ['padre', 'madre']) and ansestro['visitado'] == False):
                    ansestro['visitado'] = True
                    get_acestros_de_un_dios(grafo, nombre_origen, ansestro['nombre'], vec_asestro, False)
        
    else:
        print('El dios ', nombre_dios, ' no se encuentra en el grafo')

def mostrar_acestros_de_un_dios(grafo, nombre_dios):
    vector_ansestros = []
    get_acestros_de_un_dios(grafo, nombre_dios, nombre_dios, vector_ansestros)
    print('ANSESTROS DE ', nombre_dios)
    for ansestro in vector_ansestros:
        print('nombre ansestro: ', ansestro['nombre'], ' relacion: ', ansestro['relacion'])

# PUNTO J
def get_hijos_de_un_dios(grafo, vertice_dios, vector_nietos = []):
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''
    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if (len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][0] == 'padre' or dios_aux['relacion'][0] == 'madre'):
                    if(nombre not in vector_nietos):
                        vector_nietos.append(nombre)
    else:
        print('El dios ', vertice_dios, ' no se encuentra en el grafo')
        
def mostrar_nietos_de_un_dios(grafo, nombre_dios):
    pos_origen = grafo.buscar_vertice(nombre_dios)
    nombre = ''
    vector_nietos = []
    
    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if (len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][0] == 'padre' or dios_aux['relacion'][0] == 'madre'):
                    get_hijos_de_un_dios(grafo, nombre, vector_nietos)
                    
    else:
        print('El dios ', nombre_dios, ' no se encuentra en el grafo')
    
    print('NIETOS DE ', nombre_dios)
    for nieto in vector_nietos:
        print(nieto)


def ejercicio_6():
    grafo_dioses = Grafo(dirigido=False)
    inicializar_grafo(grafo_dioses)
    
    # print('CARGAR DESCRIPCION DE MENOS DE 20 PALABRAS')
    # cargar_descripcion(grafo_dioses)
    
    # print()
    # print('MOSTRAR LOS HIJOS DE UN DIOS DADO EL NOMBRE DE UNO')
    # mostrar_hijos(grafo_dioses, 'Cronos')
    
    # print()
    # print('MOSTRAR EL NOMBRE, PADRE, MADRE, HERMANOS Y HIJOS DE UN DIOS DADO EL NOMBRE DE UNO')
    # mostrar_nombre_padre_madre_hermanos_hijos_de_un_dios(grafo_dioses, 'Cronos')
    
    # print();
    # print('DETERMINAR SI HAY RELACION DIRECTA ENTRE DOS VERTICES' 
    #         , 'CUALQUIERA Y SI LA HAY, MOSTRAR LA RELACION')
    # relacion_directa(grafo_dioses, 'Cronos', 'Rea');

    # print()
    # print('DADO DOS DIOSES, DETERMINAR EL CAMINO MAS CORTO ENTRE ESTOS Y MOSTRARLO')
    # camino_mas_corto_entre_dos_vertices(grafo_dioses, 'Urano', 'Cronos')
    
    # print()
    # print('BARRIDO EN PROFUNDIDAD Y AMPLITUD DE DICHO GRAFO')
    # grafo_dioses.barrido_profundidad(0)
    # grafo_dioses.barrido_amplitud(0)
    
    # print()
    
    # barrido_del_grafo_mostrando_la_relacion_x(grafo_dioses, 0, 'madre')
    
    # print()
    # print('MOSTRAR LOS ANSESTROS DE UN DETERMINADO DIOS')
    # mostrar_acestros_de_un_dios(grafo_dioses, 'Persefone')
    
    # print()
    # print('MOSTRAR LOS NIETOS DE CRONOS')
    # mostrar_nietos_de_un_dios(grafo_dioses, 'Cronos')
    
    # print()
    # print('MOSTRAR LOS HIJOS DE THEIA')
    # mostrar_hijos(grafo_dioses, 'Theia')

ejercicio_6()
