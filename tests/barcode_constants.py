import barcode_to_well

# 96-well 3LevelV2 and well mappings
lig_i7_list = ["TTAGTATATA","TGCCTCGCAA","GACTACGGCC","CGGCCGCTCC","TTCATCGTAA","GAGATTCCAA","CGCCTACCAA","GTTATATGCA","TTACGAATGG","ATTCTGCGGT","GCTGATAATT","AACGCAATGG","CCAACCGCGA","CTTCTCGACT","AATGATGCTC","CGGTCCGCGG","GCAAGTTAGC","AACCAGCATG","CCTCTAGGAC","AGAGGACTGG","GCTCTTACTT","CCTTGGCTCT","TGGCGTTGGC","TACTGGACGG","CCTTAACGCC","GTCGAGGTAA","GATGATTGGA","GAACTTGCGG","TAGATCCTAA","GCCGACGATA","AGTTACGCCG","GAGGAGAGCT","TACTCGAACT","TTATAGGAGA","CGGAGCGTCA","GCGACTCGAT","TATCGGCAGT","GAGTATACCT","TGGAGGCGAA","CGGATAAGCT","GGCTGCGACG","CTGAAGTCAA","ACTAGACGTT","TTGGTCGAAT","CTAACCTACC","CTGCGGACGT","CTGCAGATCC","CTTCTCTTAG","ATTCAATTAA","TCTGCCGGCA","GATTCGGTCA","ACCAGCGGTT","ATGACGGCTA","AAGCTATGCC","GTAAGGCCGA","TTCTTGACCG","TCTAGCAAGT","AGGCAGTACC","AATTCAGAAC","TCTGGACTCA","CAATTCGTTA","ATGGCAACTT","CTCGACCGGC","TACTCCTCGA","GACTAGCATT","CTCTGGAGAC","AAGTTCCAGC","ACCTTCTGGA","AAGGATCCAA","TACCGCTCCT","TCTGCTATAA","CGAGCGGCCT","TGCTGCATCC","GCTCCAACGC","TAATGGTAGA","TGGCTGACCA","GTTCTTATAA","GCTATCCTCC","ACGATAGCTG","GATCCGCCAT","TAGATAATGG","CCTATTACCT","AGAAGCGATC","ACTACCGCGC","CGAGGCCGGA","TATTGCAGCT","AGAATTAGCA","TGATCCTGGC","GCCGTAATCG","AAGGCGTCGC","TGCATGGCCA","CAGCCATGAT","CGTAAGCGAA","GTCGGCAAGA","GCAACTCCGG","ATATAGGTTG"]
pcr_i7_list = ["GAATGCCTTG","CGGACTGGCC","CTGGCAGCGG","TCATCAGCCA","TAACCAGTTA","AGCTCATTCG","CAACGGTCTT","TGGTATCAGA","GGTAACTACG","CTTCAGGCCA","ATCCTTCAAC","TGATTGAATG","TGCTTAGCGA","CGAGTTCGCC","CGGCATCTTG","TCAACGAGGT","GGTCTAGGAA","AAGTCAACGG","TAACCAATCG","ATCGGCTTGA","CAATCTCAAT","CAGTTGCTTG","ATGCTAACCT","CGGATCTCCG","TGACGCGACC","TCTGACGAAC","GATCATGATA","TTCTCTACGA","TACGCAGGTT","TGCGAATCGG","CTAAGAGTTA","TCCATACCTG","ACCGGTCTGC","TAGAACCTCC","TGACCATCAG","GACTCGAGGA","GCATTAGGCG","GGACTTATGG","TTGGTTCTCA","TAATTCCGGT","CTACTGCAAG","CGTAGCCGTA","TTGACTTCGT","TCAGCGCAAT","ATATGGTACC","TGCCGGTACC","GGTACTTCCA","AATTGAGTTA","GCGGCGCAAG","AATACCTGCC","AGCATACGGC","GCCTCGGTAA","ACGGACCTGC","CATTCTGATG","GCTTACTATA","TCCAATGGTT","ACGGTAATTG","TCGGAGTATG","GGTTAGTTGG","CTGCATTACG","TGCGGCCTGG","CATCTATTCG","GCAGCTGATT","ATATCTTCCG","GTCGTACGCG","TTGATGCCTC","TTGGAACTGG","GGAGAATGGC","TTCCATTCTT","CCGAAGGTTA","CCGGCTGAGC","ACGAGGAGCC","AAGATCAGTT","ATCCGAACGG","CTGCGCTGGT","TGCCATGGAA","AGCTGAACGC","GAGACGTTCT","CTGACTACTT","CGCCGATATC","TGGATCGTTA","GTACCTGAAT","GAATTCTCCA","AGACCAGGTT","CTAGCTTCTT","GGCAACCTTC","CCGTTAGCAA","GGCGTCTGCC","CGCGCAACCG","AGTCTTAATT","TAAGGAACGG","TCGTTCATTA","ACTCCAGATT","CGATATATCT","GGCTGGCTCT","GGCGGATACC"]
pcr_i5_list = ["GACCTCCTTG","ACCAGTTCAG","TTCTGGCGCA","GGCAATCAAG","TTGGCCAGGT","TCTCCTCCTG","CTTCAGTAGT","AAGGTTAAGT","TGAGCCGCGG","TGGCCGTCTT","AACCTTCTCT","GGCGCCATCG","GTCGACCATT","CATTACCAAG","CTAGTTAAGT","CATATTGCAT","GCCAAGGCAA","GATCCATAAC","ATGAATACCA","TTATTGCTAA","TATTCCTTGC","GGTACCGGCT","GTACTGGTTG","CGTTGATGAT","ATGCCTCTTC","TTATATTGAA","GTTCGTCTGA","ATCCGGATAA","TTGCCTTATC","ATCTAGTTAG","AGATAGAGGT","TTCTAATCCG","AAGATGGATT","TTCCAAGTAA","ATGAAGCTTG","ATCCTTGGAG","GTTCCGTATC","GCCGGAGCGG","AGATGGCGCA","TTATTAAGAA","CTCTTCCAGG","TTAGCGGTTG","AGTAGATCTA","GTATCAATAT","GGTCTTCGGT","CCTAGTCTAT","GACCGTTACT","TATGCTTACT","CAGGAATCGG","AGGAGTAAGG","TGAGGTTAGC","GCATCGCGCA","GAACGTCAGG","TGAGTTGGAC","ATAGCATCAA","TCTAGTTCCA","TGCGTCTATA","ATAGAGAGCC","TCTTAATCAG","CGGAAGACTT","GCCAGACTCA","TAACTGGCTT","AAGGCCATCA","GTATACGTAA","CCAATTCCAT","AATATAGCGG","GTTCGAGGCG","ACGTACTAGG","ATCGAATCTG","TCTGCGTCGC","TAAGCTCGCC","GGCATAACCG","AGTCGCGTCG","TGGACCAAGG","CTGATCAGAG","TCTCATTGCC","ACTCGGCATA","GAGCTCAGCC","ATTGAGGATA","TTAGCGGAAC","CCTTCATCCG","GGCAGCAGTT","TAAGTAAGTA","TATCAAGGTC","GCGGTTGGAA","GAATGAATAA","GAAGAGTATT","TACCTTAGCT","CGTCAGTCAA","GCGCCTAGTT","GTAGTAGTCC","ACGCTTCGTC","GATAGCCGAT","AGTCATGGAT","TCTTAAGGAC","CCGGTCCTAA"]
lig_i5_list = ["TGCTCCTTAT","CTCGATCTTC","GCAGGTCGTC","ACTAATCCAG","GCTGGTTATG","ATGAGTAATA","CAATAATTAA","GAAGCAGCGG","TGCGCCGAAG","TCCTGGTCAA","GTTAATTCTA","GCGTAAGATC","CTCAGAATAA","AACCTATAGT","ACCGGAAGAA","ATTGCATAGT","ATTCCTACCG","ACGCGACGGC","GTTCTCTCCT","TTATAGCTCT","AATCGTTGAT","TATTACTCTA","ATGCCAGCAA","CAAGTAGGAC","CTTACGTTGA","TTCGCGATGG","TCGATAAGAA","TTAGAGCTGA","TAGGTCCGCA","ATGCGATTGA","TACTATTAGA","CTATGGCCTA","CCGAACTATG","ACGATCAAGG","GGATGGTATT","GGAGGCCTCC","TTAACGACCG","AGACCGCAAG","ATTATCGATT","AGGTTGCAAG","TGCCGCAGAG","TTACTAGTAC","ACTTGCTGAT","TGAACGGCGT","TAAGGCTGGT","AGGCCGGCCA","AATCTCGCGT","CCGCCTCCGT","CGCTACGATT","GCTTGAGTCT","GAACTAACCT","GCGTCCAGGT","GGTCGACTTG","ACCATAATAA","GTCCTATGAA","GCTACCGTAG","TGGCTCATAT","TATCTGCCTA","CATGCGAGAA","ACTGGTAGGA","CCATATGCTC","GGATTCTCGG","TAGTCGGATG","TGGTCTTGAA","CGTCGCCTGC","GTTCGGAGAT","TCAGATTCTT","TATATGACGT","CCGTCGAATG","CAGCGTCCAA","TCGTTGCGGC","AAGAAGTCTA","ATAATCGCGG","ATGGAGCTAC","GCAGAGCCAT","ACTCTCTAGT","CAATGAGAAG","CTAATATGAT","TCGATGATAC","TTAACTCATA","CTACGACTAT","CCGGCGTTCG","AATATATCAA","AGACTACTAG","GGTTGGCGGT","GAATGAGGTT","TGCAGAGATG","CGTATTATAC","GTTAGGAGCG","CAAGCATACC","CCTATTGAGT","TGGTATTATT","GAATTATTCG","AAGCGGCATT","CTTGCGTAAC","CCTGCGTATT"]

