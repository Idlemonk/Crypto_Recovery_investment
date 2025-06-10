from django.db import migrations, models


def change_column_type(apps, schema_editor):
    # Get the model
    BlockchainTransaction = apps.get_model('Restapi_app', 'BlockchainTransaction')
    db_alias = schema_editor.connection.alias

    # Add a new column
    schema_editor.execute(
        "ALTER TABLE BlockchainTransaction ADD COLUMN new_amount NUMBER(20,8)"
    )

    # Copy data from the old column to the new column
    schema_editor.execute(
        "UPDATE BlockchainTransaction SET new_amount = AMOUNT"
    )

    # Drop the old column
    schema_editor.execute(
        "ALTER TABLE BlockchainTransaction DROP COLUMN AMOUNT"
    )

    # Rename the new column to the original name
    schema_editor.execute(
        "ALTER TABLE BlockchainTransaction RENAME COLUMN new_amount TO AMOUNT"
    )


class Migration(migrations.Migration):
    atomic = False  # Disable transactions for this migration

    dependencies = [
        ('Restapi_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(change_column_type),
    ]
    

