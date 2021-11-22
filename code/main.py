from visual import visualizeDataFileArray
from compareFuncs import *

def main():
        urls = [
                #'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-1.xml',
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-2.xml', ##
                #'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-3.xml',
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-4.xml', ##
                #'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_dmz/mid-level-phase-5.xml',
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-1.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-2.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-3.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-4.xml', ##
                #'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_1.0/data_and_labeling/tcpdump_inside/mid-level-phase-5.xml',
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-1.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-2.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-3.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-4.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_inside/mid-level-phase-5.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-1.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-2.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-3.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-4.xml', ##
                'https://archive.ll.mit.edu/ideval/data/2000/LLS_DDOS_2.0.2/data_and_labeling/tcpdump_dmz/mid-level-phase-5.xml' ##
                ]

        cmpMeta = [
                ('alertid', 0, equals),
                ('date', 0.12, dateCmp), 
                ('time', 0.08, timeCmp),
                ('sessionduration', 0.02, sessionCmp),
                ('spoofed', 0.02, equals),
                ('category', 0.02, equals), # Source ip address category
                ('address', 0.2, addressCmp), # Source ip address
                ('sport', 0.15, portCmp), # Source ip address port
                ('Address category', 0.02, equals), # Target ip address category
                ('Address address', 0.1, addressCmp), # Target ip address
                ('dport', 0.1, portCmp), # Target ip address port
                ('Service name', 0.15, equals),
                ('impact', 0.02, equals),
                
                # Neuračunati atributi
                ('version', 0, equals), # Message version
                ('Alert version', 0, equals), # Alert version
                ('ident', 0, equals), # Analyzer identificator
                ('name', 0, equals) # Analyzer name
        ]

        (a, c, h) = zip(*cmpMeta)
        t = 0.65
        visualizeDataFileArray(urls, a, c, h, t)
        
        
if __name__ == '__main__':
        main()