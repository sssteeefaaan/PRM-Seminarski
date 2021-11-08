from visual import *

urls = [
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-1.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-2.xml',
        'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-3.xml'
        # ,'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-4.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-5.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-1.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-2.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-3.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-4.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-5.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-1.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-2.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-3.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-4.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-5.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-1.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-2.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-3.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-4.xml',
        # 'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-5.xml',
        ]

cmpMeta = [
        ('alertid', 0, equals),
        ('date', 0.09, dateCmp), 
        ('time', 0.09, timeCmp),
        ('sessionduration', 0.05, sessionCmp),
        ('spoofed', 0.05, equals),
        ('category', 0.05, equals), # Source ip address category
        ('address', 0.15, addressCmp), # Source ip address
        ('sport', 0.09, portCmp), # Source ip address port
        ('Address category', 0.05, equals), # Target ip address category
        ('Address address', 0.15, addressCmp), # Target ip address
        ('dport', 0.09, portCmp), # Target ip address port
        ('Service name', 0.1, equals),
        ('impact', 0.04, equals),
        
        # Neuračunati atributi
        ('version', 0, equals), # Message version
        ('Alert version', 0, equals), # Alert version
        ('ident', 0, equals), # Analyzer identificator
        ('name', 0, equals) # Analyzer name
]

(a, c, h) = zip(*cmpMeta)
t = 0.75

for url in urls:
    visualizeData(url, a, c, h, t)