lig_i7_to_well = barcode_to_well.get_well_dict_384_to_96(lig_i7_list, row_ordered=True)
pcr_to_well = barcode_to_well.get_pcr_plate_dict(pcr_i5_list, pcr_i7_list)
lig_i5_to_well = barcode_to_well.get_well_dict_384_to_96(lig_i5_list, row_ordered=False)

lig_i7 = set(lig_i7_list)
pcr_i7 = set(pcr_i7_list)
pcr_i5 = set(pcr_i5_list)
lig_i5 = set(lig_i5_list)



# 384-well 3LevelV2 and well mappings
lig_i7_list_384 = ["TTAGGCGTCC","GGTCTAACTG","ATTGAGACGG","AACGTACCAT","GTTCAGTTAC","GTTAACCTTA","GGAGTAGTAG","CAGGTTGAGA","AACCAATAAC","GGTACCTATT","AGCTGCCTCA","TTGGTTGGTA","CTGATATCGG","TTGATGGAAC","GGACCAGAAG","ACCTGAGGTC","TTGCAATGAG","ACTAACTGAC","GGTAAGAGGT","GTAATCGCAA","ATATGATGAA","CCTACGGAAG","GACTCTCCGA","ATAGATACGT","TATGAAGCAA","GTAGAGACGA","TTCGCATAAC","TAGATTCGCC","TTCTTCGCGG","TTCTTGGTCT","GTATAGATTA","GACTATGACT","GCTCCGCGAA","GGAACGATTC","GTACCTTCGT","TTATGCGACT","AACGGTTGGT","CTAGAAGGAA","GTATGGAGGA","CGTAAGTAGC","TAGTCGTCAA","GTAGTATGGA","AATGGACGTA","CCGTTCGCTG","CAGTCAATAT","GTCGGACTGA","TTCCATGCGC","GGACGGCATG","GGAGCAACGT","CGTCCTAGCT","ATATTAGTAG","AGTTCCTTCT","GCCTTCAAGG","TAACGCCTCA","GAATACGTCT","GATGAGCCTT","TACGGAGACT","AGAGGTCATT","CGGCCAGTTA","TAGCGCTTAA","CAACCTTATG","CTTCGACGAA","AGAGTCCGAG","CTATGGTTCG","AACTATTGGC","CTTGCGAGGT","TTCGGCTCGT","CTCAAGTCTG","ATTAGGCCTG","TGGCTAACGT","AGCTAATATT","AGGAATCTTC","AAGACCAGAC","ACCATAAGCG","TGCTTATTAC","ATAGAGCATT","AATTATCTTG","GTTCCGCGCG","CCGAAGTCCG","TTACCATGAT","TATAGATGGC","GCATATCTGG","ACTCTAGAAG","CAAGAATATG","CTGCTGCGCG","CATATTACGG","CGGCGGAATG","TGCTTCTGAA","GTATTCTTCT","CAGTAGTAAT","CCGCGGAGAC","GCTCGTCGGC","CTTAGAGGCA","GACCAAGACG","AGCAGATGGT","AATTAACCAT","CAGACTCGCT","CTTCGCCGTT","CCTGCCAACC","GAGATCGCGG","AATTGCCGTC","GCGCGGTCCG","GCGAAGGCTC","CATCGACTCA","CTCGGTTGCA","GTTAAGTATT","AGTTCCGGAC","CAGCGGTCGG","GACGCGGTAG","TTCTTCTATT","CAATTATAGT","ATAGGAGTTC","GTTATTAATT","ATGATCGCCA","ATCATCAGAA","GTTCGGCCTT","TTACGTCTAG","GCTGCATAGC","TGATTGCTTC","TAACTTGGAG","AACTTACGCT","GGTTCGTACC","CGCTCCTTGG","GCTTGCGCGT","AATCTAGTCC","TTGGAGAACG","GGTAGTCTTA","TGGAACCGTA","GAGTTAAGGT","GTTATCGGTA","CTACGAGTCG","CCTAATTCTG","TGCCTTGACG","TCTAATTATT","CGCAACCTGG","AGGCGGTCTC","TCTCGTTGAG","AATTACTAAT","CTATCCGGAG","TTCGTTCCTG","CGACCTATAC","CTGGCTTAGT","TACGCCGTAT","GAGTCCTGCA","TGGCGCAACT","CCGTCTACTA","AGGCTGATTA","CTCCATAATC","ATTACGTAGG","ACGTATGCGC","GTCTAATAGG","TCAGAACGAC","GTCCAGTCGT","TGATGCTGAT","CGCGTTACCT","TCTCTGATCG","GGTATCATCT","GCCTGGCAGT","TGGTTACGCT","CCTACCGTCC","CGCTCCAGAA","TTCCGCGTTA","CCGACGCGCC","GATCTTATCC","CGCGAGGATG","TGGAATATAG","GCGGCTACTC","GTTATGAGAA","CAACGTTGCC","AGTAGCCTTG","GCCGGTTAAC","AAGATATAGA","TCTCAGCGGC","TCCAAGGAGA","GACCAATTCT","GGACCTTGCA","TGATCAATTA","TTCTCCGCTA","TTGGACGCGG","AACTGCTAAG","CGAGTCGAAG","TCAGGATTAA","AAGGACCTTA","TCCTCTTAAC","TCATAGGCTT","GTTACGACTC","GAGGTCCAGT","GGAAGTCTGG","CATGATCGTT","CTCATGATTG","GGCAGAGGAG","GTTCTAGCCA","CAGCGGATAA","GCGAGAGAAG","TGAATAACTA","TGGAGAGGCC","GAGGACCGAT","CGCTGGCAAG","CTTGATTCAA","TTCCTCAAGG","TACTGGATAA","GGATGGTCCG","TGCGCGGCAT","AGCGCGGAAC","CTGGATGCCA","TTATCTTATT","GTCTTGATGC","TGGTCAAGAT","CCGTCAGTTG","TGACCTTAAT","CTGATTCTCT","CCTTCCTTCA","CATACGGATT","GAGCTTAGAA","CTTATCGCAG","CCGGCAATCC","GTTCTATTGG","CAATCGACGG","GGAGGAGCTT","GGTTATATTA","GATGGTTACC","AGCGTCTGGT","ATGGTACTCT","CGTAGGTTGG","ATCGGTTCCG","ATAGGTTATC","CGAGGCTACC","GCCATAGTAG","GGCCGTTGAT","TTCGACCAGA","CGCCTAGAGA","GTTCTCCGGA","CGCCTCGGCG","TGGATCTGCA","GTCTATACCA","TTATCCATCC","TGGACCGCCA","ACTCGCCGCT","TAGCATTGAT","GTCATCGACC","GTATAACTCC","CGGCGAGTCC","AGCCTGACTG","ACGAGCCTCT","ATGAAGGAGG","TGCTTCCGCC","ATGCGCGAGT","TATGAGTTGA","ATGGCTCGGT","GCTGGCTGAA","CTGGATTGGA","GTTGGCATGG","AGAATGCTGG","GGAGAGATCC","GTCAACTAAT","GGTACCAACC","ACGGCAAGCA","CCGGATTACT","GAAGGTTCGG","AGTAAGTTAC","GGCCTAGCGG","ACTGATGAGT","GCGGTCAGAG","TAGGTATGAA","GAGGCAAGGC","TTCGAACGTC","GTCCTGCCGA","TAGGCGATAT","GAACCTCTAA","GGAACGCCTA","GGTATTAGCG","TGCAAGCGCG","CCAACTGAAT","GGCATATATA","AGCCGAGGAC","AATGCTCTGA","GTATTGAAGT","TTAATGACTT","GTATCTCGAT","AGCCGTTCCA","GTACGATACT","ATGGTTAGAA","CCTTGGCGAA","TTGGCTACTA","CCGGAGGACC","AGAGAGTTGG","TTACGCCATT","ATATGCCGCG","CCTGGATAGT","GAGGCGTAAT","CGACGGAGGC","ATAAGTCGAA","TCGAGGTCTT","TCAGACTGGA","GTCGATTATG","CAGGACCAGC","GCGCAGGCGA","GTTAGCTAAG","CTACCATCTC","CTTACTTCCT","GACTTCTACT","TAACCGCTGA","CTTGCCAATA","ATAGTATTGC","CCGCGGTCAA","ATCTCCTGAA","CGGACCGGTA","ATAACCGTCC","TTCTGATTAA","GCCTACGTTC","CATTGATACC","AAGTCTTCTG","AGTTATTGAC","ATTAGTAACG","GTCATATTCG","CGACTTCGGA","TATCGTAGGA","ACCGCTCAAC","AGCTGCGTTG","TATTATTGGT","GCTATGCGAT","TAGGCTTCGA","CGTATCTGCT","TGGTTGAGGA","GTTCCAACTT","CATGGCGTCA","GTCGTTGCTT","ATTATACTAC","CGAATAGTTG","GGTAATGGAC","GGAGTCCATT","GATGAACGGT","GCGGTCTTAT","CTCCGAATGC","TGAGAACTTG","ACTCCGACCA","TAATCCTCTT","CAGTATGGTC","ACGTCTCCTC","CTCCAGGCGG","AAGATTCCTC","TCTCGAAGGC","ACTAGTCTCG","TCCAGCTCTC","TAACCTGCAA","GTTCTGACGT","CCAAGGTCGG","CGTTACTTAG","CGGCATGGAC","GTCTGCGCTT","TGAATTATGA","AAGCCGGTAA","CGCATTAATT","GGCCGACCGT","AGCGAAGTAG","GGCCATACTT","GAGAGTTAAC","GTTGGCGACC","AGGTTATACC","TTCTATAGTT","GAGGTCTGAC","GAGAATGAAG","GTCCGCAGTA","TTGGTTAACC","TTATGGCCGG","CAGACTTCAT","GTCGCTGGAG","TCGAGAAGGT","TCGGCGTACC","CAACGCCTGG","GCTGCCATTC","AAGTTCGTAA","TCATGCTCAG","TATCTCTCAT","GAGGCTTGGT","ACCAATATGG","GGAACTGAGC","GCCGAACTGC","TAATACGGAC","GGATATACGG","TTACTCTCTT","CGCAACGCCA","GTATAAGGCA","AGATAATTCC"]
pcr_i7_list_384 = ["GAATGCCTTG","CGGACTGGCC","CTGGCAGCGG","TCATCAGCCA","TAACCAGTTA","AGCTCATTCG","CAACGGTCTT","TGGTATCAGA","GGTAACTACG","CTTCAGGCCA","ATCCTTCAAC","TGATTGAATG","TGCTTAGCGA","CGAGTTCGCC","CGGCATCTTG","TCAACGAGGT","GGTCTAGGAA","AAGTCAACGG","TAACCAATCG","ATCGGCTTGA","CAATCTCAAT","CAGTTGCTTG","ATGCTAACCT","CGGATCTCCG","TGACGCGACC","TCTGACGAAC","GATCATGATA","TTCTCTACGA","TACGCAGGTT","TGCGAATCGG","CTAAGAGTTA","TCCATACCTG","ACCGGTCTGC","TAGAACCTCC","TGACCATCAG","GACTCGAGGA","GCATTAGGCG","GGACTTATGG","TTGGTTCTCA","TAATTCCGGT","CTACTGCAAG","CGTAGCCGTA","TTGACTTCGT","TCAGCGCAAT","ATATGGTACC","TGCCGGTACC","GGTACTTCCA","AATTGAGTTA","GCGGCGCAAG","AATACCTGCC","AGCATACGGC","GCCTCGGTAA","ACGGACCTGC","CATTCTGATG","GCTTACTATA","TCCAATGGTT","ACGGTAATTG","TCGGAGTATG","GGTTAGTTGG","CTGCATTACG","TGCGGCCTGG","CATCTATTCG","GCAGCTGATT","ATATCTTCCG","GTCGTACGCG","TTGATGCCTC","TTGGAACTGG","GGAGAATGGC","TTCCATTCTT","CCGAAGGTTA","CCGGCTGAGC","ACGAGGAGCC","AAGATCAGTT","ATCCGAACGG","CTGCGCTGGT","TGCCATGGAA","AGCTGAACGC","GAGACGTTCT","CTGACTACTT","CGCCGATATC","TGGATCGTTA","GTACCTGAAT","GAATTCTCCA","AGACCAGGTT","CTAGCTTCTT","GGCAACCTTC","CCGTTAGCAA","GGCGTCTGCC","CGCGCAACCG","AGTCTTAATT","TAAGGAACGG","TCGTTCATTA","ACTCCAGATT","CGATATATCT","GGCTGGCTCT","GGCGGATACC"]
pcr_i5_list_384 = ["GACCTCCTTG","ACCAGTTCAG","TTCTGGCGCA","GGCAATCAAG","TTGGCCAGGT","TCTCCTCCTG","CTTCAGTAGT","AAGGTTAAGT","TGAGCCGCGG","TGGCCGTCTT","AACCTTCTCT","GGCGCCATCG","GTCGACCATT","CATTACCAAG","CTAGTTAAGT","CATATTGCAT","GCCAAGGCAA","GATCCATAAC","ATGAATACCA","TTATTGCTAA","TATTCCTTGC","GGTACCGGCT","GTACTGGTTG","CGTTGATGAT","ATGCCTCTTC","TTATATTGAA","GTTCGTCTGA","ATCCGGATAA","TTGCCTTATC","ATCTAGTTAG","AGATAGAGGT","TTCTAATCCG","AAGATGGATT","TTCCAAGTAA","ATGAAGCTTG","ATCCTTGGAG","GTTCCGTATC","GCCGGAGCGG","AGATGGCGCA","TTATTAAGAA","CTCTTCCAGG","TTAGCGGTTG","AGTAGATCTA","GTATCAATAT","GGTCTTCGGT","CCTAGTCTAT","GACCGTTACT","TATGCTTACT","CAGGAATCGG","AGGAGTAAGG","TGAGGTTAGC","GCATCGCGCA","GAACGTCAGG","TGAGTTGGAC","ATAGCATCAA","TCTAGTTCCA","TGCGTCTATA","ATAGAGAGCC","TCTTAATCAG","CGGAAGACTT","GCCAGACTCA","TAACTGGCTT","AAGGCCATCA","GTATACGTAA","CCAATTCCAT","AATATAGCGG","GTTCGAGGCG","ACGTACTAGG","ATCGAATCTG","TCTGCGTCGC","TAAGCTCGCC","GGCATAACCG","AGTCGCGTCG","TGGACCAAGG","CTGATCAGAG","TCTCATTGCC","ACTCGGCATA","GAGCTCAGCC","ATTGAGGATA","TTAGCGGAAC","CCTTCATCCG","GGCAGCAGTT","TAAGTAAGTA","TATCAAGGTC","GCGGTTGGAA","GAATGAATAA","GAAGAGTATT","TACCTTAGCT","CGTCAGTCAA","GCGCCTAGTT","GTAGTAGTCC","ACGCTTCGTC","GATAGCCGAT","AGTCATGGAT","TCTTAAGGAC","CCGGTCCTAA"]
lig_i5_list_384 = ["AAGTAGACTA","ATGGAAGCAT","TGGATCAGGC","GTTACTTAGC","ACCGCCGCAA","CTCAAGTCCT","CGGTCGACTA","TTCGCCGTAA","GCTCCGCTTG","ACTTAAGATA","GGCATGGCCA","CTTCGGTATA","GAGATTCGCC","CTAGGCCGTT","GGCCAACGAT","ACGGAACCTG","TGATTCTCGT","TTGCGTCAAC","GAATGCAACC","TGCGGTTCAG","TTGGCCAACC","TTGGTTAAGC","CTTAAGTTCG","GTCCTCAGAA","GGAGTCGTCT","GGTACCTCTA","GATCGCTGAG","AGAGTACTCC","TCATTCTATT","GTTACTACCA","CCAGCTCGCC","CGCCGGTATG","TTAATTCGTA","GAAGGCTCCA","GAGACGTACG","GAAGAGCCTC","CCGATGCATA","GTAATGGTAT","TTCTATCTCA","GCAGCAGCTA","TTGCTCGATT","CCTCATCGGC","ACTTCAGCAA","AGGTCATCCT","AACGCGTCAG","CTATGCTTAC","GTTGCCGTTC","GCTTACCGCC","TGGCAAGTCA","CATCGAAGGA","AGAATCCTCG","GCAATCGGTT","CCTAAGATTC","CCTGCGCGCG","ATCAGCGCGA","GTACGATTCT","TTACCTTGCA","CCGGCTCAGC","TTCTGCAAGA","ATATACGCTT","CTCAGCAACC","CAATTCTAGG","ATCAGTCTCG","AATCCGCAAC","CGGTTACCTT","ACGTTAAGAC","CTATCCAACC","ATAAGCGAAT","CTTATATCGG","ATATGACGAC","TTACCGCATA","ATTCATCGCC","AGAAGCAGAA","GTTCGTCGTT","CATGCTTCCA","TCGGTACCAG","TTGAGCCAAT","AGATGACTGA","ACGCTAGAAG","GTTCAATTGC","GGACCGTCAA","CATTAACGGA","TAAGCAGTCC","CCGGTCAGTT","ATAACGGACT","ACGAGAAGAT","ATCCTCTTAA","AATCCAATAA","CTAGCAGGAT","TGGTCTCGGA","CCGAGTACTA","GATGACGAAG","GGCAGTCTTC","AATACGAATA","ACCTAGGAGA","GAAGCGCCAA","CGTTACGTTG","GTCGCGAATA","TTAGAGCCTG","ACGGTCATCA","ACGTAGCAGG","CGACCGAGAG","AAGCGGTTCT","TCGGAATAAC","AAGTTCGCTG","AATAATCGGT","AGGCGAAGGC","AAGCCGCCGC","TCGGCCGATG","AGCGACTGCT","CTTAATGAGC","AATTCCTCTC","GCTGGTCTCC","AGTATTGCTA","TCTAGGATAA","GGTCCTGCAA","CGCTTCAATT","GGATTATTAT","TCCGGCTGAT","CCGCCTCGTT","TTATAATCAA","CCATTGAACG","ACTCCAACGG","ACCTCCTGAA","AGAGGCCGGC","CTGCCTCTTC","CAGTATCCTT","GTCAACTAGC","TGACGCAGTC","GTCAATACGA","TGAACTTCGA","CGTACCAACG","AGAGATGAAT","TATTCCAATT","GGATGCGATT","GTAACCAGGT","CCTCGTCATA","AATGGTCTTA","ATGAATGCCT","GTCCGTAGAT","CCATCCTAGT","TGGTTCCTAC","GCGCCTTCCG","CGTACTACGC","GGCCGCGGTT","TGGATAGTTG","CGGCGCCAGG","CAAGCTCAGG","ATCATCCTTC","CCTCCGGAGT","CCATTGCTGG","TATTCGCAGT","CCGGTTAAGT","ATATTCTACC","TACGGATCGT","TTCTCTCCAG","CCAAGAGCAA","TTGGTTCGAG","AACGGATTAC","CATCTTCAGA","TTGAACCTCC","GGAATTCCAA","ATAGGTCCAA","GCCATGGTAC","GAGCTCTTCA","CCGAGGCAAC","GTCTCTAGTT","GCTGGTTATA","TCGTAGGTCA","AACTCAGACG","TGCTGCCGGA","TGGAGGCAAG","ACTGATGCGA","ACGACTCCTC","TGGCAGCGAA","CCGATACTCT","CAATATAGGC","ACCGGCCGAC","AATAAGGCTC","CATCATAGCA","GATGATCCAT","ATGGCAATAC","ACCAGAACCA","GGTTCGACCT","CTTGGACGGA","CGGTCTCATA","AATCAGAGCC","CCTGAATACT","CTTGGAGACT","AAGACCTTAC","GCGAGCGCTC","TCGCAAGACG","CAATCTCGGA","TCGACCTACC","TTATAGGCAT","TTCTGGCCTA","AATTGGCGAT","AGGCAACCGC","ACGCAATGAT","ACTCGTTACT","CAAGTCAGCA","GGTACGGATA","CTCAATGGTC","ACTCCGAAGA","AATCCAAGGC","CGTCCATCGC","TTAGGTACGA","CTTACCATCT","CGAGATAAGA","CGATCTTCTA","GTTCCGATCC","GCCATAAGAA","AGATTCATAA","CAGAGCGTCA","GAGGAGCCAG","ATGAGGATCC","CGGCGCTCAA","CCTTACGTCA","TTCTCAGTCA","ATAGGAGCTT","TAGCCGACTC","AAGAACTCCG","CTTGAGACCG","AACGCCATAC","CCTACTCAAC","TCTAGCCTCC","CGCTTAGATC","GCTTAATCAT","AGCAGGTCAA","CCGCTTATAA","CCTAATGGAA","CATTGGTTCC","ACCAGTTATT","GACTCGCTTA","AATTGCTCCG","TGCGAATGCC","TGCCTCCAGC","TTAGGCTTGA","ACTCTGAGCT","TTCGAACGAC","TACTGCTCGG","TCTAGAAGAC","TATTGGAATA","AAGATATCAA","AGTCCATGGT","GGTTGAATAC","CTAGCGATGG","CCAATACGCC","GAGATACCTC","GCTCAGGAGC","ACTAGTTGCA","CCGCTATCCA","ATGCAACTTA","AGGACCAAGT","GGCGTCCTCA","GGAAGCTCGC","AATCGTTATA","CCGAGAGAGG","GAGGAACTCA","GGTCTGAGCA","ACCATTAAGC","AACTCTACCA","TGCTCAACTC","CCGGCAGCCT","CTCGCGACCA","TGGACCTTAG","GGAATGACCG","CAGTATGATG","CTCATGAATA","CTGCGTAGTA","GGAGCAACCT","TCAGTAATAC","GACGCTGCAT","ATCTCCAGCT","TTAGAACTGC","CCGTAACGCC","GACTATACCT","TGCGAGAGGT","ATAGGCCTCA","TCAATTCAAC","GGCTACCTGG","CTTCTTGAAC","TTACGCAGCA","ATAACCGCCA","CCAGTCGAAT","TAACCAACTA","TAGCTGGCGA","CAATGACTTG","CTCTGCGATC","GCATACCAAT","ACCTGATAGG","ATGGTTACCG","CTTAGGTTAT","CGCCTTAGCC","ACGTAACGTA","TTATTCTCTA","GCATAGTATA","CATGCGCATA","GTACCAATTC","AACGAGATCA","TCTCGATTAA","CGTCGACCGG","GTTGATAGCT","CAGCGTTGGT","ATCGGCATTG","GGTAGTCCTA","TAGCATCGCG","ACTGGTAACC","TCTACTGACC","CAAGAGTTAT","CAATTAGGAA","TTGCGGAACC","AGCCGAAGTA","GGTCCGTACG","AGCATGCAAG","TCTTCGTTGC","GTTGGAAGAA","GGAATACGGA","ACCGACGGTA","ATACTTGATT","GTCGTTCGCC","AATGATTGCA","CCATTAGCAG","CTGACTAATG","CCTTACGGAC","CGCATAACTA","AACCGGAGGA","AATGCAGCGG","CAGTCGGCAA","ATAGAATCCA","TCTCAGATAT","ACGAAGTATT","AGACTTATCA","TCGCGCCGTA","AGCTTGAAGA","CGGTAGCTAC","GCGGCATGCG","AAGACTGGCT","CGCATTCTTA","TACCGTCTCC","AATATAGTAT","ATCATAAGAT","ATCAATATCC","TATTACCAAC","GAGAAGACCA","TGGCGCTCTC","GCGACGATAA","AACGTCGCGA","ATGAAGCTTC","GCCATAGAGT","TGACTGAGAA","CGGCTCCGAA","CAGCCAATTG","GCGACCAGTT","CCTAACGACG","CTTCGCAATC","TGACTCCGTT","GATAGTCGCT","AAGGTACTAA","TTGCATGAGG","GTATTATATA","ATTCTTGGCT","TGCATCTTGG","GTTGGCTCAA","AATATCATTA","TAACTAAGTC","CAATAACCAA","TTATACTGCA","TGAGCAGAGC","TGCAAGCCAA","TGGAGAACGA","ATCGGATTCA","ACTAGACCGA","CGAGATGCTT","TTCTATTAAT","AATTAGTCCA","GCTCCAAGCC","CTCTTCCTAA","CCGCGTTAAC","GACGGAATAG","CTCAGAGTTG","GGACGTATGA","AAGATGAGTC","ATGCGCTACC"]

