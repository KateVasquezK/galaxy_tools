import logging

from galaxy.util.dictifiable import Dictifiable

log = logging.getLogger(__name__)


class Collector(Dictifiable):
    dict_collection_visible_keys = ['id', 'person_id', 'contact_id']

    def __init__(self, person_id=None, contact_id=None):
        self.person_id = person_id
        self.contact_id = contact_id

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Colony(Dictifiable):
    dict_collection_visible_keys = ['id', 'latitude', 'longitude', 'depth', 'reef_id']

    def __init__(self, latitude=None, longitude=None, depth=None, reef_id=None):
        # Latitude in decimal degrees, WGS84 datum, geographic location of
        # the wild donor colony from which the sample was collected.
        self.latitude = latitude
        # Longitude in decimal degrees, WGS84 datum, geographic location of
        # the wild donor colony from which the sample was collected.
        self.longitude = longitude
        # Depth in meters of the wild donor colony.
        self.depth = depth
        self.reef_id = reef_id

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Coralvcf_allele(Dictifiable):
    dict_collection_visible_keys = ['id', 'chr', 'pos', 'sample_id', 'ref', 'alt', 'qual', 'filter',
        'ac', 'an', 'bqb', 'dp', 'hob', 'icb', 'idf', 'imf', 'indel', 'mq', 'mqof', 'mqb', 'mqsb',
        'rpb', 'sgb', 'vdb']

    def __init__(self, chr=None, pos=None, sample_id=None, ref=None, alt=None, qual=None,
                 filter=None, ac=None, an=None, bqb=None, dp=None, hob=None, icb=None, idf=None,
                 imf=None, indel=None, mq=None, mqof=None, mqb=None, mqsb=None, rpb=None, sgb=None,
                 vdb=None):
        self.chr = chr
        self.pos = pos
        self.sample_id = sample_id
        self.ref = ref
        self.alt = alt
        self.qual = qual
        self.filter = filter
        self.ac = ac
        self.an = an
        self.bqb = bqb
        self.dp = dp
        self.hob = hob
        self.icb = icb
        self.idf = idf
        self.imf = imf
        self.indel = indel
        self.mq = mq
        self.mqof = mqof
        self.mqb = mqb
        self.mqsb = mqsb
        self.rpb = rpb
        self.sgb = sgb
        self.vdb = vdb

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Experiment(Dictifiable):
    dict_collection_visible_keys = ['id', 'seq_facility', 'array_version', 'data_sharing', 'data_hold']

    def __init__(self, seq_facility=None, array_version=None, data_sharing=None, data_hold=None):
        # Description of experiment metadata.
        self.seq_facility = seq_facility
        self.array_version = array_version
        self.data_sharing = data_sharing
        self.data_hold = data_hold

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Genotype(Dictifiable):
    dict_collection_visible_keys = ['id', 'coral_mlg_clonal_id', 'symbiot_mlg_clonal_id',
        'genetic_coral_species_call', 'percent_missing_data', 'percent_apalm', 'percent_acerv',
        'percent_mixed']

    def __init__(self, coral_mlg_clonal_id=None, symbiot_mlg_clonal_id=None, genetic_coral_species_call=None,
                 percent_missing_data=None, percent_apalm=None, percent_acerv=None, percent_mixed=None):
        # Description of experiment metadata.
        self.coral_mlg_clonal_id = coral_mlg_clonal_id
        self.symbiot_mlg_clonal_id = symbiot_mlg_clonal_id
        self.genetic_coral_species_call = genetic_coral_species_call
        self.percent_missing_data = percent_missing_data
        self.percent_apalm = percent_apalm
        self.percent_acerv = percent_acerv
        self.percent_mixed = percent_mixed

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Idx_annotation(Dictifiable):
    dict_collection_visible_keys = ['id', 'probe_set_id', 'chr_id', 'start', 'stop', 'strand',
                                    'dbsnp_rs_id', 'strand_vs_dbsnp', 'probe_count', 'cytoband',
                                    'chrx_par', 'allele_a', 'allele_b']

    def __init__(self, probe_set_id=None, chr_id=None, start=None, stop=None, strand=None,
                 dbsnp_rs_id=None, strand_vs_dbsnp=None, probe_count=None, cytoband=None,
                 chrx_par=None, allele_a=None, allele_b=None):
        self.probe_set_id = probe_set_id
        self.chr_id = chr_id
        self.start = start
        self.stop = stop
        self.strand = strand
        self.dbsnp_rs_id = dbsnp_rs_id
        self.strand_vs_dbsnp = strand_vs_dbsnp
        self.probe_count = probe_count
        self.cytoband = cytoband
        self.chrx_par = chrx_par
        self.allele_a = allele_a
        self.allele_b = allele_b

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Person(Dictifiable):
    dict_collection_visible_keys = ['id', 'lastname', 'firstname', 'organization', 'email']

    def __init__(self, lastname=None, firstname=None, organization=None, email=None):
        self.lastname = lastname
        self.firstname = firstname
        self.organization = organization
        self.email = email

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Probe_annotation(Dictifiable):
    dict_collection_visible_keys = ['id', 'probe_set_id', 'affy_snp_id', 'chr_id', 'start', 'stop',
                                    'strand', 'dbsnp_rs_id', 'dbsnp_loctype', 'in_hapmap', 'strand_vs_dbsnp',
                                    'probe_count', 'cytoband', 'chrx_par', 'flank', 'allele_a', 'allele_b',
                                    'ref_allele', 'alt_allele', 'associated_gene', 'genetic_map',
                                    'microsatellite', 'heterozygous_allele_frequencies', 'allele_frequency_count',
                                    'allele_frequencies', 'minor_allele', 'minor_allele_frequency',
                                    'omim', 'biomedical', 'annotation_notes', 'allele_count', 'ordered_alleles',
                                    'chrtype', 'custchr', 'custid', 'custpos', 'organism', 'pconvert',
                                    'recommendation', 'ref_str', 'snp_priority']

    def __init__(self, probe_set_id=None, affy_snp_id=None, chr_id=None, start=None, stop=None, strand=None,
                 dbsnp_rs_id=None, dbsnp_loctype=None, in_hapmap=None, strand_vs_dbsnp=None, probe_count=None,
                 cytoband=None, chrx_par=None, flank=None, allele_a=None, allele_b=None, ref_allele=None,
                 alt_allele=None, associated_gene=None, genetic_map=None, microsatellite=None,
                 heterozygous_allele_frequencies=None, allele_frequency_count=None, allele_frequencies=None,
                 minor_allele=None, minor_allele_frequency=None, omim=None, biomedical=None, annotation_notes=None,
                 allele_count=None, ordered_alleles=None, chrtype=None, custchr=None, custid=None, custpos=None,
                 organism=None, pconvert=None, recommendation=None, ref_str=None, snp_priority=None):
        self.probe_set_id = probe_set_id
        self.affy_snp_id = affy_snp_id
        self.chr_id = chr_id
        self.start = start
        self.stop = stop
        self.strand = strand
        self.dbsnp_rs_id = dbsnp_rs_id
        self.dbsnp_loctype = dbsnp_loctype
        self.in_hapmap = in_hapmap
        self.strand_vs_dbsnp = strand_vs_dbsnp
        self.probe_count = probe_count
        self.cytoband = cytoband
        self.chrx_par = chrx_par
        self.flank = flank
        self.allele_a = allele_a
        self.allele_b = allele_b
        self.ref_allele = ref_allele
        self.alt_allele = alt_allele
        self.associated_gene = associated_gene
        self.genetic_map = genetic_map
        self.microsatellite = microsatellite
        self.heterozygous_allele_frequencies = heterozygous_allele_frequencies
        self.allele_frequency_count = allele_frequency_count
        self.allele_frequencies = allele_frequencies
        self.minor_allele = minor_allele
        self.minor_allele_frequency = minor_allele_frequency
        self.omim = omim
        self.biomedical = biomedical
        self.annotation_notes = annotation_notes
        self.allele_count = allele_count
        self.ordered_alleles = ordered_alleles
        self.chrtype = chrtype
        self.custchr = custchr
        self.custid = custid
        self.custpos = custpos
        self.organism = organism
        self.pconvert = pconvert
        self.recommendation = recommendation
        self.ref_str = ref_str
        self.snp_priority = snp_priority

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Reef(Dictifiable):
    dict_collection_visible_keys = ['id', 'name', 'region', 'latitude', 'longitude']

    def __init__(self, name=None, region=None, latitude=None, longitude=None):
        self.name = name
        self.region = region
        # Latitude in decimal degrees, WGS84 datum, geographic location of reef.
        self.latitude = latitude
        # Longitude in decimal degrees, WGS84 datum, geographic location of reef.
        self.longitude = longitude

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Sample(Dictifiable):
    dict_collection_visible_keys = ['id', 'sample_id', 'genotype_id', 'experiment_id',
        'colony_id', 'taxonomy_id', 'collector_id', 'collection_date', 'user_specimen_id',
         'depth', 'dna_extraction_method', 'dna_concentration', 'duplicate_sample']

    def __init__(self, sample_id=None, genotype_id=None, experiment_id=None, colony_id=None,
                 taxonomy_id=None, collector_id=None, collection_date=None, user_specimen_id=None,
                 depth=None, dna_extraction_method=None, dna_concentration=None, duplicate_sample=None):
        self.sample_id = sample_id
        self.genotype_id = genotype_id
        self.experiment_id = experiment_id
        self.colony_id = colony_id
        self.taxonomy_id = taxonomy_id
        self.collector_id = collector_id
        self.collection_date = collection_date
        # User specific identification for samples, should limit to some sort of length.
        self.user_specimen_id = user_specimen_id
        # Depth in meters of the sample for this entry.
        self.depth = depth
        # Method used to extract DNA.
        self.dna_extraction_method = dna_extraction_method
        # DNA concentration in ug.
        self.dna_concentration = dna_concentration
        # Indicate whether DNA from this colony or sample has been run before
        self.duplicate_sample = duplicate_sample

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval


class Taxonomy(Dictifiable):
    dict_collection_visible_keys = ['id', 'species_name', 'genus_name']

    def __init__(self, species_name=None, genus_name=None):
        self.species_name = species_name
        self.genus_name = genus_name

    def as_dict(self, value_mapper=None):
        return self.to_dict(view='element', value_mapper=value_mapper)

    def to_dict(self, view='collection', value_mapper=None):
        if value_mapper is None:
            value_mapper = {}
        rval = {}
        try:
            visible_keys = self.__getattribute__('dict_' + view + '_visible_keys')
        except AttributeError:
            raise Exception('Unknown API view: %s' % view)
        for key in visible_keys:
            try:
                rval[key] = self.__getattribute__(key)
                if key in value_mapper:
                    rval[key] = value_mapper.get(key, rval[key])
            except AttributeError:
                rval[key] = None
        return rval