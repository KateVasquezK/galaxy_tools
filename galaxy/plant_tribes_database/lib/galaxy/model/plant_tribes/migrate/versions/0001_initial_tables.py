import logging

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    Table,
    TEXT
)
from sqlalchemy.dialects.postgresql import JSON

# Need our custom types, but don't import anything else from model
from galaxy.model.custom_types import TrimmedString

log = logging.getLogger(__name__)
metadata = MetaData()

PlantTribesScaffold_table = Table("plant_tribes_scaffold", metadata,
    Column("id", Integer, primary_key=True),
    Column("scaffold_id", TrimmedString(10), index=True, nullable=False),
    Column("clustering_method", TrimmedString(30), index=True, nullable=False))


PlantTribesTaxon_table = Table("plant_tribes_taxon", metadata,
    Column("id", Integer, primary_key=True),
    Column("species_name", TrimmedString(50), index=True, nullable=False),
    Column("scaffold_id", Integer, ForeignKey("plant_tribes_scaffold.id"), index=True, nullable=False),
    Column("num_genes", Integer, nullable=False),
    Column("species_family", TrimmedString(50), nullable=False),
    Column("species_order", TrimmedString(50), nullable=False),
    Column("species_group", TrimmedString(50), nullable=False),
    Column("species_clade", TrimmedString(50), nullable=False))


PlantTribesOrthogroup_table = Table("plant_tribes_orthogroup", metadata,
    Column("id", Integer, primary_key=True),
    Column("orthogroup_id", Integer, index=True, nullable=False),
    Column("scaffold_id", Integer, ForeignKey("plant_tribes_scaffold.id"), index=True, nullable=False),
    Column("num_species", Integer, nullable=False),
    Column("num_genes", Integer, nullable=False),
    Column("super_ortho_1_2", TrimmedString(10), nullable=False),
    Column("super_ortho_1_5", TrimmedString(10), nullable=False),
    Column("super_ortho_1_8", TrimmedString(10), nullable=False),
    Column("super_ortho_2_0", TrimmedString(10), nullable=False),
    Column("super_ortho_2_5", TrimmedString(10), nullable=False),
    Column("super_ortho_3_0", TrimmedString(10), nullable=False),
    Column("super_ortho_3_5", TrimmedString(10), nullable=False),
    Column("super_ortho_4_0", TrimmedString(10), nullable=False),
    Column("super_ortho_4_5", TrimmedString(10), nullable=False),
    Column("super_ortho_5_0", TrimmedString(10), nullable=False),
    Column("ahrd_description", JSON),
    Column("tair_description", JSON),
    Column("pfam_description", JSON),
    Column("interproscan_description", JSON),
    Column("molecular_function", JSON),
    Column("biological_process", JSON),
    Column("cellular_component", JSON))

PlantTribesGene_table = Table("plant_tribes_gene", metadata,
    Column("id", Integer, primary_key=True),
    Column("gene_id", TrimmedString(100), index=True, nullable=False),
    Column("dna_sequence", TEXT, nullable=False),
    Column("aa_sequence", TEXT, nullable=False))

GeneScaffoldOrthogroupTaxonAssociation_table = Table("gene_scaffold_orthogroup_taxon_association", metadata,
    Column("id", Integer, primary_key=True),
    Column("gene_id",Integer, ForeignKey("plant_tribes_gene.id"), index=True, nullable=False),
    Column("scaffold_id", Integer, ForeignKey("plant_tribes_scaffold.id"), index=True, nullable=False),
    Column("orthogroup_id", Integer, ForeignKey("plant_tribes_orthogroup.id"), index=True, nullable=False),
    Column("taxon_id", Integer, ForeignKey("plant_tribes_taxon.id"), index=True, nullable=False))


def upgrade(migrate_engine):
    print(__doc__)
    metadata.bind = migrate_engine
    metadata.create_all()