lig_i7_to_well_384 = barcode_to_well.get_well_dict_384_to_96(lig_i7_list_384, row_ordered=True)
pcr_to_well_384 = barcode_to_well.get_pcr_plate_dict(pcr_i5_list_384, pcr_i7_list_384)
lig_i5_to_well_384 = barcode_to_well.get_well_dict_384_to_96(lig_i5_list_384, row_ordered=False)

#20200224 - bge: replace the following three lines with the preceding three.
#lig_i7_to_well_384 = barcode_to_well.get_well_dict(lig_i7_list_384, row_ordered=True)
#pcr_to_well_384 = barcode_to_well.get_pcr_plate_dict(pcr_i5_list_384, pcr_i7_list_384)
#lig_i5_to_well_384 = barcode_to_well.get_well_dict(lig_i5_list_384, row_ordered=False)

lig_i7_384 = set(lig_i7_list_384)
pcr_i7_384 = set(pcr_i7_list_384)
pcr_i5_384 = set(pcr_i5_list_384)
lig_i5_384 = set(lig_i5_list_384)

# Two-level Indexed TN5 barcode sets and well mappings
nex_i7_two_level_indexed_tn5_list = ["ATTACTCG", "TCCGGAGA", "CGCTCATT", "GAGATTCC", "ATTCAGAA", "GAATTCGT", "CTGAAGCT", "TAATGCGC", "CGGCTATG", "TCCGCGAA", "TCTCGCGC", "AGCGATAG"]
pcr_i7_two_level_indexed_tn5_list = ["TCGGATTCGG" ,"GCGGCTGCGG", "AGATTACGTT", "CTAACTAGGT", "CATAGCGACC", "CCGCTAAGAG", "ATGGAACGAA", "GCGTTCCGTT", "GGTTATCGAA", "GCATCGTATG", "AATACGATAA", "TTCCGTCGAC", "TCCGGCTTAT", "ACCAGGCGCA", "AGAGGAGAAT", "GTACTCCTAT", "GCTAACGGAT", "AGTTGAATCA", "TGATTAGGTA", "TCGTAGCATC", "TCTTGAGGTT", "AGGTCAGCTT", "TATTAGACTT", "CTCAATTAGT", "TCGCCGCCGG", "CCGTATGATT", "AACGCGCAGA", "CTCGTCGTAG", "CTAATTGCGA", "CGCGGCCATA", "AATATTACTT", "ATTGGCAGAT", "ATGGCGCCTG", "ATAAGGACTC", "TAGTAAGCCG", "ATTATGCAAG", "TTGGCAAGCC", "TTGATTGGCG", "GCATATGAGC", "GAACTCGACT", "CTAGCCAGCC", "TGCGACCTCT", "ATTCTTAGCT", "TTGATACGAT", "TATAATAGTT", "TTGCCGTAGG", "AGACCATATC", "TTGGTAAGGA", "CAGCTAGCGG", "CTAAGCCTTG", "CGTTACCGCT", "GACTGGACCA", "GCAAGACCGT", "TCAATCTCCT", "ATACCTCGAC", "TAGAGGCGTT", "TAGGTAACTT", "TTCGAATATT", "TGGACGACTA", "GTAGGCTGCA", "GTAGGATAAG", "CGTCGAGCGC", "ACTATTCATT", "TTGCTTAGAT", "CGAATGGAGC", "CTATATAGCC", "CTACTAATAA", "TGGTTGCCGT", "TCCTCTGCCG", "GATTCTTGAA", "GTAGCAGCTA", "CCTCAGCTCC", "AAGTAGCTCA", "TATTGCTGGA", "CCAGATACGG", "AACGAATTCG", "CGCTTATCGT", "AAGTACGCGA", "GATCTTCGCA", "TCTTAGCCTG", "TTATTGAGGC", "TTGCGAGCAT", "GCTTGAAGAG", "AGTCCGCTGC", "TAAGTCCTGA", "AGTTCTCATG", "CAGACTAAGG", "TCTATCGCTG", "GCGCTATGGT", "CATTATTATT", "AGCCGTAGTT", "TGATATTGCG", "ACGGCGTTAA", "GGCTTACTCC", "GCGCGTTCAT", "GAGCGCGATG"]
pcr_i5_two_level_indexed_tn5_list = ["CTCCATCGAG", "TTGGTAGTCG", "GGCCGTCAAC", "CCTAGACGAG", "TCGTTAGAGC", "CGTTCTATCA", "CGGAATCTAA", "ATGACTGATC", "TCAATATCGA", "GTAGACCTGG", "TTATGACCAA", "TTGGTCCGTT", "GGTACGTTAA", "CAATGAGTCC", "GATGCAGTTC", "CCATCGTTCC", "TTGAGAGAGT", "ACTGAGCGAC", "TGAGGAATCA", "CCTCCGACGG", "CATTGACGCT", "TCGTCCTTCG", "TGATACTCAA", "TTCTACCTCA", "TCGTCGGAAC", "ATCGAGATGA", "TAGACTAGTC", "GTCGAAGCAG", "AGGCGCTAGG", "AGATGCAACT", "AAGCCTACGA", "GTAGGCAATT", "GGAGGCGGCG", "CCAGTACTTG", "GGTCTCGCCG", "GGCGGAGGTC", "TAGTTCTAGA", "TTGGAGTTAG", "AGATCTTGGT", "GTAATGATCG", "CAGAGAGGTC", "TTAATTAGCC", "CTCTAACTCG", "TACGATCATC", "AGGCGAGAGC", "TCAAGATAGT", "TAATTGACCT", "CAGCCGGCTT", "AGAACCGGAG", "GAGATGCATG", "GATTACCGGA", "TCGTAACGGT", "TGGCGACGGA", "AGTCATAGCC", "GTCAAGTCCA", "ATTCGGAAGT", "GTCGGTAGTT", "AGGACGGACG", "CTCCTGGACC", "TAGCCTCGTT", "GGTTGAACGT", "AGGTCCTCGT", "GGAAGTTATA", "TGGTAATCCT", "AAGCTAGGTT", "TCCGCGGACT", "TGCGGATAGT", "TGGCAGCTCG", "TGCTACGGTC", "GCGCAATGAC", "CTTAATCTTG", "GGAGTTGCGT", "ACTCGTATCA", "GGTAATAATG", "TCCTTATAGA", "CCGACTCCAA", "GCCAAGCTTG", "CATATCCTAT", "ACCTACGCCA", "GGAATTCAGT", "TGGCGTAGAA", "ATTGCGGCCA", "TTCAGCTTGG", "CCATCTGGCA", "CTTATAAGTT", "GATTAGATGA", "TATAGGATCT", "AGCTTATAGG", "GTCTGCAATC", "CGCCTCTTAT", "GTTGGATCTT", "GCGATTGCAG", "TGCCAGTTGC", "CTTAGGTATC", "GAGACCTACC", "ATTGACCGAG"]
nex_i5_two_level_indexed_tn5_list = ["TATAGCCT", "ATAGAGGC", "CCTATCCT", "GGCTCTGA", "AGGCGAAG", "TAATCTTA", "CAGGACGT", "GTACTGAC"]

nex_two_level_indexed_tn5_list = barcode_to_well.get_row_col_matrix(nex_i5_two_level_indexed_tn5_list, nex_i7_two_level_indexed_tn5_list)
nex_two_level_indexed_tn5_to_well = barcode_to_well.get_well_dict_384_to_96(nex_two_level_indexed_tn5_list, row_ordered=True)
pcr_two_level_indexed_tn5_to_well = barcode_to_well.get_pcr_plate_dict(pcr_i5_two_level_indexed_tn5_list, pcr_i7_two_level_indexed_tn5_list)

nex_i7_two_level_indexed_tn5 = set(nex_i7_two_level_indexed_tn5_list)
pcr_i7_two_level_indexed_tn5 = set(pcr_i7_two_level_indexed_tn5_list)
pcr_i5_two_level_indexed_tn5 = set(pcr_i5_two_level_indexed_tn5_list)
nex_i5_two_level_indexed_tn5 = set(nex_i5_two_level_indexed_tn5_list)