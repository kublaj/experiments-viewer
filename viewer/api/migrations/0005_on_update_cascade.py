# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-12-02 19:20
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_collection_subgroup'),
    ]

    operations = [
        migrations.RunSQL(
            [
                """
                  ALTER TABLE api_collection
                    DROP CONSTRAINT api_collection_dataset_id_cf7b03de_fk_api_dataset_id,
                    ADD CONSTRAINT api_collection_dataset_id_cf7b03de_fk_api_dataset_id
                      FOREIGN KEY (dataset_id)
                      REFERENCES api_dataset(id)
                      ON DELETE CASCADE
                      ON UPDATE CASCADE
                      DEFERRABLE INITIALLY DEFERRED
                """,
            ]
        )
    ]
